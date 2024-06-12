import discord
from utils.request_utils import tarkov_api_request

async def query_tarkov_api(caliber: str) -> discord.Embed:
    query = '''
    {
      ammo {
        item {
          name
        }
        caliber
        damage
        penetrationPower
        ammoType
      }
    }
    '''
    data = await tarkov_api_request(query)
    if data:
        return format_tarkov_response(data, caliber)
    else:
        embed = discord.Embed(title="Error", description="Failed to fetch data from the Tarkov API.")
        return embed

def format_tarkov_response(data: dict, caliber: str) -> discord.Embed:
    ammo = data.get('data', {}).get('ammo', [])
    if not ammo:
        embed = discord.Embed(title="Tarkov Ammo Details", description="No ammo found for the specified caliber.")
        return embed

    filtered_ammo = [item for item in ammo if item['caliber'].lower() == caliber.lower()]

    if not filtered_ammo:
        embed = discord.Embed(title="Tarkov Ammo Details", description="No ammo found for the specified caliber.")
        return embed

    # Sort by penetrationPower in descending order
    sorted_ammo = sorted(filtered_ammo, key=lambda x: x['penetrationPower'], reverse=True)

    embed = discord.Embed(title="Tarkov Ammo Details")
    for item in sorted_ammo:
        embed.add_field(
            name=f"**{item['item']['name']}**",
            value=(
                f"> Caliber: {item['caliber']}\n"
                f"> Damage: {item['damage']}\n"
                f"> Penetration: {item['penetrationPower']}\n"
                f"> Type: {item['ammoType']}"
            ),
            inline=False
        )
    return embed
