import os, sys
from pathlib import Path
import logging

# logging.basicConfig(level = logging.INFO,format='[%(asctime)]:%(message)s:')
logging.basicConfig(level = logging.INFO,format='[%(asctime)]:%(messages)s:')

project_name = "Predication_Ml"

list_of_files= [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/commmon.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constanats/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py"
    "app.py",
    "requirements.txt"
    "setup.py",
    "research/trails.ipynab",
    "template/index.html"


]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,  filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Created fule dirctory ;{filedir} for the file :{filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")

# setup logging 



