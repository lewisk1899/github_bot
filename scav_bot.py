import discord  # discord library
import requests  # library allows us to request data from apis, the data will be returned in json
import json
import random

from prevent_from_close import keep_running

client = discord.Client()  # creating an instance of a client, which is the connection to discord
tarkov_trigger = ['play', 'is anyone on', 'tarkov', 'EFT',
                  'escape from tarkov']  # anytime my friends reference a game the bot will say something about it

bot_tarkov_responses = ['Oyy!', 'Cheeky Breeky', 'Kepka', 'Vot khuy!', 'Chiki-briki, palchik vykin',
                        'Da yobushki-vorobushki', 'Gandon yebuchiy!']


def get_quote():
    response = requests.get(
        "https://zenquotes.io/api/random")  # this will return a random quote from this api, should be in a
    json_data = json.loads(response.text)  # getting the response and loading it into a quote
    quote = json_data[0]['q'] + " -" + json_data[0]['a']  # q stands for quote
    return quote


# this is an event that happens as soon as the bot is ready
@client.event
async def on_ready():
    print("We have logged in as  {0.user}".format(client))


# trigger if message received
@client.event
async def on_messsage(msg):
    msg = msg.content
    if msg.author == client.user:
        return
    # if anyone says $hello in the chat the bot will respond with hello
    if msg.content.startswith('$hello'):
        await msg.channel.send('Hello!')

    if msg.content.startswith('$inspire'):
        quote = get_quote()
        await msg.channel.send(quote)
        # anytime someone wants to play tarkov bot will say something that a scav would say

    if any(word in msg.content.lower() for word in tarkov_trigger):
        await msg.channel.send(random.choice(bot_tarkov_responses))

token = ""
keep_running()
client.run(token)  # getting the token from the env file