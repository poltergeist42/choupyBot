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

import moteurPap
import ultrason

class C_choupyBot(object) :
    def __init__(self):
        """ variables globales """
        
    def f_papInit(self):
        """ initialisation des 2 moteur pas a pas """
        self.i_PapGauche = C_MoteurPap(antihorraire)     # Creation des 2 objet "moteur pas a pas"
        self.i_PapDroit  = C_MoteurPap()     # 
        self.i_PapGauche.f_gpioInit()
        self.i_PapDroit.f_gpioInit(v_gpioA=06, v_gpioB=12, v_gpioC=13, v_gpioD=19)
                                        # Initialisation des GPIO de chacun des moteur.
                                        # i_PapGauche est initialiser avec les valeur par defaut
                                        # (v_gpioA=17, v_gpioB=18, v_gpioC=27, v_gpioD=22)
        
                                        
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
    ultrason.ultraInit()
    
    
if __name__ == '__main__':
    main()
