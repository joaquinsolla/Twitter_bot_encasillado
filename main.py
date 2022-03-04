import tweepy
import json
import random

from Twitter_Files.tw_credentials import *

# Abrimos el archivo json
with open('word_database.json') as f:
    data = json.load(f)

# Nos autenticamos en Twitter
auth = tweepy.OAuthHandler(botUsername, botPassword)
auth.set_access_token(apiKey, apiKeySecret)

# Creamos un objeto de la libreria
api = tweepy.API(auth)

# Se calcula la palabra del dia

#CALCULAR

# borrar:
today_index = 0
while data[today_index]['appear'] == "True":
    today_index = int(random.uniform(0, len(data)))
    if data[today_index]['appear'] == "False":
        data[today_index]['appear'] = "True"
        break

# Abrimos el archivo json con permisos para escritura
with open('word_database.json', 'w') as f:
    f.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))

# Guardamos el mensaje final
msg = f"¡El Encasillado de hoy ha sido {data[today_index]['word']}!"

# Tuiteamos el resultado final pasándole el parámetro de mensaje y la imagen.
api.update_status(msg)