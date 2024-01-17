from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from tool.models import DevTool

# Create your models here.
class Idea(models.Model):
    title = models.CharField('아이디어명', max_length=255)
    content = models.TextField('아이디어 설명', max_length=5000)
    image = models.ImageField('이미지', blank=True, upload_to='idea/')
    interest = models.IntegerField('아이디어 관심도', default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    pick = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    devtool = models.ForeignKey(DevTool, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
