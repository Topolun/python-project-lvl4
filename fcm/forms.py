from django import forms
from fcm.models import rack


class RackForm(forms.ModelForm):

    class Meta:
        model = rack
        fields = '__all__'
    

class GetItem(forms.Form):
    your_id = forms.IntegerField(label='Your id number')
