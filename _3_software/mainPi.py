#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   :Nom du fichier:     choupyBot.py
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

from moteurPap import moteurPap
from ultrason import ultrason
from devChk.devChk import C_DebugMsg

class C_choupyBot(object) :
    def __init__(self):
        """ variables globales """
        
    def __del__(self) :
        """destructor
        
            il faut utilise :
            ::
            
                del [nom_de_l'_instance]
        """
        v_className = self.__class__.__name__
        print("\n\t\tL'instance de la class {} est terminee".format(c_className))

        
    def f_papInit(self):
        """ initialisation des 2 moteur pas a pas """
        self.i_PapGauche = C_MoteurPap(v_rotationInit = "antihorraire", v_rayonInit = 3)
                                        # Le PAP Gauche doit tourner en sens inverse du droit 
                                        # pour que le robot puisse aller tout droit
        self.i_PapGauche.f_gpioInit(v_gpioA=06, v_gpioB=12, v_gpioC=13, v_gpioD=19)
                                        # Initialisation des GPIO de chacun des moteur.
                                        # i_PapGauche est initialiser avec les valeur par defaut
                                        # (v_gpioA=17, v_gpioB=18, v_gpioC=27, v_gpioD=22)
        
        self.i_PapDroit  = C_MoteurPap(v_rayonInit = 3)
        self.i_PapDroit.f_gpioInit()

                                        
    def avance(self) :
        """ avance tout droit """
        
    def recul(self) :
        """ reculler tout droit """
        
    def gauche(self) :
        """ tourner a gauche """
        
    def droite(self) :
        """ Tourner a droite """

def main() :
    """ Fonction principal """
    i_choupy = C_choupyBot()
    i_choupy.f_papInit()
    ultrason.f_ultraInit(v_gpioEcho = 5)
    
    
if __name__ == '__main__':
    main()