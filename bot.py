import os
import re
import telebot
from googleapiclient.discovery import build
from dotenv import load_dotenv
import yt_dlp

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)


def extract_video_id(url):
    patterns = [
        r"(?:youtube\.com\/.*v=|youtu\.be\/)([a-zA-Z0-9_-]{11})",
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def get_video_details(url):
    video_id = extract_video_id(url)
    if not video_id:
        return None

    request = youtube.videos().list(
        part="snippet,contentDetails",
        id=video_id
    )
    response = request.execute()
    if response['items']:
        return response['items'][0]
    return None


def download_audio(video_url):
    video_details = get_video_details(video_url)
    if not video_details:
        return None

    title = video_details['snippet']['title']
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f"{title}.%(ext)s",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    filename = f"{title}.mp3"
    return filename


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Send me a YouTube URL, and I'll download the audio for you.")


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    url = message.text
    if 'youtube.com' in url or 'youtu.be' in url:
        bot.reply_to(message, "Downloading audio, please wait...")
        filename = download_audio(url)

        if filename:
            with open(filename, 'rb') as audio:
                bot.send_audio(message.chat.id, audio)
            os.remove(filename)
        else:
            bot.reply_to(message, "Failed to download audio. Please make sure the URL is valid.")
    else:
        bot.reply_to(message, "Please send a valid YouTube URL.")


if __name__ == '__main__':
    print("Bot is polling...")
    bot.polling()