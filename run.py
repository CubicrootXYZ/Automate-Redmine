from redminelib import Redmine
import re
import configparser,os,datetime,json
import closer as close
import telegrambot
from datetime import timedelta as td

os.chdir("/opt/app")

class AutomateRedmine:
    def __init__(self):
        self.getConfig()

    def getConfig(self):
        config = configparser.ConfigParser()
        config.readfp(open('settings.ini'))

        self.host = config.get('redmine', 'url')
        self.user = config.get('redmine', 'user')
        self.password = config.get('redmine', 'password')

        self.closer = {}
        self.closer["list_spam"] = json.loads(config.get('closer', 'spam_list'))
        self.closer["list_close"] = json.loads(config.get('closer', 'close_list'))
        self.closer["projects"] = json.loads(config.get('closer', 'projects'))
        self.closer["id_spam"] = config.get('closer', 'spam_id')
        self.closer["id_close"] = config.get('closer', 'close_id')

    def run(self):
        lastrun_closer = datetime.datetime.now()-td(days=10)
        
        while True:
            now = datetime.datetime.now()

            if now - lastrun_closer > td(minutes=10):
                print("run")
                lastrun_closer = datetime.datetime.now()
                self.runCloser()

    
    def runCloser(self):
        closer = close.Closer(self.host, self.user, self.password, self.closer["id_close"], self.closer["id_spam"])
        closer.setSpam(self.closer["list_spam"])
        closer.setClose(self.closer["list_close"])
        closer.setProjects(self.closer["projects"])
        closer.run()

run = AutomateRedmine()
run.run()