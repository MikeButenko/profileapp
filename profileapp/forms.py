from django import forms
from django.http import request
from profileapp.models import Profile
from django.forms.extras.widgets import SelectDateWidget


BIRTH_YEAR_CHOICES = [i for i in range(1900, 2018, 1)]


class UserEditProfile(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    date_of_birth = forms.DateField(widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    biography = forms.Textarea()
    contacts = forms.CharField()

    def __init__(self, *args, **kw):
        super(UserEditProfile, self).__init__(*args, **kw)
        self.fields['first_name'].initial = self.instance.first_name
        self.fields['last_name'].initial = self.instance.last_name
        self.fields['date_of_birth'].initial = self.instance.date_of_birth
        self.fields['biography'].initial = self.instance.biography
        self.fields['contacts'].initial = self.instance.contacts

        self.fields.keyOrder = [
            'first_name',
            'last_name',
            'date_of_birth',
            'biography',
            'contacts'
        ]

    def save(self, *args, **kw):
        super(UserEditProfile, self).save(*args, **kw)
        self.instance.first_name = self.cleaned_data.get('first_name')
        self.instance.last_name = self.cleaned_data.get('last_name')
        self.instance.date_of_birth = self.cleaned_data.get('date_of_birth')
        self.instance.biography = self.cleaned_data.get('biography')
        self.instance.contacts = self.cleaned_data.get('contacts')
        self.instance.save()

    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
            'date_of_birth',
            'biography',
            'contacts'
        )
        exclude = ['user', 'ip_address']
