# proyectoAutomatizacion
1) Para correr el paquete
Para correr en el computador:
roslaunch proyectoAutomatizacion computador.launch

Para correr en la raspberry:
(Aun no se ha terminado)
rosrun proyectoAutomatizacion nodo_raspberry.py

2) Configuracion de las IPs
En el computador:
export ROS_MASTER_URI='la ip del master:11311'

En la raspberry:
export ROS_MASTER_URI='la ip del master:11311' (Cambiarlo en el ./bashrc)
editar en etc/hosts la relacion entre la ip del master y el nombre

