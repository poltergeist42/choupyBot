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

ChoupyBot est un petit "robot" anim� par un Raspberry pi et motoriser par 2 moteur pas � pas (PAP).
Un capteur ultrason ainsi qu'un ensemble de capteur infrarouge compl�te son �quipement de base.

L'object de ce projet et de r�alis� une petite plateform ludique qui pourra �tre programmer � distance
par un enfant. Ce robot evoluera dans un cadrillage de 10x10.

**N.B :** la dimension des case sera determi� ult�rieurement en fonction de la taille du robot.

------------------------------------------------------------------------------------------

Descriptif d�taill�
===================

    #. Liste des �quipements
        * Un capteur ultrason
            # Il vat permetre la d�tection des obstables. Un potentiomettre sera associ�
            � ce capteur pour permettre de modifier la distance de s�curit� avant
            �vitement des obstacles.
        * Des emeteurs recepteurs infrarouge
            # Ils vont permettre de detecter les bords de table pour pr�venir des chutes.
            Ils devront �galement �tre capable de suivre une ligne trac� au sols.

------------------------------------------------------------------------------------------

R�f�rences materiels
====================

    :reference du moteur Pas a Pas:         28BJY-48
    :reference du driver pour le PAP:       UNL2003
    :reference du capteur ultrason:         HC-SR04