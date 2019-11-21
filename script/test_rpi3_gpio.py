#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import rospy

class GpioCtrl:
    def __init__(self, pinNo):
        self.pinNo = pinNo
        rospy.init_node('rpi3_gpio_ctrl')
        # Initialize GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pinNo, GPIO.OUT)

    def gpio_on(self):
        rospy.loginfo('GPIO' + str(self.pinNo) + ' ON')
        GPIO.output(self.pinNo, True)


    def gpio_pwm_on(self, duty):
        rospy.loginfo('GPIO' + str(self.pinNo) + ' PWM Duty ' + str(duty) + '[%] ON')
        while not rospy.is_shutdown():
            GPIO.output(self.pinNo, True)
            time.sleep(duty/10000.0)
            GPIO.output(self.pinNo, False)
            time.sleep(0.01 - (duty/10000.0))

    def gpio_off(self):
        rospy.loginfo('GPIO' + str(self.pinNo) + ' OFF')
        GPIO.output(self.pinNo, False)

    def gpio_cleanup(self):
        GPIO.cleanup()
        rospy.loginfo('GPIO cleanup done')

if __name__ == '__main__':
    gpioCtrl = GpioCtrl(26)
    gpioCtrl.gpio_pwm_on(10)
    gpioCtrl.gpio_off()
    gpioCtrl.gpio_cleanup()


    #gpioCtrl.gpio_on()
    #time.sleep(5)
    #gpioCtrl.gpio_off()
    #gpioCtrl.gpio_cleanup()
