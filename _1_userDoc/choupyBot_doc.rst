=========
choupyBot
=========

   :Autheur:                    `Poltergeist42 <https://github.com/poltergeist42>`_
   :Organistation:              `VoLAB <https://github.com/volab>`_
   :Projet:                     `choupyBot <https://github.com/volab/choupyBot>`_
   :Licence:                    CC BY-NC-SA 4.0
   :Liens:                      https://creativecommons.org/licenses/by-nc-sa/4.0/ 

------------------------------------------------------------------------------------------

    :Version:                   20160720

------------------------------------------------------------------------------------------

Outils de conception
=======================

    :Langage de programmation:  Python (v3.4)
    :modelisation 3D:           Fusion 360
    :Circuit imprime:           Kicad (v4.0.2)

------------------------------------------------------------------------------------------

Description
===========

ChoupyBot est un petit "robot" anim� par un Raspberry pi et motoriser par 2 moteurs
pas � pas (PAP) et un capteur ultrason.

L'objectif de ce projet et de r�aliser une petite plateforme ludique qui pourra �tre
programm�e / command�e � distance par un enfant. Ce robot �voluera dans un quadrillage
de 15x15.

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
            
            *N.B :* Le potentiom�tre n'�tant pas indispen�able, il peut �tre homis.
            
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
        * Cr�ation d'un programme et d'un interface pour tablettes Android et / ou PC
            - 4 boutons de base : Avance, Recul, Gauche, Droite
            - 1 menu d�roulant permettant de choisir le mode disponible : Boxxle, Parcours,
              Aventure.
            - 1 paire de bouton radio Start / Stop

------------------------------------------------------------------------------------------

