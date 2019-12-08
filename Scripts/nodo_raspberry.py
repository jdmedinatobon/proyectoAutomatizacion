#!/usr/bin/env python
#Las librerias que se importan
import rospy
import RPi.GPIO as GPIO
from sensor_msgs.msg import Image as msg_Image
from std_msgs.msg import Int32
from proyectoAutomatizacion.srv import DireccionBanda

h = 10 #Hertz
funcionando = False

pinStart = 37

def callbackPrueba(msg):
    print("Recibiendo: {}.".format(msg.data))
    pass

def main():
    rospy.init_node('nodo_raspberry', anonymous=True)
    rate = rospy.Rate(h)

    #servicio = rospy.ServiceProxy('servicio_camara', DireccionBanda, persistent = True)

    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(pinStart, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

    while not rospy.is_shutdown():
        #res = servicio()

        #print(res)

        if GPIO.input(pinStart):
            print("START HIGH")
        else:
            print("START LOW")

        rospy.sleep(1)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
