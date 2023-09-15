from django import forms

class EmailForm(forms.Form):
    to_email = forms.EmailField(label='Para')
    subject = forms.CharField(max_length=100, label='Asunto')
    message = forms.CharField(widget=forms.Textarea, label='Mensaje')
    recipient_email = forms.EmailField(label='Tu correo electrónico')