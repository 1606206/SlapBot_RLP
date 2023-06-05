*SLAPBOT*:
SlapBot és un robot capaç de jugar a cartes, concretament al joc ("El Tapete"). El robot és composa en 4 parts, un mecanisme que carrega el "slap" del robot, un llença cartes, una càmera que fa d'"ulls" del robot i uns sensors que detecten qui ha guanyat la ronda.
Per poder detectar quines cartes s'han tirat fem ús d'una API de Roboflow com figura a la carpeta de src/raspberry_pi que processa el que veu la càmera, li passa a l'algorisme el resultat i per tant es genera una acció.

(Prèviament el reconeixement de les cartes s'havia de fer utilitzant la xarxa neuronal que figura a src/neural_network però com està explicat al explicacio.md de la corresponent carpeta no s'ha utilitzat finalment)

Software:
- Python 3 (con raspberry pi 4)
- C++ (con arduino)

API:
- Un projecte de roboflow per a detecció de cartes (detellat a src/raspberry_pi4/execute_program_and_cite_project_api_roboflow)

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

Src:
-Arduino:
        Amb l'arduino (codi en c++) controlem els sensors i els motors (juntament amb la controladora) per detectar el moviment i controlar els moviments dels motors quan calgui.
        En el cas dels sensors detecten qui pica a la taula abans, ja sigui quan hi ha una combinació o quan algun jugador pica a la taula sense que el robot hagi detectat una combinació; ja que també hi ha la probabilitat que l'API utiltizada per reconèixer les cartes falli i no detecti una possible combinació. Quan els sensors detecten que o el robot o un jugador ha picat a la taula l'arduino envia la senyal a la raspberry pi 4 per a que ho sàpiga.

-Neural_Network:

-Raspberry_pi4:



Com Jugar:
- La partida i la ronda la comença SEMPRE el robot (es una forma de "timejar" tot)
- El jugador quan rebi la notificació podrà tirar la carta al recipient
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


