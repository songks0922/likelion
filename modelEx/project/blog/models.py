from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add =True)
    view_cnt = models.IntegerField(default=0)
    scrap = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]