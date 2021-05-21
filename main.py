# bot.py
import discord
import os
import rates
import random
from wonderwords import RandomWord
from udpy import UrbanClient

client = discord.Client()
r = RandomWord()
UClient = UrbanClient()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if "bum" in message.content:
    emoji = '🏳️‍🌈'
    await message.add_reaction(emoji)

  if message.content.startswith('sir, '):
    if message.content.startswith('sir, help'):
      HelpEmbed = discord.Embed(title = "Every command there is", color = random.randint(0, 16777215))
      HelpEmbed.add_field(name="Rates", value="qwordrate\nfurryrate\ngayrate\ndankrate\ngamerrate\nthotrate", inline=False)
      HelpEmbed.add_field(name="Others", value="fetish\ninsult", inline=False)
      HelpEmbed.set_footer(text = "Type 'sir,' followed by the cmd you want to use")
      await message.channel.send(embed = HelpEmbed)

    if message.content.startswith('sir, qwordrate'):
      WhichRate = "Q-word"
      Rate = (random.randint(1,101))
      if len(message.content) != 14:
        AllArgs = str(message.content)[13:-1] + str(message.content)[-1]
        Rating =  AllArgs + " is " + str(Rate) + "% Q-word!"
      else:
        Rating =  "You are " + str(Rate) + "% Q-word!"
    
      RateEmbed = discord.Embed(title = "✨ Q-word rate ✨", description = Rating, color = random.randint(0, 16777215))
      rates.Rate(Rate, WhichRate, RateEmbed)
      RateEmbed.set_thumbnail(url = "https://media.discordapp.net/attachments/709674340504829974/810920366233878588/arabic.png")
      await message.channel.send(embed = RateEmbed)

    if message.content.startswith('sir, furryrate'):
      WhichRate = "Q-word"
      Rate = (random.randint(1,101))
      if len(message.content) != 14:
        AllArgs = str(message.content)[13:-1] + str(message.content)[-1]
        Rating =  AllArgs + " is " + str(Rate) + "% furry!"
      else:
        Rating =  "You are " + str(Rate) + "% furry!"
    
      RateEmbed = discord.Embed(title = "🐺 Furry rate 🐺", description = Rating, color = random.randint(0, 16777215))
      rates.Rate(Rate, WhichRate, RateEmbed)
      RateEmbed.set_thumbnail(url = "https://upload.wikimedia.org/wikipedia/commons/f/fb/Anthro_vixen_colored.jpg")
      await message.channel.send(embed = RateEmbed)
  
    if message.content.startswith('sir, gayrate'):
      WhichRate = "gay"
      Rate = (random.randint(1,101))
      if len(message.content) != 12:
        AllArgs = str(message.content)[11:-1] + str(message.content)[-1]
        Rating =  AllArgs + " is " + str(Rate) + "% gay!"
      else:
        Rating =  "You are " + str(Rate) + "% gay!"
    
      RateEmbed = discord.Embed(title = "🏳️‍🌈 Gay rate 🏳️‍🌈", description = Rating, color = random.randint(0,16777215))
      rates.Rate(Rate, WhichRate, RateEmbed)
      RateEmbed.set_thumbnail(url = "https://www.tripridetn.org/wp-content/uploads/pride-flags-11.jpg")
      await message.channel.send(embed = RateEmbed)
  
    if message.content.startswith('sir, dankrate'):
      WhichRate = "dank"
      Rate = (random.randint(1,101))
      if len(message.content) != 13:
        AllArgs = str(message.content)[12:-1] + str(message.content)[-1]
        Rating =  AllArgs + " is " + str(Rate) + "% dank!"
      else:
        Rating =  "You are " + str(Rate) + "% dank!"
    
      RateEmbed = discord.Embed(title = "😎 Dank rate 😎", description = Rating, color = random.randint(0, 16777215))
      rates.Rate(Rate, WhichRate, RateEmbed)
      RateEmbed.set_thumbnail(url = "https://dankmemer.lol/40326fed0d1bc75a2688535e70dd31be.png")
      await message.channel.send(embed = RateEmbed)

    if message.content.startswith('sir, gamerrate'):
      WhichRate = "gamer"
      Rate = (random.randint(1,101))
      if len(message.content) != 14:
        AllArgs = str(message.content)[13:-1] + str(message.content)[-1]
        Rating =  AllArgs + " is " + str(Rate) + "% gamer!"
      else:
        Rating =  "You are " + str(Rate) + "% gamer!"
    
      RateEmbed = discord.Embed(title = "🎮 Gamer rate 🎮", description = Rating, color = random.randint(0, 16777215))
      rates.Rate(Rate, WhichRate, RateEmbed)
      RateEmbed.set_thumbnail(url = "https://miro.medium.com/max/1400/1*FRtwS_vPzro4ozZ9QJ2bLQ.png")
      await message.channel.send(embed = RateEmbed)

    if message.content.startswith('sir, thotrate'):
      WhichRate = "thot"
      Rate = (random.randint(1,101))
      if len(message.content) != 13:
        AllArgs = str(message.content)[12:-1] + str(message.content)[-1]
        Rating =  AllArgs + " is " + str(Rate) + "% thot!"
      else:
        Rating =  "You are " + str(Rate) + "% thot!"
    
      RateEmbed = discord.Embed(title = "😩 Thot rate 😩", description = Rating, color = random.randint(0, 16777215))
      rates.Rate(Rate, WhichRate, RateEmbed)
      await message.channel.send(embed = RateEmbed)

    if message.content.startswith('sir, insult'):
      Insult = "You are a " + r.word(include_parts_of_speech=["adjectives"]) + " " + r.word(include_parts_of_speech=["noun"])
      InsultEmbed = discord.Embed(title = "Insult", description = Insult, color = random.randint(0, 16777215))
      InsultEmbed.set_footer(text = "Feel hurt?")
      await message.channel.send(embed = InsultEmbed)
    
    if message.content.startswith('sir, fetish'):
      Fetish = r.word(include_parts_of_speech=["noun"]) + " fetish"
      RealDefinition = UClient.get_definition(Fetish)
      if len(RealDefinition) == 0:
        PrintFetish = "No"
      else:
        PrintFetish = RealDefinition[0].definition
      FetishEmbed = discord.Embed(title = "Time to create a fetish!", color = random.randint(0, 16777215))
      FetishEmbed.add_field(name = "Fetish name:", value = Fetish, inline=False)
      FetishEmbed.add_field(name = "Is it real?", value = PrintFetish, inline=False)
      await message.channel.send(embed = FetishEmbed)


client.run(os.getenv('DISCORD_TOKEN'))
