from django.db import models


class Meme(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to='pics')
    pub_date = models.DateField(auto_now_add=True)
    credit = models.CharField(max_length=60)

    def __str__(self):
        return self.name
