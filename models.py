from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    last_update = models.DateTimeField(db_index=True, auto_now=True)
    is_starred = models.BooleanField(default=False)

    def __str__(self):
        return self.title