R�f�rences mat�riels
====================

    :reference du moteur Pas a Pas:         28BJY-48
    :reference du driver pour le PAP:       UNL2003
    :reference du capteur ultrason:         HC-SR04
    :reference du Raspberry Pi:             Raspberry Pi2
    :reference Battery:                     Lipo Battery 7.4V
    :reference abaisseur de tension:        UBEC 5v 3a
    :reference electronique:
        +------------------------------------------------------------------------------+
        |                           Carte �l�ctronique                                 |
        +--------------------------+-----+---------------------------------------------+
        |          R�f�rence       | QTE |                 Descriptif                  |
        +==========================+=====+=============================================+
        | Resistor 20K             |  1  | pond diviseur pour abesser la tension en    |
        +--------------------------+-----+ sortie de la broche 'echo' (+5v) jusqu'� la |
        | Resistor 10k             |  1  | tension d'entr�e des GPIO du RPi            |
        +--------------------------+-----+---------------------------------------------+
        | Resistor 330R            |  1  | Control de reception, par 'echo', du son    |
        +--------------------------+-----+ �mit par 'trig'. Cette ensemble est         |
        | Red LED 5mm              |  1  | facultatif                                  |
        +--------------------------+-----+---------------------------------------------+
        | Pin_Header_Straight_1x02 |  2  | P1, entr�e Ubec. P10 N.U, en cas de besoin  |
        +--------------------------+-----+---------------------------------------------+
        | Pin_Header_Straight_1x03 |  1  | Broches I2c du Pi, en cas de besoin         |
        +--------------------------+-----+---------------------------------------------+
        | Pin_Header_Straight_2x20 |  1  | Pour relier le PCB au Pi                    |
        +--------------------------+-----+---------------------------------------------+
        | XH_connector_4pins_Vert  |  3  | Pour le sonar et les 2 drivers de PAP       |
        +--------------------------+-----+---------------------------------------------+
        | XH_connector_2pins_Vert  |  4  | Pour alimenter les dif�rents elements       |
        +--------------------------+-----+---------------------------------------------+
        | 40 Pin Flat grey Ribbon  |  1  | Nape permettant de relier le RPi � la carte |
        | Cable                    |     | du robot                                    |
        +--------------------------+-----+---------------------------------------------+
        | 40 Pin IDC FC Female     |     | Connecteur � placer sur chaque extremit�    |
        | Header Cable Socket      |  2  | de la nape une fois coup�e aux bonnes       |
        | Connector FC-40          |     | dimensions                                  |
        +--------------------------+-----+---------------------------------------------+
        
        +------------------------------------------------------------------------------+
        |                           Autres Composant                                   |
        +--------------------------+-----+---------------------------------------------+
        |          R�f�rence       | QTE |                 Descriptif                  |
        +==========================+=====+=============================================+
        | Mini Digital Voltmeter   |  1  | Permet de mesurer la tension de la battery  |
        +--------------------------+-----+---------------------------------------------+
        | spdt toggle switch 2     |  1  | Switch Permettant la mise sous tension et   |
        | position                 |     | la mise hors tension                        |
        +--------------------------+-----+---------------------------------------------+
        
    :ref fournisseur:
        * `Resistor <http://www.aliexpress.com/item/1Pack-300Pcs-10-1M-Ohm-1-4w-Resistance-1-Metal-Film-Resistor-Resistance-Assortment-Kit-Set/32505894332.html?spm=2114.30010308.3.1.85eorw&ws_ab_test=searchweb201556_0,searchweb201602_3_10057_10056_10055_10037_10049_10033_10059_10032_10058_10017_405_404_407_10040,searchweb201603_1&btsid=8e5d318c-a269-4c5b-a395-16bc8a31fc73>`_
        
        * `Red LED 5mm <http://www.aliexpress.com/item/Free-shipping-100pcs-Red-LED-5MM-Red-light-emitting-diode-Red-turn-Red/32628839823.html?spm=2114.30010308.3.1.01SFzv&ws_ab_test=searchweb201556_0,searchweb201602_3_10057_10056_10055_10037_10049_10033_10059_10032_10058_10017_405_404_407_10040,searchweb201603_1&btsid=47854a59-62f5-488d-87f2-74b3ebb1b718>`_

        * `Pin_Header_Straight(SIL) <http://www.aliexpress.com/item/20pcs-lot-Connector-2-54mm-40-Pin-Male-Single-Row-silver-Pin-Header-Strip-Free-Shipping/606254600.html?spm=2114.30010308.3.12.xWCI9f&ws_ab_test=searchweb201556_0,searchweb201602_3_10057_10056_10055_10037_10049_10033_10059_10032_10058_10017_405_404_407_10040,searchweb201603_1&btsid=45858581-d831-43e6-adae-868ebc290c68>`_

        * `Pin_Header_Straight (DIL) <http://www.aliexpress.com/item/5PCS-LOT-2-54mm-2-x-40-Pin-Male-Double-Row-Pin-Header-Strip-pin-header/32639552444.html?spm=2114.30010308.3.172.xWCI9f&s=p&ws_ab_test=searchweb201556_0,searchweb201602_3_10057_10056_10055_10037_10049_10033_10059_10032_10058_10017_405_404_407_10040,searchweb201603_1&btsid=45858581-d831-43e6-adae-868ebc290c68>`_

        * `XH_connector <http://www.aliexpress.com/item/40-sets-Kit-in-box-2p-3p-4p-5-pin-2-54mm-Pitch-Terminal-Housing-Pin/32682649292.html?spm=2114.13010608.0.74.pS2urM>`_
 
        * `40 Pin Flat grey Ribbon Cable <http://www.aliexpress.com/item/1meter-free-shipping-40-Pin-1-27mm-Spacing-2-54mm-Pitch-Extension-Flat-grey-Ribbon-Cable/32695430026.html?spm=2114.13010608.0.66.tULEbf>`_
        
        * `40 Pin IDC FC Female Header Cable Socket Connector FC-40 <http://www.aliexpress.com/item/50-Pcs-2-54mm-2x20-Pin-40-Pin-IDC-FC-Female-Header-Cable-Socket-Connector-FC/32425419419.html?spm=2114.30010308.3.2.SSNuZS&ws_ab_test=searchweb201556_0,searchweb201602_3_10057_10056_10055_10037_10049_10033_10059_10032_10058_10017_405_404_407_10040,searchweb201603_1&btsid=aadd4877-4555-4aa3-bfb5-1c5a960b74ee>`_
        
        * `Step motor + Drivers <http://www.aliexpress.com/item/5V-4-Phase-Stepper-Step-Motor-Driver-Board-ULN2003-With-Drive-Test-Module-Machinery-Board-Tools/32532201168.html?spm=2114.30010308.3.1.wHrE7I&ws_ab_test=searchweb201556_0,searchweb201602_3_10057_10056_10055_10037_10049_10033_10059_10032_10058_10017_405_404_407_10040,searchweb201603_1&btsid=5e1b0c4c-c554-49cf-8065-2a162d1b7fc5>`_
        
        * `HC-SR04 Ultrasonic <http://www.aliexpress.com/item/5pcs-HC-SR04-Ultrasonic-Module-Distance-Measuring-Transducer-Sensor-Detector-Ranging-Module-DC-5V/1787674353.html?spm=2114.30010308.3.1.CF7FU0&ws_ab_test=searchweb201556_0,searchweb201602_3_10057_10056_10055_10037_10049_10033_10059_10032_10058_10017_405_404_407_10040,searchweb201603_1&btsid=fbf652a2-1388-4059-8230-f07c7a479e81>`_

        * `Raspberry Pi 3 (le 2 est �puis�) <http://www.rs-particuliers.com/WebCatalog/Raspberry_Pi_Model_3_B_SBC-8968660.aspx>`_
        
        * `Lipo Battery 7.4V <http://www.aliexpress.com/item/New-Lion-Power-Lipo-Battery-7-4V-2S-900Mah-25C-High-Power-For-RC-Helicopter-Quadcopter/32490119056.html?spm=2114.30010308.3.200.L5R1oe&ws_ab_test=searchweb201556_0,searchweb201602_3_10057_10056_10055_10037_10049_10033_10059_10032_10058_10017_405_404_407_10040,searchweb201603_1&btsid=5df62305-c0ef-4954-b372-49875b600234>`_
        
        * `UBEC <http://www.aliexpress.com/item/DC-Converter-Module-3A-5V-Mini-UBEC-For-RC-Plane-Quadcopter-UBEC-For-FPV-Image-Transmission/32672871968.html?spm=2114.30010308.3.126.czjaXj&ws_ab_test=searchweb201556_0,searchweb201602_3_10057_10056_10055_10037_10049_10033_10059_10032_10058_10017_405_404_407_10040,searchweb201603_1&btsid=782431b5-bf7c-4989-af00-d58d274b1460>`_
        
        * `Mini Digital Voltmeter <http://www.banggood.com/0_28-Inch-2_5V-30V-Mini-Digital-Voltmeter-p-974258.html>`_
        
        * `spdt toggle switch <http://www.aliexpress.com/item/2-Pcs-AC-125V-6A-Amps-ON-ON-2-Position-3-Pins-SPDT-Mini-Toggle-Switch/32616445190.html?spm=2114.30010308.3.292.Cuv17y&ws_ab_test=searchweb201556_0,searchweb201602_3_10057_10056_10055_10037_10049_10033_10059_10032_10058_10017_405_404_407_10040,searchweb201603_1&btsid=3ba9a450-a00f-4e04-ab23-c6719cd05a1d>`_
        