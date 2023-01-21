import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5820073046:AAF5pXdO333nkK8KVjzXNQSTpgjsJTjnPoY")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQBylaS31dBMNWABt_-plJ3Rb54AtTpq5JWCUZ0MvmPeogebg-hv0cSmGHbD0l46Oy2aIpUyeitDew93nWAHZ3jGgE_oH4rzVUSytywBVi19KpJS7tglb49FNmdmzj5xBymrUEvAQUrIMAN5-vIvvpbKj1srWofiuNeaBxGD_8XQlagtDruxj9YVHuL3YwFESkHPrCzEG0VxJys4pOy3YCq9uniYPLIVhAmNQPtQl2fR3lx6ZEU4vGiZdJZ6ZzXqKcyfdhuJaEpXBQmHaOF8LeDI7her8eEqqTduYZvQKK1Ccsb7q7LnLWTjWZBIJuHdwnTooiZjRTS9n5GYrOBgW5SFAAAAAWFsnJgA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Vc_Xr_Bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5929475224")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
