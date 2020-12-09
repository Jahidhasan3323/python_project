from django import forms
from django.forms import ModelForm
from .models import *


class HostelTypeForm(forms.ModelForm):
    class Meta:
        model = HostelType
        fields ='__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows' : 5}),
        }


class HostelForm(forms.ModelForm):
    class Meta:
        model= Hostel
        fields='__all__'
        widgets = {
            'address': forms.Textarea(attrs={'rows' : 5}),
            'history': forms.Textarea(attrs={'rows' : 5}),
            'description': forms.Textarea(attrs={'rows' : 5}),
        }


class RoomTypeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RoomTypeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'
    class Meta:
        model= RoomType
        fields='__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows' : 5}),
        }

class RoomForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'
    class Meta:
        model= Room
        fields='__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows' : 5}),
        }

class DesignationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DesignationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'
    class Meta:
        model= Designation
        fields='__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows' : 5}),
        }

