import RPi.GPIO as GPIO
import time
import logging
logging.basicConfig()

servo_pin = 25

# Set up the GPIO pin for the servo
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Create a PWM instance
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)

# Function to set the servo to a specific angle
def set_servo_angle(angle):
    duty_cycle = angle / 18 + 2
    print(f'The duty cycle is: {duty_cycle}')
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1)
#    logging.debug(duty_cycle)
    return duty_cycle

angles = [0, 180]
try:
    while True:
#        move_servo("forward")
#       move_servo("backward")
        for angle in angles:
            print(f'The angle is: {angle}')
            set_servo_angle(angle)
except KeyboardInterrupt:
    print("Exiting program")
    pwm.stop()
    GPIO.cleanup()

    # Function to move the servo back and forth
    #def move_servo(direction):
    #    if direction == "forward":
    ##        print("forward")
    #        # Set the servo to the maximum angle
#        set_servo_angle(10)
#    elif direction == "backward":
#        print("backward")
#        # Set the servo to the minimum angle
#        set_servo_angle(9)

# Continuously move the servo back and forth
#try:
#    while True:
#        move_servo("forward")
#        move_servo("backward")

# If the user presses Ctrl+C, clean up the GPIO pins
#except KeyboardInterrupt:
#    print("Exiting program")
#    pwm.stop()
#    GPIO.cleanup()

