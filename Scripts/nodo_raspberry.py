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
pinLED1 = 36
pinLED2 = 38
pinLED3 = 40

def callbackPrueba(msg):
    print("Recibiendo: {}.".format(msg.data))
    pass

def main():
    global funcionando
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

        if GPIO.input(pinStart):
            funcionando = True

        if GPIO.input(pinStop):
            funcionando = False

        if funcionando:
            GPIO.output(pinLED1, 1)
        else:
            GPIO.output(pinLED1, 0)

        rospy.sleep(1)

    GPIO.output(pinLED1, 0)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
