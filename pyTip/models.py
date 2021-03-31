from django.db import models

# Create your models here.


class PyTip(models.Model):
    tweet_id = models.CharField(max_length=500, null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    tweet_text = models.CharField(max_length=500, null=True, blank=True)
    tweet_link = models.CharField(max_length=500, null=True, blank=True)
    external_url = models.CharField(max_length=5000, null=True, blank=True)
    posted_by = models.CharField(max_length=200, null=True, blank=True)
    like = models.IntegerField(null=True, blank=True)
    retweet = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.tweet_id
