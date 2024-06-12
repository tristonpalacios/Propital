from discord.ui import View, Button
import requests
import discord
from utils.request_utils import tarkov_api_request
from responses.ammo import query_tarkov_api
from responses.ammo import format_tarkov_response

def normalize_caliber(caliber: str) -> str:
    if not caliber.startswith('Caliber'):
        return 'Caliber' + caliber.replace('x', 'x').replace('.', '')
    return caliber

def create_views(calibers: list):
    views = []
    view = discord.ui.View()
    for i, caliber in enumerate(calibers):
        if i % 25 == 0 and i != 0:
            views.append(view)
            view = discord.ui.View()
        button_label = caliber.replace("Caliber", "")
        button = discord.ui.Button(label=button_label, style=discord.ButtonStyle.primary)
        button.callback = create_callback(caliber)
        view.add_item(button)
    views.append(view)
    return views

def create_callback(caliber: str):
    async def callback(interaction):
        response = await query_tarkov_api(caliber)
        await interaction.response.send_message(embed=response)

    return callback

async def get_all_calibers() -> list:
    query = '''
    {
      ammo {
        caliber
      }
    }
    '''
    data = await tarkov_api_request(query)
    return extract_calibers(data)

def extract_calibers(data: dict) -> list:
    ammo = data.get('data', {}).get('ammo', [])
    calibers = {item['caliber'] for item in ammo}
    return sorted(calibers)
