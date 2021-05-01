from django.db import models
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from transliterate import translit
from textblob import TextBlob
from datetime import datetime

from django.template.defaultfilters import slugify

def slugify_title(content):
    content = content.replace(' ', '-')
    if TextBlob(content).detect_language() != 'en':
        content = translit(content, reversed=True)
    final_content = content.replace("'", "")
    while Publications.objects.filter(slug=final_content).count() != 0:
        n = 1
        final_content = content + str(n)
        n += 1
    return final_content


class Publications(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name='Название')
    content = models.TextField(verbose_name='Контент')
    created_time = models.DateTimeField(auto_now=True, verbose_name='Время создания')
    slug = AutoSlugField(populate_from='title', slugify_function=slugify_title, null=True, max_length=100)

    def get_absolute_url(self):
        return reverse("SinglePublication", kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-created_time']