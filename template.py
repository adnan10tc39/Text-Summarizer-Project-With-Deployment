import os
from pathlib import Path
import logging #for logs creation 

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:, %(message)s:') #basicConfig(level=information related logging karny lagy hain,format='yahan per hum apni file ka formate define karien gy ya aur list k ander time name etc define karien gy.)


project_name = "textSummarizer"

list_of_files = [ #is k ander hum apny project ki files and folder define karien gy.

        ".github/workflows/.gitkeep",
        f"src/{project_name}/__init__.py",
        f"src/{project_name}/components/__init__.py",
        f"src/{project_name}/utils/__init__.py",
        f"src/{project_name}/utils/comman.py",
        f"src/{project_name}/logging/__init__.py",
        f"src/{project_name}/config/__init__.py",
        f"src/{project_name}/config/configuration.py",
        f"src/{project_name}/pipeline/__init__.py",
        f"src/{project_name}/entity/__init__.py",
        f"src/{project_name}/constants/__init__.py",
        "config/config.yaml",
        "params.yaml", #it contains model related parametes
        "app.py",
        "main.py",
        "Dockerfile",
        "requirements.txt",
        "setup.py",
        "research/trails.ipynb",
]

#write the login to create these files and folders

#========================folder creation start =========================
for filepath in list_of_files:
    filepath= Path(filepath) #we convert our path into our specific operating system path. ye Path ki library khud he handle kar laiti hai.in linux we have forward slash while in windows we have backword slash so to handle these thing we use path loibrary
    #filepath give us a file path one by one
    #first of all we create folder than inside these folders we will create file 
    filedir, filename = os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir, exist_ok=True) 
        logging.info(f"creating directory {filedir} for the file {filename}")
#========================folder creation end =========================

#========================file creation start =========================
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): #filepath say file name ko get kar lay ga
            with open(filepath,'w') as f:
                pass
                logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")
#========================file creation start =========================

        
'''
.github folder deployment k hisab say bohat important hain .jab kabi hum git hub per apna code comment karien gy ya koe 
modified karien gy tu ye .github he responsible ho ga cloud ya aws per update karny k liay.ye auto per wahan per b 
update kar day ga.
ye .gitkeep jab hum files ko comment karien gy tu empty folder update ho jay ga tu us k bachny k liay hum .gitkeep 
use karty hain jo k hidden file ko upload kar daita hai bad mien hum delete kar daity hain jab hum apni actual ymal
file create kar laity hain.
2nd hum src ka folder bnay gy aur us k ander ak apny project ka folder bnaien gy aur us k ander constructer file
create karien gy.

'''
#koe b new file create karni hai tu list_of_files mien add kar dien aur pher ise file ko run karien gy tu wo file or folder create ho jay ga.






































































