from django.db import models
from django.contrib.auth import models as ms


def user_directory_path(instance, filename):
    format = filename.split('.')[-1]
    pk = 1+int(Post.objects.last().id)
    return 'images/{}.{}'.format(pk, format)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Tag, self).save(*args, **kwargs)


class Post(models.Model):
    author = models.ForeignKey(ms.User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='posts')
    image = models.ImageField(upload_to=user_directory_path)

    class Meta:
        ordering = ['created_at']
