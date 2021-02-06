import os
import discord


class BrassageBot:

    def __init__(self, client, token) -> None:
        super().__init__()
        self.client = client
        self.token = token

        @client.event
        async def say_hi():
            print("Début du développement de ...", client.user)

    def run(self):
        self.client.run(self.token)


if __name__ == '__main__':
    brassage_bot = BrassageBot(discord.Client(), os.getenv("DISCORD_TOKEN"))
    brassage_bot.run()
