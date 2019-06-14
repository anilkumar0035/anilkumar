from django import forms
class FeedbackForm(forms.Form):
    name=forms.CharField(
        label='enter the name',
        widget=forms.TextInput(
            attrs={
                'placeholder':'enter the name',
                'class':'form-control'
            }
        )
    )
    rating=forms.IntegerField(
        label='enter rating',
        widget=forms.NumberInput(
            attrs={
                'placeholder':'rating',
                'class':'form-control'
            }
        )
    )
    feedback=forms.CharField(
        label='enter the feedback',
        widget=forms.TextInput(
            attrs={
                'placeholder':'feedback',
                'class':'form-control'
            }
        )
    )