from redminelib import Redmine
import re

class Closer:
    def __init__(self, host, user, password, close_id, spam_id):
        self.rm = Redmine(host, username=user, password=password)
        self.list_close = []
        self.list_spam = []
        self.projects = []
        self.close_id=close_id
        self.spam_id=spam_id

    def setSpam(self, spam):
        self.list_spam=spam

    def setClose(self, close):
        self.list_close=close

    def setProjects(self, projects):
        self.projects=projects

    def run(self):
        for project_name in self.projects:
            try:
                project = self.rm.project.get(project_name)
            except Exception as e:
                print(e)
                continue

            for issue in project.issues:
                close = False
                spam = False

                for tag in self.list_close:
                    
                    if re.search(tag,issue["subject"]) != None:
                        close = True
                        print(int(self.close_id))
                for tag in self.list_spam:
                    if re.search(tag,issue["subject"]) != None:
                        spam = True

                if close and not spam: 
                    self.rm.issue.update(issue["id"], status_id=int(self.close_id))
                if spam: 
                    self.rm.issue.update(issue["id"], status_id=int(self.spam_id))