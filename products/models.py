from django.db import models
from django.utils.translation import ugettext_lazy as _

class Category(models.Model):
    parent= models.ForeignKey('self',verbose_name=_('parent'),blank=True,null=True,on_delete=models.CASCADE)
    title = models.CharField(_('title'),max_length=50)
    description = models.TextField(_('description'),blank=True)
    avatar = models.ImageField(_('avatar'),blank=True, upload_to='categories/')
    is_enable = models.BooleanField(_('is enable'),default=True)
    created_time = models.DateTimeField(_('created time'),auto_now_add=True)
    update_time= models.DateTimeField(_('updated time'),auto_now=True)
class Meta:
    db_table = _('categories')
    verbose_name= _('category')
    verbose_name_plural = _('category')

class Product(models.Model):
    parent = models.ForeignKey('self', verbose_name=_('parent'), blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='products/')
    category=models.ManyToManyField('category',verbose_name=_('category'),blank=True)
class File (models.Model) :
    pass