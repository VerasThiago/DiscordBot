import discord
import asyncio
import requests
from bs4 import BeautifulSoup

client = discord.Client()



@client.event
async def on_ready():
	print(client.user.name)
	print(client.user.id)

@client.event
async def on_message(message):



	
	msg = message.content.lower()

	if(msg.startswith("!oi")):
		await client.send_tts_messages(message.channel, 'tnc viado')
	elif(msg.startswith("!build")):
		string = msg.split(' ', 1)
		
		champ = string[1]

		url = 'https://www.probuilds.net/champions/details/' + champ

		r = requests.get(url,stream=True)

		soup = BeautifulSoup(r.text, 'html.parser')
		divTag = soup.find_all("div", {"class":"item tooltip"})

		i = 1

		if(len(divTag) == 0):
			await client.send_message(message.channel, champ + ' não encontrado.')

		else:
			await client.send_message(message.channel, 'Build lixo pro ' + champ)
			for tag in divTag:
				if(i > 6):
					break
				palavra = str(tag)
				palavra = palavra.split('src="')
				print(palavra[0])
				imgLink = palavra[1][:-10]
				palavra = palavra[0].split('alt="')
				item = palavra[1][:-2]
				emb = discord.Embed()
				emb.set_author(name = item, icon_url = imgLink)
				await client.send_message(message.channel, embed=emb)
				i += 1







client.run('TOKEN KEY HERE')