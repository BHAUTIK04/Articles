from __future__ import unicode_literals

from django.db import models
from Articles.models import Articles
from django.conf import settings
# Create your models here.


class Comment(models.Model):
    articles = models.ForeignKey(Articles)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    comment_text = models.TextField()
    timestamp = models.DateTimeField(auto_now = True, auto_now_add = False)
    
    class Meta:
        ordering = ['-timestamp']
        
    def __unicode__(self):
        return self.comment_text
    
    def __str__(self):
        return self.comment_text