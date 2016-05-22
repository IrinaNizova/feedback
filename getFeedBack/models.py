from django.db import models
from django.core.exceptions import ValidationError

class FeedbackMessage(models.Model):

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=10, blank=True)
    text = models.TextField()
    attach = models.FileField(blank=True)

    def save(self, *args, **kwargs):
        print(self.__dict__)
        if self.attach:
            if (self.attach.name.split('.')[-1].upper()
                  not in ('JPG', 'BMP', 'PNG', 'TIFF')):
                raise(ValidationError(u'Unsupported format'))
            if self.attach.size > 2*1024*1024:
                raise(ValidationError(u'File is very big'))
            elif self.attach.size < 50 * 1024:
                raise(ValidationError(u'File is very small'))
        super(FeedbackMessage, self).save(*args, **kwargs)
