# Propital Bot

Propital Bot is a Discord bot that provides various features for the game Escape from Tarkov. It can list ammo calibers, check boss spawn rates, and provide quest details.

## Features

- List ammo calibers
- Check boss spawn rates
- Provide quest details

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/propital-bot.git
    cd propital-bot
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file and add your Discord token and any other necessary environment variables:
    ```env
    DISCORD_TOKEN=your_discord_token
    ```

4. Run the bot:
    ```bash
    python main.py
    ```

## Commands

- `Propital ammo`: Lists all available calibers.
- `Propital boss`: Checks spawn rates for bosses.
- `Propital quest [quest_name]`: Provides information about a quest.
- `Propital help`: Displays the help message.

## Contributing

Feel free to submit issues or pull requests if you find any bugs or have suggestions for new features.

## License

This project is licensed under the MIT License.
