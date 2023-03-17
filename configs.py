from os import path, getenv
import time
import re
import asyncio
from os import environ as evn
id_pattern = re.compile(r'^.\d+$')

class Config:
    API_ID = int(getenv("API_ID", "26756378"))
    API_HASH = getenv("API_HASH", "28f615585ac59b2ec39e5fe828de21a0")
    BOT_TOKEN = getenv("BOT_TOKEN", "6059695462:AAHHGQk0mQj-Q06Yt7_8yoiBejI-HwCN90k")
    FSUB = getenv("FSUB", "beta_botz")
    CHID = int(getenv("CHID", "-1001858865209"))
    SUDO = [int(admin) if id_pattern.search(admin) else admin for admin in evn.get('SUDO', '5558249587').split()]
    MONGO_URI = getenv("mongodb+srv://accept:accept@uster0.b3l2v1d.mongodb.net/?retryWrites=true&w=majority", "")
    
cfg = Config()
