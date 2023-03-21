from os import path, getenv
import time
import re
import asyncio
from os import environ as evn
id_pattern = re.compile(r'^.\d+$')

class Config:
    API_ID = int(getenv("API_ID", "15236804"))
    API_HASH = getenv("API_HASH", "409da5b68ad699091fa72b381921f0e5")
    BOT_TOKEN = getenv("BOT_TOKEN", "5692016993:AAHHzEaeekjeF5fXaJZWwyjRgYmvtV7y2l4")
    FSUB = getenv("FSUB", "Matiz_Techz")
    CHID = int(getenv("CHID", "-1001724664296"))
    SUDO = [int(admin) if id_pattern.search(admin) else admin for admin in evn.get('SUDO', '1963114305').split()]
    MONGO_URI = getenv("mongodb+srv://Matin:9x7RlW5MPHgT3NyR@cluster0.ygefm.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
