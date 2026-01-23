from machine import Pin, I2C, ADC
import time


# ----------------------------
# Grove 16x2 LCD (I2C) Driver
# ----------------------------
class GroveLCD1602:
    """
    Treiber für Grove 16x2 LCD (monochrom) mit I2C-Adresse typ. 0x3E.
    Unterstützt: clear(), set_cursor(), write_line()
    """

    def __init__(self, i2c: I2C, addr: int = 0x3E, cols: int = 16, rows: int = 2):
        self.i2c = i2c
        self.addr = addr
        self.cols = cols
        self.rows = rows
        self._init_lcd()

    def _write_cmd(self, cmd: int):
        # Control byte 0x80 = command
        self.i2c.writeto(self.addr, bytes([0x80, cmd & 0xFF]))
        time.sleep_ms(2)

    def _write_data(self, data: int):
        # Control byte 0x40 = data
        self.i2c.writeto(self.addr, bytes([0x40, data & 0xFF]))

    def _init_lcd(self):
        time.sleep_ms(50)
        self._write_cmd(0x38)  # Function set: 8-bit, 2 lines
        self._write_cmd(0x08)  # Display OFF
        self._write_cmd(0x01)  # Clear
        time.sleep_ms(10)
        self._write_cmd(0x06)  # Entry mode
        self._write_cmd(0x0C)  # Display ON, cursor OFF
        self.clear()

    def clear(self):
        self._write_cmd(0x01)
        time.sleep_ms(10)

    def set_cursor(self, col: int, row: int):
        # Zeilenoffsets für 16x2
        row_offsets = [0x00, 0x40, 0x14, 0x54]
        if row < 0:
            row = 0
        if row >= self.rows:
            row = self.rows - 1
        if col < 0:
            col = 0
        if col >= self.cols:
            col = self.cols - 1
        self._write_cmd(0x80 | (row_offsets[row] + col))

    def print(self, text: str):
        for ch in text:
            self._write_data(ord(ch))

    def write_line(self, row: int, text):
        # MicroPython-sicher: kein ljust()
        if not isinstance(text, str):
            text = str(text)

        s = text[:self.cols]
        if len(s) < self.cols:
            s = s + (" " * (self.cols - len(s)))  # mit Spaces auffüllen

        self.set_cursor(0, row)
        self.print(s)


# ----------------------------
# Helpers
# ----------------------------
def read_adc_avg(adc: ADC, n: int = 10) -> int:
    total = 0
    for _ in range(n):
        total += adc.read_u16()
        time.sleep_ms(5)
    return total // n


def clamp(x: int, lo: int, hi: int) -> int:
    return lo if x < lo else hi if x > hi else x


def to_percent(raw: int, dry_raw: int, wet_raw: int) -> int:
    # Annahme: höherer ADC = feuchter
    if wet_raw == dry_raw:
        return 0
    pct = int((raw - dry_raw) * 100 / (wet_raw - dry_raw))
    return clamp(pct, 0, 100)


def setup_i2c():
    """
    Viele Pico-Grove-Shields nutzen I2C1 (GP6/GP7).
    Manche Layouts nutzen I2C0 (GP0/GP1).
    Wir probieren beides automatisch.
    """
    # Versuch 1: I2C1 auf GP6/GP7
    try:
        i2c1 = I2C(1, sda=Pin(6), scl=Pin(7), freq=400_000)
        if i2c1.scan():
            return i2c1
    except Exception:
        pass

    # Versuch 2: I2C0 auf GP0/GP1
    try:
        i2c0 = I2C(0, sda=Pin(0), scl=Pin(1), freq=400_000)
        if i2c0.scan():
            return i2c0
    except Exception:
        pass

    # Wenn beide leer sind, gib trotzdem I2C1 zurück, damit scan/Fehler sauber ist
    return I2C(1, sda=Pin(6), scl=Pin(7), freq=400_000)


def find_lcd_address(i2c: I2C):
    """
    Grove 16x2 LCD ist häufig 0x3E.
    Manche LCD-Backpacks sind 0x27.
    """
    devs = i2c.scan()
    for addr in (0x3E, 0x27):
        if addr in devs:
            return addr, devs
    return None, devs


# ----------------------------
# Main
# ----------------------------
# Moisture Sensor v1.4 an A0 => ADC0 (GPIO26)
moisture_adc = ADC(0)

# Kalibrierwerte (bitte später durch deine Messwerte ersetzen)
DRY_RAW = 19000   # trocken
WET_RAW = 61000   # sehr nass

SAMPLES = 10
UPDATE_MS = 500

i2c = setup_i2c()
lcd_addr, devices = find_lcd_address(i2c)

if lcd_addr is None:
    raise RuntimeError(
        "LCD nicht gefunden. I2C-Scan gefunden: %s. "
        "Prüfe: LCD am I2C-Port, Shield auf 3.3V, Verkabelung."
        % [hex(d) for d in devices]
    )

lcd = GroveLCD1602(i2c, addr=lcd_addr, cols=16, rows=2)
lcd.clear()
lcd.write_line(0, "Moisture Sensor")
lcd.write_line(1, "LCD: " + hex(lcd_addr))
time.sleep(1)

while True:
    raw = read_adc_avg(moisture_adc, SAMPLES)
    pct = to_percent(raw, DRY_RAW, WET_RAW)

    lcd.write_line(0, "Moisture: %3d%%" % pct)
    lcd.write_line(1, "ADC: %5d" % raw)

    time.sleep_ms(UPDATE_MS)
