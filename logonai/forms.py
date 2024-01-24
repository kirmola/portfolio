from django import forms

class LogonForm(forms.Form):
    prompt = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            "placeholder":"Tell Logon about your idea..",
            "class":"rounded-full w-full md:text-3xl text-center"
        }
    ))
