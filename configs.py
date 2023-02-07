import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "0"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-100"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1445283714"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
        ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File.I can Work In Channel too Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link.

◽My Name: [File Share Bot](https://t.me/{BOT_USERNAME})

◽Language: [Python3](https://www.python.org)

◽Library: [Pyrogram](https://docs.pyrogram.org)

◽Server: [railway](https://railway.app)

◽Developer: [Ace Knox](https://t.me/aceknox) 

◽Bot Support: [Support](https://t.me/knoxsupport)

◽Bot Updates:[Updates](https://t.me/knoxprojects)


"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 Developer:[Knox](https://t.me/aceknox) 
small engorgement for my works. contact admin
[Donate Me](https://t.me/aceknox) KNOX
"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent File Share Bot.

◽How to Use Bot & it's Benefits??
◽Send me any File & You will Get the File Link.
◽Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
◽Useless contents are strictly prohibited & get Permanent Ban. You know what i meant useless
"""
