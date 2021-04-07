from django.shortcuts import render
from . import forms
from . import jiraAPI

#DataFlair #Form #View Functions
def queryForm(request):
    myform = forms.QueryIssues()
    if request.method == 'POST':
        myform = forms.QueryIssues(request.POST)
        if myform.is_valid():
            start = str(myform.cleaned_data['Start_Date'])
            end = str(myform.cleaned_data['End_Date'])
            project = myform.cleaned_data['Project']
            maxResults = str(myform.cleaned_data['Max_Result'])
            issuesData = jiraAPI.getIssues_byDateRange_byProject(project, start, end, maxResults)
    else:
        issuesData = []
    return render(request, 'QueryData.html', {'issues': issuesData, 'form': myform})