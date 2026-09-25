from django import forms

class SettingsForm(forms.Form):
    THEME_CHOICES = [
        ('light', 'Светлая'),
        ('dark', 'Темная'),
    ]
    FONT_CHOICES = [
        ('small', 'Маленький'),
        ('medium', 'Средний'),
        ('large', 'Большой'),
    ]
    
    theme = forms.ChoiceField(choices=THEME_CHOICES, label="Тема оформления")
    font_size = forms.ChoiceField(choices=FONT_CHOICES, label="Размер шрифта")