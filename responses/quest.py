from utils.request_utils import tarkov_api_request
import discord

async def get_quest_id(quest_name: str):
    query = '''
    {
      tasks {
        id
        name
      }
    }
    '''
    data = await tarkov_api_request(query)
    tasks = data.get('data', {}).get('tasks', [])
    for task in tasks:
        if task['name'].lower() == quest_name.lower():
            task_id = task['id']
            return await get_quest_info(task_id)
    return discord.Embed(title="Quest Not Found", description=f"Could not find quest named '{quest_name}'.")

async def get_quest_info(task_id: str):
    query = f'''
    {{
      task(id: "{task_id}") {{
        name
        objectives {{
          description
        }}
        wikiLink
      }}
    }}
    '''
    data = await tarkov_api_request(query)
    task = data.get('data', {}).get('task', {})
    if task:
        name = task['name']
        objectives = task['objectives']
        wiki_link = task['wikiLink']
        objectives_list = "\n".join([f"- {obj['description']}" for obj in objectives])
        embed = discord.Embed(title=f"Quest Details: {name}", url=wiki_link)
        embed.add_field(name="Objectives", value=objectives_list, inline=False)
        embed.add_field(name="Wiki Link", value=f"[Link]({wiki_link})", inline=False)
        return embed
    else:
        return discord.Embed(title="Quest Not Found", description=f"Could not find quest details for ID '{task_id}'.")

