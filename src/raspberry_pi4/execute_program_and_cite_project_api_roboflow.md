# S'utilitza com API de Roboflow per a visió per computador un model ja entrenat.

# Crear un docker a la terminal de la raspberry pi:
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Terminal 1 executar les dues comandes següents:
### Comanda 1
sudo docker pull roboflow/inference-server:cpu
### Comanda 2
sudo docker run --net=host roboflow/inference-server:cpu

# Terminal 2 executar les dues comandes següents quan a terminal 1 surti que inference-server està llest per rebre tràfic:
### Comanda 1
python -m venv raspi
### Comanda 2
source raspi/bin/activate

A partir d'aquí executar el programa a la terminal 2 (si no està instal·lat roboflow fer: pip install roboflow al terminal 2):
python3 programa.py

# Citació a l'api de roboflow utilitzada; que al codi programa.py es crida:

@misc{ carddetpokerdeck_dataset,
    title = { carddetpokerdeck Dataset },
    type = { Open Source Dataset },
    author = { h },
    howpublished = { \url{ https://universe.roboflow.com/h-pv33i/carddetpokerdeck } },
    url = { https://universe.roboflow.com/h-pv33i/carddetpokerdeck },
    journal = { Roboflow Universe },
    publisher = { Roboflow },
    year = { 2023 },
    month = { may },
    note = { visited on 2023-06-05 },
}
