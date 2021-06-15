from os import path
from pathlib import Path
from yaml import load, FullLoader

ROOT_PATH = Path(path.abspath(__file__)).parent.parent
# dotenv_path = path.join(ROOT_PATH, '.env')
# if path.exists(dotenv_path):
#     load_dotenv(dotenv_path)


def read_config(filepath):
    with open(filepath) as f:
        return load(f, Loader=FullLoader)


CONFIG_PATH = path.join(ROOT_PATH, 'config/config.yml')
config = read_config(CONFIG_PATH)
name = config["name"]
