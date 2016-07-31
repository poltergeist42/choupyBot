#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

=========
choupyBot
=========

   :Nom du fichier:     choupyBot.py
   :Autheur:            `Poltergeist42 <https://github.com/poltergeist42>`_
   :Version:            20160731

####

   :Licence:            CC-BY-NC-SA
   :Liens:              https://creativecommons.org/licenses/by-nc-sa/4.0/

####

    :dev language:      Python 3.4
    
####

lexique
=======

   :**v_**:                 variable
   :**l_**:                 list
   :**t_**:                 tuple
   :**d_**:                 dictionnaire
   :**f_**:                 fonction
   :**C_**:                 Class
   :**i_**:                 Instance
   :**m_**:                 Module
"""
try :
    from moteurPap.moteurPap import C_MoteurPap
except ImportError :
    print( "module 'moteurPap' non charge") 

try :
    from ultrason.ultrason import C_ultrasonSensor
except ImportError :
    print( "module 'ultrason' non charge")
    
try :
    from devChk.devChk import C_DebugMsg
except ImportError :
    print( "module 'devChk' non charge")
    
try :
    from objJson.objJson import C_ObjJson
except ImportError :
    print( "module 'objJson' non charge")

class C_choupyBot(object) :
    def __init__(self, ):
        """ variables globales """
        
        ## Creation de l'instance de C_DebugMsg
        self.i_dbg = C_DebugMsg()
        
        ## Variables globales
        self.v_case = 15
        self.v_mode = ""
        
        
        
    def __del__(self) :
        """ Destructor
        
            Permet de fremer proprement l'instance en cours.
            il faut utilise :
            ::
            
                del [nom_de_l'_instance]
                
            N.B : cette methode est appelee automatiquement par le ramasse miette si
            l'instance n'est plus solicitee.
        """
        v_className = self.__class__.__name__
        print("\n\t\tL'instance de la class {} est terminee".format(c_className))

        
    def f_setMode(self, v_mode = "boxxle") :
        """ identification / modification du mode de fonctionnement du robot
        
            Le Robot peut être parametrer pour fonctionner selon plusieur mode.
            
            **Les modes disponibles sont :**
            
                * Boxxle (mode par defaut)
                * Parcours
                * Aventure
        """
        if v_mode == "boxxle" or v_mode == "parcours" or v_mode == "aventure"
            self.v_mode = v_mode
        else : self.v_mode = "boxxle"
        
    def f_papInit(self):
        """ initialisation des 2 moteur pas a pas (pap)
        
            +------------+-------------------------+
            | BCM (GPIO) | Serigraphie sur UNL2003 |
            +============+=========================+
            |   v_gpioA  |           N1            |
            +------------+-------------------------+
            |   v_gpioB  |           N2            |
            +------------+-------------------------+
            |   v_gpioC  |           N3            |
            +------------+-------------------------+
            |   v_gpioD  |           N4            |
            +------------+-------------------------+
           
            le papGauche est intialiser sur les GPIO par defaut soit ::
           
                v_gpioA = GPIO17
                v_gpioB = GPIO18
                v_gpioC = GPIO27
                v_gpioD = GPIO22
           
            et tourne dans le sens anti-horriare.
            le papDroit est initialiser sur un autre jeux de GPIO ::
           
                v_gpioA = GPIO06
                v_gpioB = GPIO12
                v_gpioC = GPIO13
                v_gpioD = GPIO19
                
            et tourne dans le sens horriare. La valeur de v_rayonInit correspond
            au rayon des roues du robot. Les deux pap tournes en sens inverse l'un de 
            l'aure, pour que le robot puisse aller tout droit.
        """
       
        ## papGauche
        self.i_papGauche = C_MoteurPap(v_rotationInit = "antihorraire", v_rayonInit = 3)
        self.i_papGauche.f_gpioInit(v_gpioA=06, v_gpioB=12, v_gpioC=13, v_gpioD=19)
        
        ## papDroit
        self.i_PapDroit  = C_MoteurPap(v_rayonInit = 3)
        self.i_PapDroit.f_gpioInit()

                                        
    def f_sonarInit(self) :
        """ Initialisation du capteur ultrason

        La broche du trig et configuer sur GPIO 7 par défaut.
        La broche echo ayant le GPIO 12 par defaut, elle a ete reconfiguree
        sur GPIO 5
        """
        
        i_ultrason = C_ultrasonSensor()
        i_ultrason.f_ultraInit(v_gpioEcho = 5)
    
    def f_avance(self) :
        """ avance tout droit """
        
    def f_recul(self) :
        """ reculler tout droit """
        
    def f_gauche(self) :
        """ tourner a gauche """
        
    def f_droite(self) :
        """ Tourner a droite """

def main() :
    """ Fonction principal """
    i_choupy = C_choupyBot()
    i_choupy.f_papInit()
    i_choupy.f_sonarInit()

    
    
if __name__ == '__main__':
    main()
