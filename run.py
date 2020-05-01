from redminelib import Redmine
import re
import configparser,os

os.chdir("D:/github_repos/Automate-Redmine")

config = configparser.ConfigParser()
config.readfp(open('settings.ini'))
url = config.get('redmine', 'url')
username = config.get('redmine', 'user')
password = config.get('redmine', 'password')

close_tags = ["Hallo .* Alexander"]

redmine = Redmine(url, username=username, password=password)
project = redmine.project.get('test-ticket')

for issue in project.issues:
    close = False
    print(issue["subject"])
    for tag in close_tags:
        if re.search(tag,issue["subject"]) != None:
            close = True
            print("close")
    if close:
        redmine.issue.update(issue["id"], status_id=2)