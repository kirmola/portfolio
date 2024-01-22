from django import forms

LANGUAGE_STYLES = (
    ("formal", "Formal"),
    ("informal", "Informal"),
    ("technical", "Technical"),
    ("literary", "Literary"),
    ("Persuasive", "Persuasive"),
    ("academic", "Academic"),
    ("humorous", "Humorous"),
    ("satiristic", "Satiristic"),
)

MOODS_STYLE = (
    ("happy" ,"Happy"),
    ("sad" ,"Sad"),
    ("angry" ,"Angry"),
    ("excited" ,"Excited"),
    ("calm" ,"Calm"),
    ("stressed" ,"Stressed"),
    ("relaxed" ,"Relaxed"),
    ("energetic" ,"Energetic"),
    ("anxious" ,"Anxious"),
    ("melancholic" ,"Melancholic"),
)


class PersonalityForm(forms.Form):
    query = forms.CharField(max_length="200", required=True, widget=forms.TextInput(attrs={
        "placeholder": "Ask Moody about anything!",
        "class":"rounded-full w-full md:text-3xl text-center"
        
    }))
    language_style = forms.ChoiceField(choices=LANGUAGE_STYLES, required=True, widget=forms.Select(attrs={
        "class":"rounded-full md:text-2xl w-full"
    }))   
    mood_style = forms.ChoiceField(choices=MOODS_STYLE, required=True, widget=forms.Select(attrs={
        "class":"rounded-full md:text-2xl w-full"
    }))