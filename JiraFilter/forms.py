import datetime
from django import forms
from . import jiraAPI
#DataFlair #Form
class QueryIssues(forms.Form):
    Start_Date = forms.DateField(required = True, initial = datetime.date.today , widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    End_Date = forms.DateField(required = True, initial = datetime.date.today, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    Project = forms.CharField(widget=forms.Select(choices=jiraAPI.getAllProjects()))
    Max_Result = forms.IntegerField(required = True ,initial=10)
