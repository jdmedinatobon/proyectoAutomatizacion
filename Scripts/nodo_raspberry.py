#!/usr/bin/env python
#Las librerias que se importan
import rospy
import RPi.GPIO as GPIO
from sensor_msgs.msg import Image as msg_Image
from std_msgs.msg import Int32
from proyectoAutomatizacion.srv import DireccionBanda

h = 10 #Hertz
funcionando = False

#Es el pin del boton de Start.
pinStart = 37

#Es el pin del boton de Stop
pinStop = 35

#Son los pines de cada LED.
pinLED1 =

def callbackPrueba(msg):
    print("Recibiendo: {}.".format(msg.data))
    pass

def main():
    rospy.init_node('nodo_raspberry', anonymous=True)
    rate = rospy.Rate(h)

    #servicio = rospy.ServiceProxy('servicio_camara', DireccionBanda, persistent = True)

    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(pinStart, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.setup(pinStop, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

    GPIO.setup(pinLED1, GPIO.OUT)
    GPIO.setup(pinLED2, GPIO.OUT)
    GPIO.setup(pinLED3, GPIO.OUT)


    GPIO.output(pinLED1, 1)

    while not rospy.is_shutdown():
        #res = servicio()

        #print(res)

        if GPIO.input(pinStart) and GPIO.input(pinStop):
            print("START HIGH, STOP HIGH")
        elif GPIO.input(pinStart):
            print("START HIGH, STOP LOW")
        elif GPIO.input(pinStop):
            print("START LOW, STOP HIGH")
        else:
            print("START LOW, STOP LOW")

        rospy.sleep(1)

    GPIO.output(pinLED1, 0)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
