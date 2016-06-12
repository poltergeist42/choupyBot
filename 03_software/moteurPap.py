#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   :Nom du fichier:     moteurPap.py
   :Autheur:            `Poltergeist42 <https://github.com/poltergeist42>`_
   :Version:            20160612

----

   :Licence:            CC-BY-NC-SA
   :Liens:              https://creativecommons.org/licenses/by-nc-sa/4.0/

----

lexique
-------

   :v_:                 variable
   :l_:                 list
   :t_:                 tuple
   :d_:                 dictionnaire
   :f_:                 fonction
   :C_:                 Class
   :i_:                 Instance
   :m_:                 Module
"""
#################### Taille maximum des commentaires (80 caracteres)######################


"""
    #####  moteur pap ####

    Ce module permet de creer et de manipuler l'objet 'C_MoteurPap'
    
     Une valeur positive fait
    touner le moteur dans le sens horraire. Une valeur négative fait tourner le moteur
    dans le sens anti-horraire (si on ne s'est pas trompé dans le cablage)

    N.B : se PAP doit etre pilote par un driver comme le UNL2003

        *** Specification ***
            - reference du moteur Pas a Pas         : 28BJY-48
            - angle par pas (moteur)                : 5.625°
            - Nbe de pas / tours (moteur)           : 64 (360/5.625)
            - ratio (demultiplicateur)              : 1/64
            - angle par pas (en sortie d'abre)      : 0.087890625°
            - Nbe de pas / tour (en sortie d'arbre) : 4096 

       *** Correspodanse entre le driver UNL2003 et les GPIO ***
       
           - BCM (GPIO) -   | - Serigraphie sur UNL2003 -
               v_gpioA      |               N1
               v_gpioB      |               N2
               v_gpioC      |               N3
               v_gpioD      |               N4

        *** t_phases ***
                                |  --> CW Direction (1-2 phase )
            - lead Wire color - |- 1 -|- 2 -|- 3 -|- 4 -|- 5 -|- 6 -|- 7 -|- 8 -
                4 orange        |  x  |  x  |     |     |     |     |     |  x
                3 yelow         |     |  x  |  x  |  x  |     |     |     |
                2 pink          |     |     |     |  x  |  x  |  x  |     |
                1 blue          |     |     |     |     |     |  x  |  x  |  x
               
            N.B : les 8 phases donnent 1 tour complet sur le moteur,
                soit 1/64 de tour en sortie d'arbre.
"""

import RPi.GPIO as GPIO
import time

from math import pi


class C_MoteurPap(object):
    """ Class permettant d'instancier un objet 'C_MoteurPap' """
    
    def __init__(self, v_rotationInit = "horaire", v_rayonInit = 1) :
        """
            Déclaration et intialisation des variables
        """
        # declaration des variables
        self.v_rotation = v_rotationInit.lower()
        self.v_dest = 1
        self.v_compteurDePas = 0
        self.v_tempDePause = 0.005
        self.v_nbPas = 0
        self.v_angle = 0
        self.v_refAngle = 0.087890625
        
        self.t_broches = [0, 0, 0, 0]
        
        self.v_rayon = v_rayonInit
        self.v_perimetre = 2 * pi * self.v_rayon

        # Séquense de sortie
        self.v_ndp = 8
        self.t_phase = list(range(self.v_ndp))
        self.t_phase[0] = [1,0,0,0]
        self.t_phase[1] = [1,1,0,0]
        self.t_phase[2] = [0,1,0,0]
        self.t_phase[3] = [0,1,1,0]
        self.t_phase[4] = [0,0,1,0]
        self.t_phase[5] = [0,0,1,1]
        self.t_phase[6] = [0,0,0,1]
        self.t_phase[7] = [1,0,0,1]
        
    def f_gpioInit(self, v_gpioA=17, v_gpioB=18, v_gpioC=27, v_gpioD=22):
        """
            Methode permettant de selectionner et d'activer les 4 ports du RPi
            necessaires au fonctionnement du moteur Pas a Pas.
            par défaut, les ports sont configures de la facon suivante :
                v_gpioA = GPIO17
                v_gpioB = GPIO18
                v_gpioC = GPIO27
                v_gpioD = GPIO22
                
            Ces ports doivent etre change si il y a plus d'un moteur sur le montage
            
            Cette methode est obligatoire est doit etre appellee lors de la creation
            de chaque nouvelle instance de l'objet.
        """
        # configuration du mode du GPIO
        GPIO.setmode(GPIO.BCM)

        # Déclaration des broches : GPIO17, GPIO18, GPIO27, GPIO22
        self.t_broches = [v_gpioA, v_gpioB, v_gpioC, v_gpioD]

        # Configuration des broches en sortie et initialisation à l'état bas
        for v_sortieInit in self.t_broches :
            GPIO.setup(v_sortieInit, GPIO.OUT)
            GPIO.output(v_sortieInit, False)

    def f_gpioDestructor(self):
        """
            Methode permettant de fermer proprement la gestion des GPIO du Rpi
            
            Cette methode doit etre appellee a la fin de l'utilisation
            des broches GPIO (avant de quiter le programe).
        """

        GPIO.cleanup()

    def f_moveDeg(self, v_deg):
        """
            Methode permettant d'effectuer une rotation egale 
            a la valeur fournie degres
        """
        # Récupération d'une valeur donnée en degrès puis convertion
        # de cette valeur en nombre de pas en sortie d'arbre
        self.v_dest = self.f_convertDegToStep( v_deg )
        # print("dbgMsg[01]: self.v_dest [ + ] : ", self.v_dest)
        self.f_move(self.v_dest, v_deg)

    def f_moveStep(self, v_step):
        """
            Methode permettant d'effectuer une rotation egale
            a la valeur fournie nombre de pas (en sortie d'arbre)
        """
        # Recuperation d'une valeur donnee en nombre de pas en sortie d'arbre
        self.v_dest =  v_step
        # print("dbgMsg[04]: self.v_dest [ + ] : ", self.v_dest)
        self.f_move(self.v_dest, v_step)

    def f_moveCm(self, v_cm) :
        """ effectue une rotation egale a une distance en centimetre """
        self.v_dest = self.f_convertCmToStep(v_cm)
        self.f_move(self.v_dest, v_cm)
                       
    def f_move(self, self.v_dest, v_step) :
        """ Factorisation de la sequence de mouvement des PAP """
        
        if self.v_dest > 0 :
            self.v_dest+= 1
            v_step = 1
        else :
            self.v_dest -=1
            v_step = -1
        # print("dbgMsg[04']: self.v_dest [ - ] : ", self.v_dest)
        
        for v_pas in range(0, self.v_dest, v_step):
                # print("dbgMsg[05]: v_pas : ", v_pas)
                for v_sortie in range(4):
                    v_sortieN = self.t_broches[v_sortie]
                    if self.t_phase[self.v_compteurDePas][v_sortie] !=0 :
                        # print("dbgMsg[06]: t_phase %i Activation v_sortie %i" %(self.v_compteurDePas, v_sortieN))
                        GPIO.output(v_sortieN, True)
                    else :
                        GPIO.output(v_sortieN, False)
                if v_step == 1 : self.v_compteurDePas -= 1
                elif v_step == -1 : self.v_compteurDePas +=1
            
                if (self.v_compteurDePas == self.v_ndp) : self.v_compteurDePas = 0
                if (self.v_compteurDePas < 0) : self.v_compteurDePas = self.v_ndp-1       
                
    def f_convertDegToStep(self, v_degToStep):
        """
            Methode permettant de convertir en nombre de Pas
            une valeur entree en degres
        """
        return int( v_degToStep //self.v_refAngle)
        
    def f_convertStepToDeg(self, v_stepToDeg):
        """
            Methode permettant de convertir en degres
            une valeur entree nombre de Pas
        """
        return v_stepToDeg * self.v_refAngle
        
    def f_convertCmToDeg(self, v_cmToDeg) :
        """
            Methode permettant de convertir en centimetre
            une valeur donnee en degres
            
            :Rappel:
                Calcul du perimetre d'un cercle
                    ::
                    
                        2 x pi x R
                
                +-----------------+------------------+
                |     Degres      |   centimetres    |
                +=================+==================+
                |      360        |      2piR        |
                +-----------------+------------------+
                |     360/(2piR)  |        1         |
                +-----------------+------------------+
                | (x360) / (2piR) |        x         |
                +-----------------+------------------+
                |        1        | (2piR) / (x360)  |
                +-----------------+------------------+
                |        x        | (x2piR) / (x360) |
                +-----------------+------------------+
        """
        return (v_cmToDeg * 360) / self.v_perimetre
        
    def f_convertDegToCm(self, v_degToCm) :
        """
            Methode permettant de convertir en degres
            une valeur donnee en centimetre
            
            :Rappel:
                Calcul du perimetre d'un cercle
                    ::
                    
                        2 x pi x R
                
                +-----------------+------------------+
                |     Degres      |   centimetres    |
                +=================+==================+
                |      360        |      2piR        |
                +-----------------+------------------+
                |     360/(2piR)  |        1         |
                +-----------------+------------------+
                | (x360) / (2piR) |        x         |
                +-----------------+------------------+
                |        1        | (2piR) / (x360)  |
                +-----------------+------------------+
                |        x        | (x2piR) / (x360) |
                +-----------------+------------------+
        """
        return (v_degToCm * self.v_perimetre) / 360)
    
    def f_convertCmToStep(self, v_cmToStep) :
        """ convertit une valeur en centimetre
            en l'equivalent en nombres de pas
        """
        return (4096 * v_cmToStep) / self.perimetre
        
    def f_convertStepToCm(self, v_stepToCm) :
        """ convertit un nombre de pas en une distance en centimetre """
        return (v_stepToCm * self.perimetre) / 4096
        
       
    def f_sensDeRotation(self) :
        """
            identifi le sens de rotation attendu par l'utilisateur
            et l'affecter au PAP
        """
        if self.v_rotation == antihorraire :
            self.v_dest *= -1
