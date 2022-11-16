import discord
from discord import app_commands

token = "INSERT TOKEN HERE"

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild = None)
            self.synced = True
        print(f"We have logged in as {self.user}")

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name = "givemebadge", description = "it's morbin time", guild = None)
async def self(interaction: discord.Interaction):
    await interaction.response.send_message("ok now time to wait (https://discord.com/developers/active-developer)")

client.run(token)
