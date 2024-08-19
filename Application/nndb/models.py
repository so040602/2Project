from django.db import models

# Create your models here.
class NaverNews(models.Model):
    count = models.IntegerField(primary_key=True)
    title = models.TextField()
    section = models.TextField()
    link = models.TextField()
    pDate = models.FloatField()
    description = models.TextField()
    img_link = models.TextField()
    text = models.TextField()

    class Meta:
        db_table = 'nNews'

    def __str__(self):
        return self.title