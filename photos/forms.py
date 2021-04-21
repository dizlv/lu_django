from django import forms

from photos import models


class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = [
            'picture',
        ]
