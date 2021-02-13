from django import forms
from .models import MyModel

class MyForm(forms.ModelForm):


    class Meta:

        #Defining the form attributes
        model = MyModel
        fields = ["fullname", "email", "mobile_number",]
        labels = {'fullname: "Name", "email": "Email "mobile_number": "Mobile Number"',}