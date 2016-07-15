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

ChoupyBot est un petit "robot" animé par un Raspberry pi et motoriser par 2 moteur
pas à pas (PAP) et un capteur ultrason.

L'objet de ce projet et de réalisé une petite plateforme ludique qui pourra être
programmée à distance par un enfant. Ce robot évoluera dans un quadrillage de 15x15.

**N.B :** la dimension des cases sera déterminée ultérieurement en fonction
de la taille du robot.

------------------------------------------------------------------------------------------

Descriptif détaillé
===================

    #. Liste des équipements
        * Un capteur ultrason
            Il vat permettre la détection des obstacles. Un potentiomètre sera associé
            à ce capteur pour permettre de modifier la distance de sécurité avant
            Évitement des obstacles.
            
        * Un bouton "Start"
            Lorsque la programmation du robot par l'utilisateur sera terminé,
            le robot attendra que le bouton "Start" soit enfoncé avant de commencer.
            Des LED peuvent être placés à coté pour indiquer si on est en mode Action
            ou Programmation
            
            **N.B** : Si le bouton n'est pas physique mais fait partie de l'interface,
            il ne sera pas nécessaire d'ajouter les LED.
            
    #. Les modes disponibles sont
    
        * **Boxxle** : Le robot doit manipuler une boite sur un damier a fin de la
          ranger sur un emplacement défini en évitant les obstacles. Les
          Instructions seront données par un opérateur depuis un terminal externe.
          
        * **Parcours** : Le robot doit suivre un parcours (ou un labyrinthe).
          Lorsque le robot aura suivi le parcours ou résolue le labyrinthe, le
          robot pourra refaire le trajet de façon optimisé.
          
        * **Aventure** : le robot évolue librement au sol et réagi en fonction des
          obstacles qu'il rencontre.
            

        * Se déplacer sur un damier
            - Il doit être capable de se déplacer très précisément
              à fin de ne pas dépasser les limites d'une case
               
    #. Besoin et fonctionnalités pour la "programmation" coté publique
        * Création d'un programme et d'un interface pour tablettes Android
            - 4 boutons de base : Avance, Recul, Gauche, Droite
            - 1 menu déroulant permettant de choisir le mode disponible : Boxxle, Parcours,
              Aventure.
            - 1 pair de bouton radio Start / Stop

------------------------------------------------------------------------------------------

Références matériels
====================

    :reference du moteur Pas a Pas:         28BJY-48
    :reference du driver pour le PAP:       UNL2003
    :reference du capteur ultrason:         HC-SR04
