import tweepy
import json
import datetime

from tw_credentials import *

# VERSION DE APP
appVersion = "1.0.4"

# Abrimos el archivo json
with open('word_database.json') as f:
    data = json.load(f)

# Nos autenticamos en Twitter e iniciamos el cliente
client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token,
                       access_token_secret=access_token_secret)

# Se calcula la palabra del dia
json_len = len(data)
# print("json_len = " + str(json_len))


todayIndex = 0
todayIndex = round((3.14159265359 * datetime.datetime.today().day * datetime.datetime.today().month *
                    datetime.datetime.today().year * 1000) % json_len) - 1
# print("today_index = " + str(todayIndex))

wotd = "N/A"
wotd = data[todayIndex]['word']
# print("wotd = " + str(wotd))

# Guardamos el mensaje final
msg = f"#Encasillado del " + str(datetime.datetime.today().day) + "/" + str(datetime.datetime.today().month) + "/" + \
      str(datetime.datetime.today().year) + ": " + str(
    wotd) + "\n\nEncasillado(" + appVersion + ") https://play.google.com/store/apps/details?id=com.joa.encasillado"
# print(msg)

# Publicamos el tweet
client.create_tweet(text=msg)
#print("\nTWEET CREATED AND PUBLISHED")
