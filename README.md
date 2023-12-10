# DisnakeMemelords

Disnake discord bot for personal discord server.

This project is a refactor/migration process from [MemelordsBot](https://github.com/Extrieve/MemelordsBot), moving this project from discord.py to Disnake to leverage new features such as slash_commands.

## Major Bot Functionality

- **Anime**: Search for anime and get information about it, including openings, endings, and more.
- **Search**: Search for images, word definitions, and more.
- **Fun**: Get random images, quotes, and more.
- **General Purpose**: Retrieve server information, generate random images, and more.
- **Admin**: Access server information, moderate the server, and more.

## Database and Libraries

The bots' databases were achieved using scraping libraries like Selenium and BeautifulSoup.

## Development Status

A lot of the bot functionality is still under development. TODO: Add music functionality.

## Setup and Configuration

Before running the application, ensure you have:

- A Discord account and a bot account.
- The correct permissions to run the bot.
- Your bot token configured in the `config.py` file (this is gitignored for security concerns).

## Running the Application

To run the application locally, execute the following command:

```python
python3 bot.py
