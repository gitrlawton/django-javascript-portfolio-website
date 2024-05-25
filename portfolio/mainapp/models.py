from django.db import models

### Create your models here. ###

# A Tag to associate projects with.
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

# A Programming Project.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # ManyToMany because many tags/projects can be associated with many 
    # tags/projects.
    tags = models.ManyToManyField(Tag, related_name="projects")
    link = models.URLField(max_length=200, blank=True)
    
    def __str__(self):
        return self.title

# An image previewing a project.
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name="images", 
                                on_delete=models.CASCADE) # deletes all the images associated with the project.
    # Where we want to store the images within our media directory.
    image = models.ImageField(upload_to="project_images/")
    
    def __str__(self):
        return f"{self.project.title} Image"
    