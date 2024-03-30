import importlib
import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    app_api = importlib.import_module("chatmaster")
    app_api.run()