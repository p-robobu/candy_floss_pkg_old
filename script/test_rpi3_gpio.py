#!/usr/bin/env python
import rospy
from candy_floss.srv import *
import RPi.GPIO as GPIO
import time


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


    # time added
    def gpio_pwm_on(self, req):
        rospy.loginfo('GPIO' + str(self.pinNo) + ' PWM Duty ' + str(req.duty) + '[%] ON')
        loop = 0
        while (req.time/0.01) != loop:
            GPIO.output(self.pinNo, True)
            time.sleep(req.duty/10000.0)
            GPIO.output(self.pinNo, False)
            time.sleep(0.01 - (req.duty/10000.0))
            loop ++
        self.gpio_off()
        self.cleanup()

    def gpio_off(self):
        rospy.loginfo('GPIO' + str(self.pinNo) + ' OFF')
        GPIO.output(self.pinNo, False)

    def gpio_cleanup(self):
        GPIO.cleanup()
        rospy.loginfo('GPIO cleanup done')


    def motor_on_server(self):
        #rospy.init_node('motor_on_server')
        s = rospy.Service('motor_on_server', MotorOn, self.gpio_pwm_on)
        rospy.loginfo('Ready to motor_on_server')
        rospy.spin()



if __name__ == '__main__':
    gpioCtrl = GpioCtrl(26)
    gpioCtrl.motor_on_server()
    #gpioCtrl.gpio_pwm_on(10)
    #gpioCtrl.gpio_off()
    #gpioCtrl.gpio_cleanup()


    #gpioCtrl.gpio_on()
    #time.sleep(5)
    #gpioCtrl.gpio_off()
    #gpioCtrl.gpio_cleanup()
