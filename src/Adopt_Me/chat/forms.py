from django.forms import ModelForm
from .models import DirectMessages

class SendMessage(ModelForm):
    class Meta:
        model = DirectMessages
        exclude = ['sender', 'receiver', 'time', 'date']