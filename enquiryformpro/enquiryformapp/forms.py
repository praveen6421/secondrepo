from django import forms

class EnquiryForm(forms.Form):
    firstname = forms.CharField(
        label= "First Name",
        widget=forms.TextInput(
            attrs={
                'placeholder':'Your First Name',
                'class':'form-control'
            }
        )
    )
    lastname = forms.CharField(
        label="Last Name",
        widget=forms.TextInput(
            attrs={
                'placeholder':'Your Last Name',
                'class':'form-control'
            }
        )
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                'placeholder':'Your Email',
                'class':'form-control'

            }

        )
    )
    mobile = forms.IntegerField(
        label="Mobile",
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Your Mobile',
                'class':'form-control'
            }
        )
    )
    qualification = forms.CharField(
        label='Qualification',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Your Qualification',
                'class':'form-control'
            }
        )
    )
    location = forms.CharField(
        label='Location',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your Location',
                'class': 'form-control'
            }
        )
    )
