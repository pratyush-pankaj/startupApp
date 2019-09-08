#Main executable code
from src.startApp import startApp
import json

if __name__ == '__main__':
    print("Running Startup!")
    filePath = "src/apps.json"
    startapp = startApp(filePath)
    startapp.start()

