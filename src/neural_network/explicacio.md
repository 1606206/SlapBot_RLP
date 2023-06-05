Tot i aconseguir un accuracy alt de train i un alt accuracy de test amb la BBDD, el passar-ho al programa no aconseguiem que encertes les cartes.
Així doncs, com es reflexa al programa de la raspberry pi s'ha decidit utilitzar l'api de roboflow utilitzant un model ja entrenat.

Així i tot, en aquesta carpeta es pot veure el codi per entrenar el model (.ipynb ja que s'ha utilitzat google colab per entrenar per la falta de recursos que teniem de cpu i gpu), la funció que es cridaria per obtenir la predicció i un exemple de com cridavem la funció utilitzant el model entrenat.