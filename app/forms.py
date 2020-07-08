from django import forms

class Student(forms.Form):
    name=forms.CharField(max_length=25)
    age=forms.IntegerField(max_value=65,min_value=18)