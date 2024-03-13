from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    e_mail = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=100)
    image_name = models.CharField(max_length=50)
    data = models.DateField(
        auto_now=True, verbose_name='Date')  # just by mistake
    slug = models.SlugField(unique=True, db_index=True)
    # SlugField automatically set db_index -> True
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        "blog.Author", related_name='posts', null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField("blog.Tag")

    def __str__(self):
        return self.title


class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return self.caption
