from __future__ import unicode_literals

from django.db import models
from django.conf import settings
# Create your models here.

class Articles(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=50)
    content = models.TextField()
    is_active = models.BooleanField(default=True)
    publish = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __unicode__(self):
        return self.title
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-timestamp", "-updated"]