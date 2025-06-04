from django import forms

class GuessForm(forms.Form):
    guess = forms.IntegerField(
        label='Your Guess',
        min_value=1,
        max_value=100,
        widget=forms.NumberInput(attrs={'placeholder': 'Enter a number (1-100)'})
    )
