from os import path, getenv

from dotenv import load_dotenv

dotenv_path = path.join(path.dirname(__file__), '.env')
if path.exists(dotenv_path):
    load_dotenv(dotenv_path)

NAME = getenv("NAME")
