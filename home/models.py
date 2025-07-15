from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name='Banner Title')
    image = models.ImageField(upload_to='banners/', verbose_name='Banner Image')
    link = models.URLField(max_length=200, verbose_name='Link URL')
    order = models.PositiveIntegerField(default=0, verbose_name='Display Order')

    class Meta:
        ordering = ['order']
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

    def __str__(self):
        return self.title