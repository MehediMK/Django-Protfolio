from django.db import models

class Myskill(models.Model):
    image = models.ImageField(upload_to='skillimage/')
    title = models.CharField(max_length=50,blank=False)
    desc = models.TextField(max_length=500,blank=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def summary(self):
        return self.desc[0:100]

    def __str__(self):
        return self.title


class Contactinfo(models.Model):
    cname = models.CharField(max_length=50,blank=True)
    cemail = models.EmailField(max_length=50,blank=True)
    cquery = models.TextField(max_length = 1000)

    def __str__(self):
        return self.cname



