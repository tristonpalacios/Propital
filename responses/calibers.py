import discord
from utils.caliber_utils import get_all_calibers, create_views

async def list_calibers():
    calibers = await get_all_calibers()
    if calibers:
        embed = discord.Embed(title="Tarkov Calibers", description="Click a button to get ammo details.")
        views = create_views(calibers)
        return embed, views
    else:
        return "Failed to fetch calibers from the Tarkov API."
