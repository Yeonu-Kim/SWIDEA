from django.db import models

# Create your models here.
class DevTool(models.Model):
    name = models.CharField('이름', max_length=255)
    type = models.CharField('종류', max_length=255)
    desc = models.TextField('개발툴 설명', max_length=5000)

    def __str__(self):
        return self.name