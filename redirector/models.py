from django.db import models

class Redirection(models.Model):
    "Redirect an inbound http request to the target"
    source_name = models.CharField(max_length=255, unique=True)
    destination_url = models.CharField(max_length=255)
    count = models.IntegerField(default=0)
    enabled = models.BooleanField(default=True)

    def get_url(self):
        if self.destination_url.startswith('http://'):
            return self.destination_url
        if self.destination_url.startswith('https://'):
            return self.destination_url
        return "http://%s" % self.destination_url

    def __str__(self):
        return "%s -> %s" % (self.source_name, self.get_url())

class MissDirection(models.Model):
    source_name = models.CharField(max_length=255, unique=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return "%s MISS %d" % (self.source_name, self.count)
    
