#Run selected Application
import os
import subprocess
import json

class startApp():
    def __init__(self, apps):
        self.apps = apps

    def start(self):
        with open(self.apps) as app:
            appsList = json.load(app)
            for a in appsList:
                print("Starting %s" %a['app'])
                try:
                    os.popen(a['path'])
                except Exception as e:
                    print("ERROR: %s" %e)
                    return
