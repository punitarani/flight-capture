# 2-axis pan-tilt gimbal driver

from time import sleep

from gpiozero import Servo

from defs import PAN_SERVO, TILT_SERVO


class Gimbal:
    def __init__(self):
        # RPi GPIO Pins
        self._pan_servo_pin = PAN_SERVO
        self._tilt_servo_pin = TILT_SERVO

        # MG996R Servo params
        myCorrection = 0.45
        maxPW = (2.0 + myCorrection) / 1000
        minPW = (1.0 - myCorrection) / 1000

        # Servo objects
        self.PanServo = Servo(self._pan_servo_pin,
                              min_pulse_width=minPW,
                              max_pulse_width=maxPW)

        self.TiltServo = Servo(self._tilt_servo_pin,
                               min_pulse_width=minPW,
                               max_pulse_width=maxPW)

    def test(self):
        servo = self.PanServo

        while True:
            servo.mid()
            print("mid")
            sleep(0.5)
            servo.min()
            print("min")
            sleep(1)
            servo.mid()
            print("mid")
            sleep(0.5)
            servo.max()
            print("max")
            sleep(1)


if __name__ == "__main__":
    Gimbal().test()
