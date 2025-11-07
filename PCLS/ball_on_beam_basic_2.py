from machine import Pin, I2C, PWM
from vl53l0x import VL53L0X
from ssd1306 import SSD1306_I2C
from utime import sleep, ticks_ms, ticks_diff

def setAngle(angle, pwm):
    """
    Function to convert an angle (in degree) into a PWM duty.
    For our servo, a duty of 1000 to 9000 corresponds to -90 to 90 degrees.
    """
    assert pwm.freq() == 50  # This code makes sense only for 50 Hz PWM
    position = int((angle + 90)/180*8000 + 1000)
    pwm.duty_u16(position)


###############################################################################
# Set up connections (GLEICHE PINS WIE IM ALTEN CODE)
# I2C0: VL53L0X + OLED
i2c0 = I2C(0, scl=Pin(9), sda=Pin(8), freq=400_000)

# Optional: kurzer I2C-Scan zum Debuggen (sollte 0x29 und 0x3C/0x3D zeigen)
try:
    found = i2c0.scan()
    # print("I2C devices:", [hex(a) for a in found])  # bei Bedarf auskommentieren
except:
    found = []

# Set up distance sensor (Adresse intern: 0x29, braucht keine Angabe)
tof = VL53L0X(i2c0)

# OLED Display (SSD1306) auf I2C0, Standard: 0x3C
# Wenn dein Modul 0x3D nutzt, setze addr=0x3D
OLED_W = 128
OLED_H = 64
oled = SSD1306_I2C(OLED_W, OLED_H, i2c0, addr=0x3C)

# Startbildschirm
oled.fill(0)
oled.text("Ball-on-Beam", 0, 0)
oled.text("Init...", 0, 16)
if 0x29 in found: oled.text("VL53L0X OK", 0, 32)
if 0x3C in found or 0x3D in found: oled.text("OLED OK", 0, 48)
oled.show()

# Servo wie gehabt auf D16 (GP16)
servo = PWM(Pin(16))
servo.freq(50)

# Regler-Parameter und Variablen
x_set = 180
e_old = 0
e_int = 0
x_glatt = 0
u_glatt = 0
kp = 0.1
ki = 0.015
kd = 0.055
dt = 0.01
alpha = 0.27
beta = 0.27

# Display-Update-Takt (~10 Hz)
DISPLAY_PERIOD_MS = 100
last_disp = ticks_ms()

def draw_display(distance_mm, angle_deg):
    """Einfaches Display-Layout: Distanz, Winkel, Balkenanzeige."""
    oled.fill(0)
    oled.text("Distanz:", 0, 0)
    try:
        d_mm = int(distance_mm)
    except:
        d_mm = 0
    oled.text("{:>4} mm".format(d_mm), 0, 16)

    oled.text("Winkel:", 0, 36)
    try:
        a_deg = float(angle_deg)
    except:
        a_deg = 0.0
    oled.text("{:>5.1f} deg".format(a_deg), 0, 52)

    # Balken (0..OLED_W) zur Visualisierung der Distanz
    span_mm = 300  # grob skaliert 0..300 mm auf 0..128 px
    bar_w = int(max(0, min(OLED_W, OLED_W * (d_mm / span_mm))))
    for x in range(bar_w):
        oled.pixel(x, 28, 1)

    oled.show()

while True:
    # Distance messen
    x_new = tof.ping()
    if x_new is None:
        # Sensor-Lücke: weiter warten und erneut probieren
        sleep(dt)
        continue

    # Glättung und Regler
    x_glatt = alpha * x_new + (1 - alpha) * x_glatt
    e_new = float(x_set - x_glatt)
    e_int += e_new

    u_new = kp * e_new + kd * (e_new - e_old) / dt + ki * dt * e_int
    u_glatt = beta * u_new + (1 - beta) * u_glatt
    e_old = e_new

    # Servo ansteuern
    setAngle(u_glatt, servo)

    # Display ~10x/s aktualisieren
    now = ticks_ms()
    if ticks_diff(now, last_disp) >= DISPLAY_PERIOD_MS:
        draw_display(x_new, u_glatt)
        last_disp = now

    sleep(dt)
