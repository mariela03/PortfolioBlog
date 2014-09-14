from django.db import models

# Create your models here.

class Me(models.Model):
    name = models.CharField(max_length=100)
    about_me = models.TextField()
    linkedin_link = models.URLField()
    github_link = models.URLField()
    twitter_link = models.URLField()
    profile_photo = models.ImageField(upload_to="about_me/")
    def __unicode__(self):
        return self.name

class Interests(models.Model):
    entry = models.ForeignKey(Me, related_name='photots')
    image = models.ImageField(upload_to='about_me/')
