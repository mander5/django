from django import forms
from django.core import validators

# manual validator
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("name needs to start with Z")
# use validator=[check_for_z] as a parameter of charfield

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])

    # cleans the entire form for data
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("make sure emails match")

    # maual validator
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("Gotchabot")
    #     return botcatcher
