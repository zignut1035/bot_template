import sys
# This is mainly taken from https://discordpy.readthedocs.io/en/stable/quickstart.html
# To make the file watch for changes (the script is restarted each time you save the file),
# npm package nodemon can be used:
# 1: Install npm if you do not have it yet:
#    sudo apt update
#    sudo apt install npm
# 2. To install nodemon: sudo npm i -g nodemon
# 3: To run the file: nodemon --exec python3 bottemplate.py

discordToken = "MTA2MzA1NzAzNzQ4NDg5NjMyNg.GvDygk.d-dfAzWa7G5GrbIdvTlqSjv-rFKOkkCgJ0dGF4" # Your bot token here (https://discord.com/developers/applications/ and tab Bot -> Token -> Reset Token -> Copy the token here)
name = "csm101_treenut_yusufee" # Your bot name here


if (discordToken == ""): sys.exit("ERROR: Please set the discord token.")
if (name == ""): sys.exit("ERROR: Please set the name of the bot.")

# To use this package, install: pip3 install discord.py
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')
todo_dict = {}
@client.event
async def on_message(message):
  if message.author == client.user: return # We don't want to reply to ourselves

  # RULE: To not flood the channel with responses from multiple bots,
  # we only respond to messages that start with our name

  if message.content.startswith(name):
    print(f"{message.author} says: {message.content}")
    import random
    listt = message.content
    my_list = listt.split(" ", 2)
    print(f'splitted list2:', my_list)
    print(len(my_list))
    if my_list[1] == 'todo':
      if len(my_list) >= 3:
        todo_dict[len(todo_dict) + 1] = my_list[2]
        print(todo_dict)
        await message.channel.send(todo_dict)
      elif len(my_list) < 3:  
        print("No todo items")
        await message.channel.send("No todo items")
    if my_list[1] == "help":
      print("When asking your bot todo <todo item> it should add the given todo item to the dictionary and add numbering to the item.")  
      print("When asking your bot todo it should give back all todo items. By default, the todo list is empty, and if so, it should print out 'No todo items'.")
      print("When asking your bot todoremove <number> it should remove the todo item with the given number")
       
    if message.content.startswith(f'{name} hello'):
        await message.channel.send('Hello! I am ALIVE?')
client.run(discordToken)