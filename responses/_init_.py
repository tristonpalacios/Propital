from responses.calibers import list_calibers
from responses.bosses import check_bosses
from responses.quest import get_quest_id
from responses.help import get_help

async def get_response(user_input: str):
    lowered: str = user_input.lower()

    if not lowered.startswith('propital'):
        return

    # Extract the relevant part of the user input after 'propital'
    command = lowered[len('propital'):].strip()

    if 'ammo' in command:
        return await list_calibers()
    elif 'boss' in command:
        return await check_bosses()
    elif 'quest' in command:
        quest_name = command.split('quest', 1)[1].strip()
        return await get_quest_id(quest_name)
    elif 'help' in command:
        return get_help()
    elif 'scav' in command:
        return "Давай,мочи их"
    else:
        return 'I do not understand. Please use "Propital help" for a list of commands.'
