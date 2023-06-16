from django import forms

from .models import Bid

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ('text', 'device', 'image')

    def __init__(self, *args, **kwargs):
        super(BidForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs['placeholder'] = (
            'Введите текст 🐱‍💻'
        )
        self.fields['device'].empty_label = (
            '(‾◡◝)'
        )

