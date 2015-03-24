from django import forms
from django.contrib.auth.models import User
from RMB.models import UserProfile, Images

class UploadImagesForm(forms.ModelForm):

    class Meta:
        model = Images
        fields=('image','img_name','img_cat_id')