from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    return 'blog/{0}/{1}'.format(instance.author.id, filename)

    
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    OPTIONS = (
        ('Draft', 'Draft'),
        ('Published', 'Published')
    )
    COPTIONS = (
        ('Sport','Sport'),
        ('Politic','Politic'),
        ('Social','Social'),
        ('Economy','Economy'),
        ('Technology','Technology'),
        ('Literature','Literature'),
        ('Education','Education'),
        ('Philosophy','Philosophy'),
        ('Travel','Travel'),
        ('Other','Other')
    )
    title = models.CharField(max_length=1000)
    content = models.TextField(max_length=20000)
    image = models.URLField(max_length=5000, blank=True)     #  chARFIELD YA DA URL OLARAK KOYACAGIz
    category = models.CharField(max_length=20, choices=COPTIONS)
    # category = models.ForeignKey(
    #     Category, on_delete=models.PROTECT, related_name="cats")
    # category = models.ForeignKey(Category, on_delete = models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=OPTIONS, default='p')
    slug = models.SlugField(max_length = 50, blank=True, unique=True)  # how-to-learn-django

    def __str__(self):
        return self.title
    
    @property
    def comment_count(self):
        return self.comment_set.all().count()

    @property
    def view_count(self):
        return self.postview_set.all().count()
    
    @property
    def like_count(self):
        return self.like_set.all().count()
    
    @property
    def comments(self):
        return self.comment_set.all()


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=2000)

    def __str__(self):
        return self.user.username


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class PostView(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
