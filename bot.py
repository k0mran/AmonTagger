import logging
from telethon import TelegramClient
from config import API_HASH, API_ID, BOT_TOKEN

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

LOGGER = logging.getLogger(__name__)

client = TelegramClient("client", api_id=API_ID, api_hash=API_HASH).start(bot_token=BOT_TOKEN)
