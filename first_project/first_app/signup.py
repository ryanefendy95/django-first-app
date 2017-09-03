from django import forms
from first_app.models import Webpage


class newWebpage(forms.ModelForm):
    class Meta():
        model = Webpage
        fields = '__all__'
