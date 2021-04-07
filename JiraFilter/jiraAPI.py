from requests import get
import json

user = 'user'
passwd = 'pass'

class Issue:
  def __init__(self, key, reporter, assignee, summary, updated, status):
    self.key = key
    self.reporter = reporter
    self.assignee = assignee    
    self.summary = summary    
    self.updated = updated    
    self.status = status    
  
def getIssues_byDateRange_byProject(project, startdate, enddate, maxResults):
    response = get('https://orw-ams-tools-02.wv.mentorg.com/jira/rest/api/2/search?jql=project = ' + project  + ' AND createdDate >= "' + startdate + '" AND createdDate <= "' + enddate + '"&maxResults=' + maxResults + '&fields=issues,status,reporter,assignee,updated,summary', auth=(user, passwd))
    resJson = json.loads(response.text)
    issuesList = []
    for issue in resJson["issues"]:
        key = issue["key"]
        reporter = issue["fields"]["reporter"]["displayName"] 
        if issue["fields"]["assignee"]:
            assignee = issue["fields"]["assignee"]["displayName"] 
        else:
            assignee = ''    
        summary = issue["fields"]["summary"]
        status = issue["fields"]["status"]["name"]
        updated = issue["fields"]["updated"]
        newIssue = Issue(key, reporter, assignee, summary, updated, status)
        issuesList.append(newIssue)
    return issuesList



def getAllProjects():
    response = get("https://orw-ams-tools-02.wv.mentorg.com/jira/rest/api/2/project", auth=(user, passwd))
    resJson = json.loads(response.text)
    projectList = []
    for project in resJson:
        key  = project["key"]
        name = project["name"]
        projectList.append((key, name))
    return projectList    
