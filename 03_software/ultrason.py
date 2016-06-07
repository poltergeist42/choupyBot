#!/usr/bin/env python
# -*- coding: utf-8 -*-

###
#   Nom du fichier  : ultrason.py
#   Autheur         : Poltergeist42
#   Version         : 2016.05.28
###

###
#   Licence         : CC-BY-NC-SA
#   Liens           : https://creativecommons.org/licenses/by-nc-sa/4.0/
###

###
#   [ lexique ]
#
#   v_              : variable
#   l_              : list
#   t_              : tuple
#   d_              : dictionnaire
#   f_              : fonction
#   C_              : Class
#   i_              : Instance
#   m_              : Module
###

#################### Taille maximum des commentaires (80 caracteres)######################

import RPi.GPIO as GPIO
import time

class C_ultrasonSensor(object) :
    """ Class permettant d'utiliser le capteur ultra son 
    
    - Type de capteur           : HC-SR04
    - Trig                      : En Sortie (hautparleur)
                                        # 1 impulsion est egale a 10us (0.00001)
    - Echo                      : En Entree (Micro)
                                        # Attention les entrée du RPi etant en 3.3v,il
                                        # faut faire un pont diviseur entre la broche
                                        # "Echo" et le GND pour pouvoir se brancher
                                        # sur le RPi
                                        
    - Distance                  : D = 170 x time
                                        # 170 correspond a la vitesse du son / 2 (340/2)
    - source : https://www.youtube.com/watch?v=xACy8l3LsXI
    """
    def init(self) :
        """ variables globales """
        self.v_trig = 0
        self.v_echo = 0
        
    def ultraInit(self, v_gpioTrig = 7, v_gpioEcho = 12) :
        """ initialisation des broches GPIO en entree (Echo) et en sortie (Trig) """
        GPIO.setmode(GPIO.BCM)
        self.v_trig = v_gpioTrig
        self.v_echo = v_gpioEcho
        
        GPIO.setup(self.v_echo, GPIO.IN)
        GPIO.setup(self.v_trig, GPIO.OUT)
        
    def ultraMesure(self) :
        """ mersure de la distance entre le capteur et l'obstacle """
        time.sleep(0.1)
        
        