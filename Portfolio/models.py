from django.db import models

# Create your models here.
class Project(models.Model):

    title_of_project = models.CharField(max_length=100)
    #   short_description = models.CharField(max_length= 150)
    date_project_started = models.DateField('Date Started')
    date_project_completed = models.DateField('Date Completed', default="Ongoing")
    github_Link = models.URLField()
    about_project = models.TextField()
    date_posted = models.DateTimeField('Date Posted')
    project_id = models.CharField(max_length = 100, help_text="This will be used to map the URLs")

    def __unicode__(self):
        return self.title_of_project

class ProjectScreenshot(models.Model):
    entry = models.ForeignKey(Project, related_name="screenshots")
    image_Name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='documents/')

