from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    blog_post = models.TextField()
    posted_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
