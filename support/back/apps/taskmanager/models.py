from django.db import models

from django.utils.translation import gettext_lazy as _
from back.core.models import AbsModel


class Category(AbsModel):
    name = models.CharField(_('Название категории'), max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Subcategory(AbsModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Category'))
    name = models.CharField(_('Подкатегория'), max_length=128)

    def __str__(self):
        return f'{self.category} {self.name}'

    class Meta:
        verbose_name = _('Subcategory')
        verbose_name_plural = _('Subcategories')
