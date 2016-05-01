from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=255)


class Snippet(models.Model):
    code = models.TextField()
    caption = models.CharField(max_length=255)
    lang = models.ForeignKey(Language, on_delete=models.PROTECT)
