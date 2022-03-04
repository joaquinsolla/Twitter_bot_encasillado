import tweepy
import json
import datetime

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
json_len = len(data)
print("json_len = " + json_len)

todayIndex = 0
todayIndex = round((3.14159265359 * datetime.date.day * datetime.date.month * datetime.date.year * 1000) % json_len) - 1
print("today_index = " + todayIndex)

wotd = "N/A"
wotd = {data[todayIndex]['word']}
print("wotd = " + wotd)

# Guardamos el mensaje final
msg = f"¡El Encasillado de hoy ha sido " + wotd + "!"
print(msg)

# Tuiteamos el resultado final pasándole el parámetro de mensaje y la imagen.
api.update_status(msg)