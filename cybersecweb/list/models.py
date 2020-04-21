from django.db import models
from django.urls import reverse

# Create your models here.

class EC2Instance(models.Model):
    # Fields
    instance_id = models.CharField(max_length=30, help_text='EC2 Instace unique ID')

    role = models.CharField(max_length=10, help_text='EC2 Instace role label')

    # # Metadata
    # class Meta:
    #     ordering = ['-instance_id']

    def __str__(self):
        return self.instance_id

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])