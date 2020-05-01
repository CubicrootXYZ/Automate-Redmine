from redminelib import Redmine
import re



close_tags = ["Hallo .* Alexander"]

redmine = Redmine(url, username=admin, password=password)
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