import tweepy
import json
import datetime

from tw_credentials import *

# VERSION DE APP (Next: 1.2.5)
appVersion = "1.2.3"
print("Encasillado Bot - App-version: " + appVersion)

# Abrimos el archivo json
print(" - Opening json . . .")
with open('current_database.json') as f:
    data = json.load(f)

# Nos autenticamos en Twitter e iniciamos el cliente
print(" - Twitter authentication . . .")
client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token,
                       access_token_secret=access_token_secret)

# Se calcula la palabra del dia
json_len = len(data)
todayIndex = 0
todayIndex = round((3.14159265359 * datetime.datetime.today().day * datetime.datetime.today().month *
                    datetime.datetime.today().year * 1000) % json_len) - 1
print(" - Today index: " + str(todayIndex))

wotd = "N/A"
wotd = data[todayIndex]['word']
print(" + WOTD: " + wotd)

# Guardamos el mensaje final
msg = f"#Encasillado del " + str(datetime.datetime.today().day) + "/" + str(datetime.datetime.today().month) + "/" + \
      str(datetime.datetime.today().year) + ": " + str(
    wotd) + "\n\nEncasillado(" + appVersion + ") https://play.google.com/store/apps/details?id=com.joa.encasillado"
print(" + MESSAGE: " + msg)

# Publicamos el tweet
client.create_tweet(text=msg)
print("\nTWEET CREATED AND PUBLISHED SUCCESSFULLY")

with open("bot_log.log", "a") as logFile:
 logFile.write(str(datetime.datetime.today().day) + "/" + str(datetime.datetime.today().month) + "/" +
               str(datetime.datetime.today().year) + " - " + wotd + "\n")
