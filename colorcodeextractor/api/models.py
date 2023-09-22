from django.db import models

class UploadedPhoto(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='image')

    def __str__(self):
        return self.name

