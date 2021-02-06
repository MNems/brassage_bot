import os
import discord
from dotenv import load_dotenv

class BrassageBot(discord.Client):

    async def on_ready(self):
        print("Début du développement de ...", self.user)

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if "!brassage" in message.content:
            await message.reply('Belle action ', mention_author=True)


if __name__ == '__main__':
  load_dotenv()
  brassage_bot = BrassageBot()
  brassage_bot.run(os.getenv("DISCORD_TOKEN"))
