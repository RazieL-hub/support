from django.db import models
from django.utils.translation import gettext_lazy as _


class AbsModel(models.Model):
    class Meta:
        abstract = True

    date_creation = models.DateTimeField(verbose_name=_('Date created'), auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name=_('Date updated'), auto_now=True)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()
