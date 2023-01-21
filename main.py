import nextcord
from nextcord.ext import commands
import random
import asyncio

intents = nextcord.Intents.all() #Can be optimized

client = commands.Bot(command_prefix=commands.when_mentioned_or(".."), intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as: {client.user}\n--------------------\nBot is ready\n--------------------")

@client.command(aliases=['hang'])
async def hangman(ctx):
    words = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage"
                   ,"plants"] #You can add more words!
    word = random.choice(words)
        
    correct_letters = []
        
    incorrect_letters = []
        
    chances = 6
        
    word_state = ["-"] * len(word)
       
    display = await ctx.send(f"Word: {' '.join(word_state)}\nChances: {chances}")
    message = await ctx.send("---------------")
        
    game_over = False
    while not game_over:

        guess = await client.wait_for('message', check=lambda m: m.author == ctx.author, timeout=60)
        
        if len(guess.content) == 1 and guess.content.isalpha():
            
            if guess.content in correct_letters or guess.content in incorrect_letters:
                temp = await ctx.send("You have already guessed that letter!")
                await asyncio.sleep(1)
                await guess.delete()
                await temp.delete()
                await display.edit(f"Word: {' '.join(word_state)}\nChances: {chances}")
               
            elif guess.content in word:
                correct_letters.append(guess.content)
                
                for i, c in enumerate(word):
                    if c == guess.content:
                        word_state[i] = c

                if all(c in correct_letters for c in word):
                    await ctx.send(f"Congratulations, you won!\nThe word was {word}")
                    game_over = True

                else:
                    temp = await ctx.send("Correct!")
                    await asyncio.sleep(0.5)
                    await guess.delete()
                    await temp.delete()
                    await display.edit(f"Word: {' '.join(word_state)}\nChances: {chances}")
            else:
                incorrect_letters.append(guess.content)
                chances -= 1
                    
                if chances == 0:
                    await guess.delete()
                    await asyncio.sleep(0.5)
                    await msg.delete()
                    await message.edit(content="   ------- \n"
                                            "  |     | \n"
                                            "  |     |\n"
                                            "  |     | \n"
                                            "  |     O \n"
                                            "  |    /|\ \n"
                                            "  |    / \ \n"
                                            "-----\n"
                                            "-----------------------\n"
                                            "Wrong guess. You are hanged!!!")
                    await display.edit(f"Word: {' '.join(word_state)}\nChances: {chances}")
                    game_over = True

                elif chances == 5:
                    msg = await ctx.send(f"Incorrect!")
                    await guess.delete()
                    await asyncio.sleep(0.5)
                    await msg.delete()
                    await message.edit(content="   -------\n"
                                                "  |      \n"
                                                "  |      \n"
                                                "  |      \n"
                                                "  |      \n"
                                                "  |      \n"
                                                "  |      \n"
                                                "-----\n"
                                                "-----------------------\n")
                    await display.edit(f"Word: {' '.join(word_state)}\nChances: {chances}")

                elif chances == 4:
                    msg = await ctx.send(f"Incorrect!")
                    await guess.delete()
                    await asyncio.sleep(0.5)
                    await msg.delete()
                    await message.edit(content="   -------\n"
                                            "  |     | \n"
                                            "  |     |\n"
                                            "  |      \n"
                                            "  |      \n"
                                            "  |      \n"
                                            "  |      \n"
                                            "-----\n"
                                            "-----------------------\n")
                    await display.edit(f"Word: {' '.join(word_state)}\nChances: {chances}")

                elif chances == 3:
                    msg = await ctx.send(f"Incorrect!")
                    await guess.delete()
                    await asyncio.sleep(0.5)
                    await msg.delete()
                    await message.edit(content="   -------\n"
                                            "  |     | \n"
                                            "  |     |\n"
                                            "  |     | \n"
                                            "  |      \n"
                                            "  |      \n"
                                            "  |      \n"
                                            "-----\n"
                                            "-----------------------\n")
                    await display.edit(f"Word: {' '.join(word_state)}\nChances: {chances}")

                elif chances == 2:
                    msg = await ctx.send(f"Incorrect!")
                    await guess.delete()
                    await asyncio.sleep(0.5)
                    await msg.delete()
                    await message.edit(content="   -------\n"
                                            "  |     | \n"
                                            "  |     |\n"
                                            "  |     | \n"
                                            "  |     O \n"
                                            "  |      \n"
                                            "  |      \n"
                                            "-----\n"
                                            "-----------------------\n")
                    await display.edit(f"Word: {' '.join(word_state)}\nChances: {chances}")
                    
                elif chances == 1:
                    msg = await ctx.send(f"Incorrect!")
                    await guess.delete()
                    await asyncio.sleep(0.5)
                    await msg.delete()
                    await message.edit(content="   ------- \n"
                                            "  |     | \n"
                                            "  |     |\n"
                                            "  |     | \n"
                                            "  |     O \n"
                                            "  |    /|\ \n"
                                            "  |     \n"
                                            "-----\n"
                                            "-----------------------\n")
                    await display.edit(f"Word: {' '.join(word_state)}\nChances: {chances}")
        else:
            await ctx.send("Please enter a single letter.")            

TOKEN = "" #Add your token

client.run(TOKEN)