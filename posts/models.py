from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=160)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()

    def __str__(self):
        return self.title

    def pretty_pub_date(self):
        return self.pub_date.strftime(' %d %b %Y ')

    def summary_body(self):
        return self.body[:100]
