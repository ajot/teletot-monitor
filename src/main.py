import logging
import os
import uuid
import asyncio
import pyaudio
import wave
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def create_download_path(extension):
    """
    Create a unique file path in the 'downloads' directory with the given file extension.
    """
    cwd = os.getcwd()
    downloads_dir = os.path.join(cwd, 'downloads')
    if not os.path.exists(downloads_dir):
        os.makedirs(downloads_dir)
    unique_filename = f"{uuid.uuid4()}.{extension}"
    return os.path.join(downloads_dir, unique_filename)

async def record_audio_async(duration=10):
    """
    Record audio for a given duration (in seconds) and return the path to the recorded file.
    """
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = duration

    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    logger.info("Recording started")
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()
    logger.info("Recording stopped")

    path = create_download_path('wav')
    with wave.open(path, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    return path

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Send a welcome message when the /start command is used.
    """
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome! I'm TeleTot. Use /record to record a 10-second audio clip.")

async def record(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Record a 10-second audio clip and send it to the user in response to the /record command.
    """
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Recording a 10-second audio clip...")
    filename = await record_audio_async(10)
    await context.bot.send_audio(chat_id=update.effective_chat.id, audio=open(filename, 'rb'))

if __name__ == '__main__':
    # Initialize the bot with the API token from the configuration file
    from config import TELEGRAM_API_TOKEN
    application = ApplicationBuilder().token(TELEGRAM_API_TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('record', record))

    # Start the bot
    application.run_polling()
