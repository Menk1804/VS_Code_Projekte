# ###############################################################################
# # PCLS / Physical Computing in Life Sciences
# # Norman Juchler
# ###############################################################################

# ###############################################################################
# # Ball on beam: Basic control loop, without signal smoothing
# ###############################################################################
# # 
# # Setup:
# #   - I2C0: TOF sensor
# #   - D16:  Servo motor
# ###############################################################################

# from machine import Pin, I2C, PWM
# from vl53l0x import VL53L0X
# from utime import sleep

# def setAngle(angle, pwm):
#     """
#     Function to convert an angle (in degree) into a PWM duty.
#     For our servo, a duty of 1000 to 9000 corresponds to -90 to 90 degrees.
#     """
#     assert pwm.freq() == 50  # This code makes sense only for 50 Hz PWM
#     position = int((angle + 90)/180*8000 + 1000)
#     pwm.duty_u16(position)


# ###############################################################################

# # Set up connections
# i2c0 = I2C(id=0, scl=Pin(9), sda=Pin(8))
# i2c1 = I2C(id=1, scl=Pin(7), sda=Pin(6))

# # Set up distance sensor
# tof = VL53L0X(i2c0)

# # Set up the servo motor
# servo = PWM(Pin(16))  # Servo at output D16
# servo.freq(50)        # 50 PWM frequency (don't change!)

# # Specify the target position (in mm)
# # That's where the ball should go.
# x_set = 200

# while True:

#     # Measure new sensor data
#     x_new = tof.ping()

#     # Compare measured data with set point (x_set)
#     e_new = float(x_set - x_new)

#     # Compute the new control signal (angle)
#     u_new = 0.1*e_new

#     # Apply the new beam angle
#     setAngle(u_new, servo)
    
#     # Wait a bit
#     sleep(0.01)


###############################################################################
# PCLS / Physical Computing in Life Sciences
# Norman Juchler
###############################################################################

###############################################################################
# Ball on beam: Basic control loop, without signal smoothing
###############################################################################
# 
# Setup:
#   - I2C0: TOF sensor
#   - D16:  Servo motor
###############################################################################

from machine import Pin, I2C, PWM
from vl53l0x import VL53L0X
from utime import sleep

def setAngle(angle, pwm):
    """
    Function to convert an angle (in degree) into a PWM duty.
    For our servo, a duty of 1000 to 9000 corresponds to -90 to 90 degrees.
    """
    assert pwm.freq() == 50  # This code makes sense only for 50 Hz PWM
    position = int((angle + 90)/180*8000 + 1000)
    pwm.duty_u16(position)


###############################################################################

# Set up connections
i2c0 = I2C(id=0, scl=Pin(9), sda=Pin(8))
i2c1 = I2C(id=1, scl=Pin(7), sda=Pin(6))

# Set up distance sensor
tof = VL53L0X(i2c0)

# Set up the servo motor
servo = PWM(Pin(16))  # Servo at output D16
servo.freq(50)        # 50 PWM frequency (don't change!)

# Specify the target position (in mm)
# That's where the ball should go.
x_set = 180
e_old = 0
e_int = 0
x_glatt = 0
u_glatt = 0 # Version mit u_glatt
kp = 0.1 # 0.1
ki = 0.015
kd = 0.055
dt = 0.01
alpha = 0.27 #0.27
beta = 0.27

while True:

    # Measure new sensor data
    x_new = tof.ping()

    # Compare measured data with set point (x_set)
    x_glatt = alpha * x_new + (1-alpha) * x_glatt
    e_new = float(x_set - x_glatt)
    e_int += e_new

    # Compute the new control signal (angle)
    u_new = kp * e_new + kd * (e_new - e_old) / dt + ki * dt * e_int
    u_glatt = beta * u_new + (1-beta)* u_glatt # Version mit u_glatt
    e_old = e_new

    # Apply the new beam angle
    # setAngle(u_new, servo) # Version ohne u_glatt
    setAngle(u_glatt, servo)
    
    # Wait a bit
    sleep(dt)
