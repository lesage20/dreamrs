from django.db import models

# Create your models here.
class SiteInfo(models.Model):
    """ information about the website """
    
    name = models.CharField(max_length=30)
    icon = models.ImageField(upload_to='site-icons')
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    description = models.TextField()
    addresse = models.CharField(max_length=30)
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta():
        verbose_name = "Site Info"
        verbose_name_plural = "Site Infos"
        
    def __str__(self):
        return self.name


class Contact(models.Model):
    """these fields are about Contact sections """
    geolocation = models.URLField()
    message = models.TextField()
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    class Meta():
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
    
    def __str__(self):
        return self.name 
    

class Testimonial(models.Model):
    """ these fields are about testimonies from  users """
    name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    job = models.CharField(max_length=30)
    message = models.TextField()
    icon = models.ImageField(upload_to='users-icon')
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta():
        verbose_name = "Testimonie"
        verbose_name_plural = "Testimonies"
    
    def __str__(self):
        return self.name 
    
class NewsLetter (models.Model):
    """ This is for the user to enter his email to receive news from us """
    
    email = models.EmailField()
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta():
        verbose_name = "Newsletter"
        verbose_name_plural = "Newsletters"
    
    def __str__(self):
        return self.email 

class SocialAccounts(models.Model):
    """ Site's social accounts """
    
    ICONS = [
        ("fa-facebok", "Facebook"),
        ("fa-twitter", "Twitter"),
    ]
    
    name = models.CharField(max_length=30)
    link = models.URLField()
    icon = models.CharField(max_length=30, choices=ICONS)
    
    class Meta():
        verbose_name = "Social Account"
        verbose_name_plural = "Social Accounts"
    
    def __str__(self):
        return self.name 
    
