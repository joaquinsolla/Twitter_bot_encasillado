import tweepy
import json
import datetime

from Twitter_Files.tw_credentials import *

# Abrimos el archivo json
with open('word_database.json') as f:
    data = json.load(f)

# Nos autenticamos en Twitter e iniciamos el cliente
client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)

# Se calcula la palabra del dia
json_len = len(data)
print("json_len = " + str(json_len))


#int(datetime.date.day) * int(datetime.date.month) * int(datetime.date.year)
todayIndex = 0
todayIndex = round((3.14159265359 * 2 * 1000) % json_len) - 1
print("today_index = " + str(todayIndex))

wotd = "N/A"
wotd = data[todayIndex]['word']
print("wotd = " + str(wotd))

# Guardamos el mensaje final
msg = f"El #Encasillado de hoy ha sido: " + str(wotd) + "\n\nhttps://play.google.com/store/apps/details?id=com.joa.encasillado"
print(msg)

# Publicamos el tweet
client.create_tweet(text=msg)
print("\nTWEET CREATED AND PUBLISHED")