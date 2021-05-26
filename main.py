import discord
import os
import rates
import random
import time
from wonderwords import RandomWord
from udpy import UrbanClient

client = discord.Client(activity = discord.Game(name = "bingo"))
r = RandomWord()
UClient = UrbanClient()

@client.event
async def on_ready():
  print('I have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  MsgContent = message.content.lower()
  
  if message.author == client.user:
    return
  
  if message.author.id == 204255221017214977 and message.channel.id == 828274056440446976 and message.content.endswith("prayer."):
    await message.channel.send("🙏")
  
  if MsgContent.startswith('sir, help'):
    HelpEmbed = discord.Embed(title = "Every command there is", color = random.randint(0, 16777215))
    HelpEmbed.add_field(name="Rates", value="qwordrate\nfurryrate\ngayrate\ndankrate\ngamerrate\nthotrate", inline=True)
    HelpEmbed.add_field(name="Talking to Jonathan", value="hello\nwill you marry me?\nsend a selfie\nsmell me", inline=True)
    HelpEmbed.add_field(name="Others", value="fetish\ninsult\npp\nstatus (p/w/c)\nwho is gay", inline=False)
    HelpEmbed.set_footer(text = "Type 'sir,' followed by the cmd you want to use")
    await message.channel.send(embed = HelpEmbed)

  if MsgContent.startswith('sir, qwordrate'):
    WhichRate = "Q-word"
    Rate = (random.randint(0,100))
    if len(message.content) != 14:
      AllArgs = str(message.content)[14:-1] + str(message.content)[-1]
      Rating =  AllArgs + " is " + str(Rate) + "% Q-word!"
    else:
      Rating =  message.author.mention + " is " + str(Rate) + "% Q-word!"
    
    RateEmbed = discord.Embed(title = "✨ Q-word rate ✨", description = Rating, color = random.randint(0, 16777215))
    rates.Rate(Rate, WhichRate, RateEmbed)
    RateEmbed.set_thumbnail(url = "https://media.discordapp.net/attachments/709674340504829974/810920366233878588/arabic.png")
    await message.channel.send(embed = RateEmbed)

  if MsgContent.startswith('sir, furryrate'):
    WhichRate = "furry"
    Rate = (random.randint(0,100))
    if len(message.content) != 14:
      AllArgs = str(message.content)[14:-1] + str(message.content)[-1]
      Rating =  AllArgs + " is " + str(Rate) + "% furry!"
    else:
      Rating =  message.author.mention + " is " + str(Rate) + "% furry!"
    
    RateEmbed = discord.Embed(title = "🐺 Furry rate 🐺", description = Rating, color = random.randint(0, 16777215))
    rates.Rate(Rate, WhichRate, RateEmbed)
    RateEmbed.set_thumbnail(url = "https://upload.wikimedia.org/wikipedia/commons/f/fb/Anthro_vixen_colored.jpg")
    await message.channel.send(embed = RateEmbed)
  
  if MsgContent.startswith('sir, gayrate'):
    WhichRate = "gay"
    Rate = (random.randint(0,100))
    if len(message.content) != 12:
      AllArgs = str(message.content)[12:-1] + str(message.content)[-1]
      Rating =  AllArgs + " is " + str(Rate) + "% gay!"
    else:
      Rating =  message.author.mention + " is " + str(Rate) + "% gay!"
  
    RateEmbed = discord.Embed(title = "🏳️‍🌈 Gay rate 🏳️‍🌈", description = Rating, color = random.randint(0,16777215))
    rates.Rate(Rate, WhichRate, RateEmbed)
    RateEmbed.set_thumbnail(url = "https://www.tripridetn.org/wp-content/uploads/pride-flags-11.jpg")
    await message.channel.send(embed = RateEmbed)

  if MsgContent.startswith('sir, dankrate'):
    WhichRate = "dank"
    Rate = (random.randint(0,100))
    if len(message.content) != 13:
      AllArgs = str(message.content)[13:-1] + str(message.content)[-1]
      Rating =  AllArgs + " is " + str(Rate) + "% dank!"
    else:
      Rating =  message.author.mention + " is " + str(Rate) + "% dank!"
  
    RateEmbed = discord.Embed(title = "😎 Dank rate 😎", description = Rating, color = random.randint(0, 16777215))
    rates.Rate(Rate, WhichRate, RateEmbed)
    RateEmbed.set_thumbnail(url = "https://dankmemer.lol/40326fed0d1bc75a2688535e70dd31be.png")
    await message.channel.send(embed = RateEmbed)

  if MsgContent.startswith('sir, gamerrate'):
    WhichRate = "gamer"
    Rate = (random.randint(0,100))
    if len(message.content) != 14:
      AllArgs = str(message.content)[14:-1] + str(message.content)[-1]
      Rating =  AllArgs + " is " + str(Rate) + "% gamer!"
    else:
      Rating =  message.author.mention + " is " + str(Rate) + "% gamer!"
  
    RateEmbed = discord.Embed(title = "🎮 Gamer rate 🎮", description = Rating, color = random.randint(0, 16777215))
    rates.Rate(Rate, WhichRate, RateEmbed)
    RateEmbed.set_thumbnail(url = "https://miro.medium.com/max/1400/1*FRtwS_vPzro4ozZ9QJ2bLQ.png")
    await message.channel.send(embed = RateEmbed)

  if MsgContent.startswith('sir, thotrate'):
    WhichRate = "thot"
    Rate = (random.randint(0,100))
    if len(message.content) != 13:
      AllArgs = str(message.content)[13:-1] + str(message.content)[-1]
      Rating =  AllArgs + " is " + str(Rate) + "% thot!"
    else:
      Rating =  message.author.mention + " is " + str(Rate) + "% thot!"
  
    RateEmbed = discord.Embed(title = "😩 Thot rate 😩", description = Rating, color = random.randint(0, 16777215))
    rates.Rate(Rate, WhichRate, RateEmbed)
    await message.channel.send(embed = RateEmbed)

  if MsgContent.startswith('sir, insult'):
    Insult = "You are a " + r.word(include_parts_of_speech=["adjectives"]) + " " + r.word(include_parts_of_speech=["noun"])
    InsultEmbed = discord.Embed(title = "Insult", description = Insult, color = random.randint(0, 16777215))
    InsultEmbed.set_footer(text = "Feel hurt?")
    await message.channel.send(embed = InsultEmbed)
  
  if MsgContent.startswith('sir, fetish'):
    Fetish = r.word(include_parts_of_speech = ["noun"]) + " fetish"
    RealDefinition = UClient.get_definition(Fetish)
    if len(RealDefinition) == 0:
      PrintFetish = "No"
    else:
      PrintFetish = RealDefinition[0].definition
    FetishEmbed = discord.Embed(title = "Time to create a fetish!", color = random.randint(0, 16777215))
    FetishEmbed.add_field(name = "Fetish name:", value = Fetish, inline=False)
    FetishEmbed.add_field(name = "Is it real?", value = PrintFetish, inline=False)
    await message.channel.send(embed = FetishEmbed)
  
  if MsgContent.startswith('sir, status'):
    if str(MsgContent[12]) == "p":
      AllArgs = str(message.content)[14:-1] + str(message.content)[-1]
      await client.change_presence(activity = discord.Game(name = AllArgs))
      await message.channel.send("My playing status has now changed to '" + AllArgs + "'")
    elif str(MsgContent[12]) == "w":
      AllArgs = str(message.content)[14:-1] + str(message.content)[-1]
      await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = AllArgs))
      await message.channel.send("My watching status has now changed to '" + AllArgs + "'")
    elif str(MsgContent[12]) == "c":
      await client.change_presence(status=None)
      await message.channel.send("My status has been cleared")
    else:
      await message.channel.send("Type 'sir,' followed by either 'p' or 'w' then your status of choice")
      
  if MsgContent.startswith('sir, send a selfie'):
    await message.channel.send("https://cdn.discordapp.com/avatars/844593412157866045/3e206564d1cc050d67979c54864a5892.png?size=512")
  
  if MsgContent.startswith('sir, hi') or MsgContent.startswith('sir, hello'):
    with open("DadTalk.txt") as DadTalk:
      Lines = DadTalk.readlines()
      await message.channel.send(random.choice(Lines))

  if MsgContent.startswith('sir, will you marry me?'):
    if random.randint(0,5) == 0:
      await message.channel.send("Of course!")
    else:
      await message.channel.send("Why would I?")
      time.sleep(1)
      await message.channel.send("I have a wife and kids.")

  if MsgContent.startswith('sir, pp'):
    if len(message.content) != 7:
      AllArgs = str(message.content)[7:-1] + str(message.content)[-1]
    else:
      AllArgs = message.author.mention
    PenisSize = '=' * random.randint(0,25)
    PenisEmbed = discord.Embed(title = "Penis size:", description = AllArgs + "'s penis:\n8" + PenisSize + "D", color = random.randint(0, 16777215))
    await message.channel.send(embed = PenisEmbed)
  
  if MsgContent.startswith('sir, smell me'):
    Smell = r.word(include_parts_of_speech = ["adjective"])
    SmellEmbed = discord.Embed(title = "What do you smell like?", description = "You smell " + Smell, color = random.randint(0, 16777215))
    SmellEmbed.set_thumbnail(url = "http://www.freeimageslive.com/galleries/medical/pics/nose2331.jpg")
    await message.channel.send(embed = SmellEmbed)
    
  if MsgContent.startswith('sir, who is gay'):
    guild = client.guilds[0]
    Ids = [member.id for member in guild.members]
    Gay = random.choice(Ids)
    GayEmbed = discord.Embed(title = "Who is gay?", description = "<@" + Gay + "> is the gay" , color = random.randint(0, 16777215))
    GayEmbed.set_thumbnail(url = "https://www.tripridetn.org/wp-content/uploads/pride-flags-11.jpg")
    await message.channel.send(embed = GayEmbed)

client.run(os.getenv('DISCORD_TOKEN'))
