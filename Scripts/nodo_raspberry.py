#!/usr/bin/env python
#Las librerias que se importan
import rospy
import RPi.GPIO as GPIO
from sensor_msgs.msg import Image as msg_Image
from std_msgs.msg import Int32

h = 10 #Hertz

def callbackPrueba(msg):
    print("Recibiendo: {}.".format(msg.data))
    pass

def main():
    rospy.init_node('nodo_raspberry', anonymous=True)
    rospy.Subscriber('topico_prueba', Int32, callbackPrueba)
    rate = rospy.Rate(h)

    while not rospy.is_shutdown():

        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
