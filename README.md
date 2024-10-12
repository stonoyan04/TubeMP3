# YouTube MP3 Telegram Bot

A Telegram bot that allows users to download audio from YouTube videos as MP3 files. Users simply send a YouTube URL, and the bot will process it and return the audio file.

## Features
- Accepts YouTube URLs.
- Downloads the audio in MP3 format.
- Sends the MP3 file back to the user on Telegram.

## Tech Stack
- Python
- Telegram Bot API (`pyTelegramBotAPI` / `telebot`)
- YouTube Data API v3 (`google-api-python-client`)
- `yt-dlp` for downloading audio
- `FFmpeg` for audio conversion

## Prerequisites
- Python 3.7+
- A Telegram bot token from [BotFather](https://t.me/botfather).
- A YouTube Data API v3 key from [Google Developer Console](https://console.developers.google.com).
- `FFmpeg` installed and available in your system PATH.

## Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/stonoyan04/TubeMP3.git
   cd TubeMP3
   ```

2. **Create a Virtual Environment**
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. ***Create a `.env` file in the root directory and add the following:***
   ```env
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
   YOUTUBE_API_KEY=your_youtube_api_key_here
   ```

5. **Install FFmpeg**
   - **macOS**: Install using Homebrew
     ```sh
     brew install ffmpeg
     ```
   - **Windows**: Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html) and add it to your system PATH.

## Running the Bot
To start the bot, run:
```sh
python bot.py
```
The bot will start polling for messages.

## Usage
- Send a YouTube URL to the bot on Telegram [@tube_mp3bot](https://t.me/tube_mp3bot).
- The bot will download the audio and send it back as an MP3 file.

## Dependencies
- `pyTelegramBotAPI`
- `google-api-python-client`
- `python-dotenv`
- `yt-dlp`
- `requests`

## License
This project is licensed under the MIT License.

## Contributing
Feel free to open issues or submit pull requests for improvements or bug fixes.

## Disclaimer
This bot is intended for personal use only. Downloading copyrighted content may violate YouTube's Terms of Service. Use responsibly.