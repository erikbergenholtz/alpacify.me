from django import forms

class UploadImageForm(forms.Form):
    img = forms.FileField()

class ShareFluffForm(forms.Form):
    img = forms.HiddenInput()
    conscent = forms.BooleanField(required=True)
