from django.db import models
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from transliterate import translit
from textblob import TextBlob

from django.template.defaultfilters import slugify

def slugify_transliterate(content):
    print(TextBlob(content).detect_language())
    if TextBlob(content).detect_language() == 'en':
        return content.replace(' ', '-')
    return translit(content.replace(' ', '-'), reversed=True)

class Publications(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name='Название')
    content = models.TextField(verbose_name='Контент')
    created_time = models.DateTimeField(auto_now=True, verbose_name='Время создания')
    slug = AutoSlugField(populate_from='title', slugify_function=slugify_transliterate, null=True, max_length=100)

    def get_absolute_url(self):
        return reverse("SinglePublication", kwargs={'slug': self.slug})

    # def

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-created_time']