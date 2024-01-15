from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from autoslug import AutoSlugField
# Create your models here.


class Logo_Category(models.Model):

    category_name = models.CharField(_("Category Name"), max_length=50)
    category_slug = AutoSlugField(populate_from="category_name", primary_key=True)

    class Meta:
        verbose_name = _("Logo Category")
        verbose_name_plural = _("Logo Categories")

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse("Logo_Category_detail", kwargs={"pk": self.pk})


