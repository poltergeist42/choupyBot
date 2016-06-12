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

ChoupyBot est un petit "robot" anim� par un Raspberry pi et motoriser par 2 moteur pas � pas (PAP).
Un capteur ultrason ainsi qu'un ensemble de capteur infrarouge compl�te son �quipement de base.

L'object de ce projet et de r�alis� une petite plateform ludique qui pourra �tre programmer � distance
par un enfant. Ce robot evoluera dans un cadrillage de 10x10.

**N.B :** la dimension des cases sera determi� ult�rieurement en fonction de la taille du robot.

------------------------------------------------------------------------------------------

Descriptif d�taill�
===================

    #. Liste des �quipements
        * Un capteur ultrason
            Il vat permetre la d�tection des obstables. Un potentiomettre sera associ�
            � ce capteur pour permettre de modifier la distance de s�curit� avant
            �vitement des obstacles.
            
        * Un Servo moteur
            pour manipuller le capteur ultrason (Pas obligatoire).
            
        * Des emeteurs recepteurs infrarouge
            Ils vont permettre de detecter les bords de table pour pr�venir des chutes.
            Ils devront �galement �tre capable de suivre une ligne trac� au sols.
            Pour aider la programation et le degugage, des LED CMS seront plac�es
            � cot� de chaque capteur.
            
        * Un bouton "Start"
            Lorsque la programation du robot par l'utilisateur sera termin�,
            le robot attendra que le bouton "Start" soit enfonc� avant de commencer.
            Des LED peuvent �tre plac�s � cot� pour indiquer si on est en mode Action
            ou Programmation
            
            **N.B** : Si le bouton n'est pas physique mais fait parti de l'interface,
            il ne sera pas necessaire d'ajouter les LED.
            
    #. Liste des fonctionalit�s
        * Suiveur de lignes
            - Il doit pouvoir suivre une ligne noir d'une �paisseur de 25 mm minimum.
            - En cas d'obstacle sur le parcour il doit pouvoir se d�tourner de son chemin
              et pouvoir le r�cup�rer plus loin
        
        * Se d�placer sur un dammier
            - Il doit �tre capable de se d�placer tr�s pr�c�sement
              � fin de ne pas d�passer les limites d'une case
            - on peut imagin� que le robot devrat positionner un objet sur une case pr�cise
              en contournant les obstacles pos� sur le plateau.
              
    #. Besoin et fonctionnalit�s pour la "programation" cot� publique
        * Cr�ation d'un programe et d'un interface pour tablettes Android
            - 4 boutons de base : Avance, Recul, Gauche, Droite

------------------------------------------------------------------------------------------

R�f�rences materiels
====================

    :reference du moteur Pas a Pas:         28BJY-48
    :reference du driver pour le PAP:       UNL2003
    :reference du capteur ultrason:         HC-SR04
