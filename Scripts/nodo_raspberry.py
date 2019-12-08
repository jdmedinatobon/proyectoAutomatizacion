#!/usr/bin/env python
#Las librerias que se importan
import rospy
import RPi.GPIO as GPIO
from sensor_msgs.msg import Image as msg_Image
from std_msgs.msg import Int32
from proyectoAutomatizacion.srv import DireccionBanda
import time

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

#Son los pines de los sensores de ultrasonido
pinUS1_echo = 11
pinUS1_trig = 12
pinUS2_echo = 13
pinUS2_trig = 15
pinUS3_echo = 16
pinUS3_trig = 18

def callbackPrueba(msg):
    print("Recibiendo: {}.".format(msg.data))
    pass

def calcularDistancia():
    #Por ahora solo el 1.
    GPIO.output(pinUS1_trig, 1)

    rospy.sleep(0.00001)
    GPIO.output(pinUS1_trig, 0)

    start = time.time()

    while ~GPIO.input(pinUS1_echo):
        start = time.time()

    while GPIO.input(pinUS1_echo):
        stop = time.time()

    #En cm
    distancia = ((stop - start)*34300.0)/2.0

    return distancia

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

    GPIO.setup(pinUS1_echo, GPIO.IN)
    GPIO.setup(pinUS2_echo, GPIO.IN)
    GPIO.setup(pinUS3_echo, GPIO.IN)

    GPIO.setup(pinUS1_trig, GPIO.OUT)
    GPIO.setup(pinUS2_trig, GPIO.OUT)
    GPIO.setup(pinUS3_trig, GPIO.OUT)

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

    GPIO.cleanup()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
