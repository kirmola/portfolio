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
    query = forms.CharField( max_length="200", required=True)
    language_style = forms.ChoiceField(choices=LANGUAGE_STYLES, required=True)   
    mood_style = forms.ChoiceField(choices=MOODS_STYLE, required=True)
