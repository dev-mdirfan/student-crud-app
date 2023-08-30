from django import forms
from .models import User, STATE_CHOICES, GENDER_CHOICES

# sorting the state choices - not working
# STATE_CHOICES = sorted(STATE_CHOICES, key=lambda x: x[1])

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'password': forms.PasswordInput(render_value = True, attrs={'class': 'form-control', 'placeholder': 'Enter Password'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter City'}),
            'state': forms.Select(attrs={'class': 'form-select'}, choices = STATE_CHOICES),
            'gender': forms.RadioSelect(choices = GENDER_CHOICES)
        }
    
    def __init__(self, *args, **kwargs):
        '''
        overriding the init method to change the order of the state choices
        '''
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['state'].choices = sorted(self.fields['state'].choices, key=lambda x: x[1])

