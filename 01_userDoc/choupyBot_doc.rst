=========
choupyBot
=========

   :Autheur:            `Poltergeist42 <https://github.com/poltergeist42>`_
   :Projet:             choupyBot
   :Licence:            CC BY-NC-SA 4.0
   :Liens:              https://creativecommons.org/licenses/by-nc-sa/4.0/ 

------------------------------------------------------------------------------------------

    :Version:           20160611

------------------------------------------------------------------------------------------

Description
===========

ChoupyBot est un petit "robot" animé par un Raspberry pi et motoriser par 2 moteur pas à pas (PAP).
Un capteur ultrason ainsi qu'un ensemble de capteur infrarouge complète son équipement de base.

L'object de ce projet et de réalisé une petite plateform ludique qui pourra être programmer à distance
par un enfant. Ce robot evoluera dans un cadrillage de 10x10.

**N.B :** la dimension des case sera determié ultérieurement en fonction de la taille du robot.

------------------------------------------------------------------------------------------

Descriptif détaillé
===================

    #. Liste des équipements
        * Un capteur ultrason
            # Il vat permetre la détection des obstables. Un potentiomettre sera associé
            à ce capteur pour permettre de modifier la distance de sécurité avant
            évitement des obstacles.
        * Des emeteurs recepteurs infrarouge
            # Ils vont permettre de detecter les bords de table pour prévenir des chutes.
            Ils devront également être capable de suivre une ligne tracé au sols.

------------------------------------------------------------------------------------------

Références materiels
====================

    :reference du moteur Pas a Pas:         28BJY-48
    :reference du driver pour le PAP:       UNL2003
    :reference du capteur ultrason:         HC-SR04