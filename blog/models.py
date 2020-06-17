from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    number_article = models.IntegerField()
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta():
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Author(models.Model):
    """ this section is  for article's authors"""
    name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    icon = models.ImageField(upload_to='authors-icons')
    description = models.TextField()
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta():
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
    
    def __str__(self):
        return self.name
    
    
class Article(models.Model):
    """ article section """
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='articles-images')
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categorie')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta():
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
    
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    commentator_name = models.CharField(max_length=30)
    commentator_first_name = models.CharField(max_length=30)
    icon = models.ImageField(upload_to='users-icons')
    message = models.TextField()
    email = models.EmailField()
    website = models.URLField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments_article')
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta():
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
    
    def __str__(self):
        return self.commentator_name
    

  
class Like(models.Model):
    name = models.CharField(max_length=30)
    like_status = models.BooleanField(default=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='like_article')
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta():
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
    
    def __str__(self):
        return self.name + self.like_status
    

