*SLAPBOT*:
SlapBot es un robot capaç de jugar a les cartes, concretament al joc ("El Tapete"). El robot es composa en 4 parts, un mecanisme que carregua el "slap" del robot, un llença cartes, una càmera que es els "ulls" dels robot i uns sensors que detecten qui ha guanyat la ronda.
Per poder detectar quines cartes s'han tirat fem us d'una Xarxa Neuronal que processa el que veu la càmera, li passa al algorisme el resultat i per tant es genera una acció.

Software:
- Python 3.10.x
- RPi.GPIO
- Arduino

Hardware:
- Raspberry Pi
- Camara
- Arduino Nano
- Sensor Ultrasó x2
- Motor DC 
- Altaveu
- Mini Motor DC
- Amplificador de soroll

Como Jugar:
- La partida comença SEMPRE amb el robot (es una forma de "timejar" tot)
- El jugador quan rebi la notificació podrà tirar la carta al recipient. (es necessari que el programa processi la carta primer)
- Al finalitzar una de las rondes el jugador en cas de que el robot hagi guanyat tindrá que recarregar les cartes del robot, tindrá 20 segons avans que la ronda següent comenci
        - Agafa el recipient amb compte de no moure lo demés
        - Retira les cartes de dins
        - Deixa el recipient amb compte
        - Aixeca la tela que no deixa veure les cartes del robot y recarrega aixecant el suport del motor dc les cartes per sota
        - Quan estiguis en la posició correcte espera a que els 20 segons acabin i continua!
- El que Acabi amb totes les cartes guanya!



Autors:
- Valentí Torrents | 1604484
- Guillermo Vivancos Alonso | 1606206
- Eric Rodriguez | 1496793
- Pol Reyes | 1598229
