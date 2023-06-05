*SLAPBOT*:
SlapBot és un robot capaç de jugar a cartes, concretament al joc ("El Tapete"). El robot és composa en 4 parts, un mecanisme que carrega el "slap" del robot, un llença cartes, una càmera que fa d'"ulls" del robot i uns sensors que detecten qui ha guanyat la ronda.
Per poder detectar quines cartes s'han tirat fem ús d'una API de Roboflow com figura a la carpeta de src/raspberry_pi que processa el que veu la càmera, li passa a l'algorisme el resultat i per tant es genera una acció.

(Prèviament el reconeixement de les cartes s'havia de fer utilitzant la xarxa neuronal que figura a src/neural_network però com està explicat al explicacio.md de la corresponent carpeta no s'ha utilitzat finalment)

Software:
- Python 3 (con raspberry pi 4)
- C++ (con arduino)

API:
- Un projecte de roboflow per a detecció de cartes (detallat a src/raspberry_pi4/execute_program_and_cite_project_api_roboflow)

Hardware:
- Raspberry Pi 4
- Càmera eye playstation 3
- Arduino Nano
- Sensor Ultrasons hc-sr04 x2
- Motor DC 
- Altaveu
- Mini Motor DC
- Font alimentació (porta piles de 6. De 7,2V a 9V )
- Controladora TB6612FNG (pels motors)
- 
![Image text](https://github.com/1606206/SlapBot_RLP/blob/main/Hardware/esquema_hardware_slapbot.png)


Src:
-Arduino:
        Amb l'arduino (codi en c++) controlem els sensors i els motors (juntament amb la controladora) per detectar el moviment i controlar els moviments dels motors quan calgui.
        En el cas dels sensors detecten qui pica a la taula abans, ja sigui quan hi ha una combinació o quan algun jugador pica a la taula sense que el robot hagi detectat una combinació; ja que també hi ha la probabilitat que l'API utiltizada per reconèixer les cartes falli i no detecti una possible combinació. Quan els sensors detecten que o el robot o un jugador ha picat a la taula l'arduino envia la senyal a la raspberry pi 4 per a que ho sàpiga.

-Neural_Network:
        Hem creat una xarxa neuronal entrenant un model el qual a partir d'una imatge de cadascuna de les cartes a sobre del taulell s'entrenava. Al entrenar la xarxa neuronal ens donava un molt bon accuracy tant de train com de test (els dos superiors a 0,9) com es pot veure al fitxer .ipynb però el testejar-ho jugant amb el robot no obteniem els resultats esperats. Finalment s'ha decidit fer ús d'un projecte de Roboflow de detecció de cartes però, així i tot a la carpeta corresponent s'hi pot trobar el codi emprat per entrenar la xarxa, el model obtingut, la funció amb la qual a partir del model obteniem la predicció de la carta i un exemple de com el cridariem des del programa.

-Raspberry_pi4:
        Hem implementat el codi necessàri per l'execució normal del programa, i també la comunicació amb l'arduino, la càmera i l'API per a detecció de cartes. Al corresponent .md de la carpeta src/raspberry_pi4 està explicat com executar el programa.
        
El programa principal es basa en el següent:

![Image text](https://github.com/1606206/SlapBot_RLP/blob/main/src/diagrama_software.jpg)

Per passar torn es passa sempre el tirar una sola carta sempre i quan el jugador anterior no hagi tirat una de les cartes especials (J, Q, K, A). Si es dona el cas que el jugador anterior ha tirat una de les cartes especials, J, Q, K o A, caldrà que el jugador actual tiri una, dues, tres o quatre cartes respectivaments fins que alguna d'aquestes també sigui una carta especial i salvar-se. Si una d'aquest numero limitat de cartes que pot tirar "per salvar-se" és una carta especial llavors li passa "la patata calenta" al següent jugador. Si per contra el jugador tira el numero de cartes que pot tirar per salvar-se però no ho aconsegueix, llavors guanya el jugador anterior les cartes i torna a començar les rondes


Com Jugar:
- La partida i la ronda la comença SEMPRE el robot (es una forma de "timejar" tot)
- Quan és el torn del robot, tira una carta utilitzant el motor DC del llença-cartes. En cas que hagi de tirar més d'una carta seguida, ho farà un cop detecti la última carta tirada. En cas que sigui el torn d'algun dels jugadors, anirà detectant totes les cartes que tirin, fins que li toqui tirar de nou al robot. Seguint les normes del Tapete, el robot haurà de donar un cop a la taula quan hi hagi 2 cartes seguides amb el mateix número, o un "sandwich"(dos cartes iguals separades per una diferent), i ho farà amb l'altre motor DC que utilitzem pel braç. Tanmateix, el/s jugador/s hauran de picar entre l'altre sensor i la pila de cartes perquè així el robot pugui detectar si ha guanyat ell o els altres jugadors. Un cop algun dels jugadors (o el robot) s'emporti les cartes, ja sigui perquè ha picat primer, o perquè se les emporta jugant, el robot farà una pausa de 20 segons per donar temps que es reiniciï la ronda.
- Al finalitzar una de las rondes el jugador en cas de que el robot hagi guanyat tindrá que recarregar les cartes del robot, tindrá 20 segons abans que la ronda següent comenci:
        - Agafa el recipient amb compte de no moure res més
        - Retira les cartes de dins
        - Deixa el recipient amb compte
        - Aixeca la tela que no deixa veure les cartes del robot y recarrega aixecant el suport del motor dc les cartes per sota
        - Quan estiguis en la posició correcte espera a que els 20 segons acabin i continua!
- El que acabi amb totes les cartes guanya!


Autors:
- Pol Reyes Martí  | 1598229
- Eric Rodriguez Merichal | 1496793
- Valentí Torrents Vila | 1604484
- Guillermo Vivancos Alonso | 1606206


