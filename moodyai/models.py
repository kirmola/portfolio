from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
# Create your models here.

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


class AI_Tuner(models.Model):

    mood = models.CharField(_("Mood of AI"), max_length=50)
    language_style = models.CharField(_("Language Style"), choices=LANGUAGE_STYLES, max_length=50)
    


    class Meta:
        verbose_name = _("AI_Tuner")
        verbose_name_plural = _("AI_Tuners")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("AI_Tuner_detail", kwargs={"pk": self.pk})
