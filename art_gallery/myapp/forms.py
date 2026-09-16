from django import forms

class SettingsForm(forms.Form):
    THEME_CHOICES = [
        ('light', 'Светлая'),
        ('dark', 'Темная'),
    ]
    LANGUAGE_CHOICES = [
        ('ru', 'Русский'),
        ('en', 'English'),
    ]
    
    theme = forms.ChoiceField(choices=THEME_CHOICES, label="Тема оформления")
    language = forms.ChoiceField(choices=LANGUAGE_CHOICES, label="Язык интерфейса")