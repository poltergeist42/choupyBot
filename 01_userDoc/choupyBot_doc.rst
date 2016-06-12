=========
choupyBot
=========

   :Autheur:            `Poltergeist42 <https://github.com/poltergeist42>`_
   :Projet:             choupyBot
   :Licence:            CC BY-NC-SA 4.0
   :Liens:              https://creativecommons.org/licenses/by-nc-sa/4.0/ 

------------------------------------------------------------------------------------------

    :Version:           20160612

------------------------------------------------------------------------------------------

Description
===========

ChoupyBot est un petit "robot" animé par un Raspberry pi et motoriser par 2 moteur pas à pas (PAP).
Un capteur ultrason ainsi qu'un ensemble de capteur infrarouge complète son équipement de base.

L'object de ce projet et de réalisé une petite plateform ludique qui pourra être programmer à distance
par un enfant. Ce robot evoluera dans un cadrillage de 10x10.

**N.B :** la dimension des cases sera determié ultérieurement en fonction de la taille du robot.

------------------------------------------------------------------------------------------

Descriptif détaillé
===================

    #. Liste des équipements
        * Un capteur ultrason
            Il vat permetre la détection des obstables. Un potentiomettre sera associé
            à ce capteur pour permettre de modifier la distance de sécurité avant
            évitement des obstacles.
            
        * Un Servo moteur
            pour manipuller le capteur ultrason (Pas obligatoire).
            
        * Des emeteurs recepteurs infrarouge
            Ils vont permettre de detecter les bords de table pour prévenir des chutes.
            Ils devront également être capable de suivre une ligne tracé au sols.
            Pour aider la programation et le degugage, des LED CMS seront placées
            à coté de chaque capteur.
            
        * Un bouton "Start"
            Lorsque la programation du robot par l'utilisateur sera terminé,
            le robot attendra que le bouton "Start" soit enfoncé avant de commencer.
            Des LED peuvent être placés à coté pour indiquer si on est en mode Action
            ou Programmation
            
            **N.B** : Si le bouton n'est pas physique mais fait parti de l'interface,
            il ne sera pas necessaire d'ajouter les LED.
            
    #. Liste des fonctionalités
        * Suiveur de lignes
            - Il doit pouvoir suivre une ligne noir d'une épaisseur de 25 mm minimum.
            - En cas d'obstacle sur le parcour il doit pouvoir se détourner de son chemin
              et pouvoir le récupérer plus loin
        
        * Se déplacer sur un dammier
            - Il doit être capable de se déplacer très précésement
              à fin de ne pas dépasser les limites d'une case
            - on peut imaginé que le robot devrat positionner un objet sur une case précise
              en contournant les obstacles posé sur le plateau.
              
    #. Besoin et fonctionnalités pour la "programation" coté publique
        * Création d'un programe et d'un interface pour tablettes Android
            - 4 boutons de base : Avance, Recul, Gauche, Droite

------------------------------------------------------------------------------------------

Références materiels
====================

    :reference du moteur Pas a Pas:         28BJY-48
    :reference du driver pour le PAP:       UNL2003
    :reference du capteur ultrason:         HC-SR04
