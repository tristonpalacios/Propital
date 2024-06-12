import discord
from utils.request_utils import tarkov_api_request

async def check_bosses():
    query = '''
    {
      maps {
        name
        bosses {
          name
          spawnChance
        }
      }
    }
    '''
    data = await tarkov_api_request(query)
    if data:
        return format_boss_response(data)
    else:
        embed = discord.Embed(title="Error", description="Failed to fetch data from the Tarkov API.")
        return embed

def format_boss_response(data: dict):
    maps = data.get('data', {}).get('maps', [])

    if not maps:
        embed = discord.Embed(title="Tarkov Bosses", description="No boss data found.")
        return embed

    bosses = {}
    for map_data in maps:
        map_name = map_data['name']
        for boss in map_data['bosses']:
            boss_name = boss.get('name', 'N/A')
            if boss_name in ['Raider', 'Rogue']:
                continue
            if boss_name == 'Death Knight':
                boss_name = 'Death Knight (Goons)'
            spawn_chance = boss.get('spawnChance', 'N/A')

            if boss_name not in bosses:
                bosses[boss_name] = []

            bosses[boss_name].append((map_name, spawn_chance))

    embeds = []
    embed = discord.Embed(title="Tarkov Boss Spawn Rates")
    field_count = 0

    for boss_name, spawn_info in bosses.items():
        spawn_details = "\n".join([f"**{map_name}**: {spawn_chance}%" for map_name, spawn_chance in spawn_info])
        embed.add_field(
            name=f"__**{boss_name}**__",
            value=spawn_details,
            inline=False
        )
        field_count += 1

        if field_count == 25:
            embeds.append(embed)
            embed = discord.Embed(title="Tarkov Boss Spawn Rates")
            field_count = 0

    if field_count > 0:
        embeds.append(embed)

    return embeds
