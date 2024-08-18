# Discord Radio Bot

This is a simple Discord bot built with Python that plays radio streams in voice channels. The bot allows users to play and stop a radio stream directly from Discord voice channels using slash commands.

## Features

- **Play Radio**: Plays an underground bass radio stream in your voice channel.
- **Stop Radio**: Stops the radio stream and disconnects the bot from the voice channel.
- **Bot Greetings**: The bot greets users who mention it in any text channel.

## Installation

### Prerequisites

- Python 3.8 or higher
- Discord.py library
- FFmpeg (required for audio streaming)

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/discord-python-radio.git
   cd discord-python-radio
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Replace the placeholder in `radio.py` with your Discord bot token:

   ```python
   bot.run('YOUR DISCORD DEV API KEY HERE')
   ```

4. Make sure you have FFmpeg installed on your system. You can download it from [here](https://ffmpeg.org/download.html).

## Usage

1. Run the bot:

   ```bash
   python radio.py
   ```

2. Invite the bot to your Discord server using the OAuth2 URL with the necessary permissions.

3. Use the following commands in your Discord server:

   - `/play`: Plays the radio stream in the voice channel you are currently in.
   - `/stop`: Stops the radio stream and disconnects the bot from the voice channel.

## Configuration

- The bot uses a static radio stream URL. You can change the stream by modifying the `audio_source` line in the `play` command function in `radio.py`.

## Troubleshooting

- Ensure that the bot has the necessary permissions to connect to and speak in voice channels.
- Make sure that FFmpeg is installed and properly configured in your system’s PATH.
- Double-check that you have correctly set your bot token in the script.

## Contributing

If you would like to contribute to this project, feel free to submit a pull request or open an issue on the GitHub repository.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
