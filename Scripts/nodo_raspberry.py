#!/usr/bin/env python
#Las librerias que se importan
import rospy
#import RPi.GPIO as GPIO
from sensor_msgs.msg import Image as msg_Image
from std_msgs.msg import Int32
from proyectoAutomatizacion.srv import DireccionBanda

h = 10 #Hertz

def callbackPrueba(msg):
    print("Recibiendo: {}.".format(msg.data))
    pass

def main():
    rospy.init_node('nodo_raspberry', anonymous=True)
    #rospy.Subscriber('topico_prueba', Int32, callbackPrueba)
    rate = rospy.Rate(h)

    servicio = rospy.ServiceProxy('servicio_prueba', DireccionBanda, persistent = True)

    #while not rospy.is_shutdown():
    res = servicio()

    print(res)

    #   rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
