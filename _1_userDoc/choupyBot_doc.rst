=========
choupyBot
=========

   :Autheur:                    `Poltergeist42 <https://github.com/poltergeist42>`_
   :Projet:                     choupyBot
   :Licence:                    CC BY-NC-SA 4.0
   :Liens:                      https://creativecommons.org/licenses/by-nc-sa/4.0/ 

------------------------------------------------------------------------------------------

    :Version:                   20160715

------------------------------------------------------------------------------------------

Outils de conception
=======================

    :Langage de programmation:  Python (v3.4)
    :modelisation 3D:           Fusion 360
    :Circuit imprime:           Kicad (v4.0.2)

------------------------------------------------------------------------------------------

Description
===========

ChoupyBot est un petit "robot" anim� par un Raspberry pi et motoriser par 2 moteur
pas � pas (PAP) et un capteur ultrason.

L'objet de ce projet et de r�alis� une petite plateforme ludique qui pourra �tre
programm�e � distance par un enfant. Ce robot �voluera dans un quadrillage de 15x15.

**N.B :** la dimension des cases sera d�termin�e ult�rieurement en fonction
de la taille du robot.

------------------------------------------------------------------------------------------

Descriptif d�taill�
===================

    #. Liste des �quipements
        * Un capteur ultrason
            Il vat permettre la d�tection des obstacles. Un potentiom�tre sera associ�
            � ce capteur pour permettre de modifier la distance de s�curit� avant
            �vitement des obstacles.
            
        * Un bouton "Start"
            Lorsque la programmation du robot par l'utilisateur sera termin�,
            le robot attendra que le bouton "Start" soit enfonc� avant de commencer.
            Des LED peuvent �tre plac�s � cot� pour indiquer si on est en mode Action
            ou Programmation
            
            **N.B** : Si le bouton n'est pas physique mais fait partie de l'interface,
            il ne sera pas n�cessaire d'ajouter les LED.
            
    #. Les modes disponibles sont
    
        * **Boxxle** : Le robot doit manipuler une boite sur un damier a fin de la
          ranger sur un emplacement d�fini en �vitant les obstacles. Les
          Instructions seront donn�es par un op�rateur depuis un terminal externe.
          
        * **Parcours** : Le robot doit suivre un parcours (ou un labyrinthe).
          Lorsque le robot aura suivi le parcours ou r�solue le labyrinthe, le
          robot pourra refaire le trajet de fa�on optimis�.
          
        * **Aventure** : le robot �volue librement au sol et r�agi en fonction des
          obstacles qu'il rencontre.
            

        * Se d�placer sur un damier
            - Il doit �tre capable de se d�placer tr�s pr�cis�ment
              � fin de ne pas d�passer les limites d'une case
               
    #. Besoin et fonctionnalit�s pour la "programmation" cot� publique
        * Cr�ation d'un programme et d'un interface pour tablettes Android
            - 4 boutons de base : Avance, Recul, Gauche, Droite
            - 1 menu d�roulant permettant de choisir le mode disponible : Boxxle, Parcours,
              Aventure.
            - 1 pair de bouton radio Start / Stop

------------------------------------------------------------------------------------------

R�f�rences mat�riels
====================

    :reference du moteur Pas a Pas:         28BJY-48
    :reference du driver pour le PAP:       UNL2003
    :reference du capteur ultrason:         HC-SR04
