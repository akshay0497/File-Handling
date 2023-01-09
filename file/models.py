from django.db import models

# Create your models here.

class FileHandling(models.Model):
    index = models.CharField(max_length=10, verbose_name='Index')
    user_id = models.CharField(max_length=200, verbose_name='User Id')
    first_name = models.CharField(max_length=250, verbose_name='First Name')
    last_name = models.CharField(max_length=250, verbose_name='Last Name')
    gender= models.CharField(max_length=10, verbose_name='Gender')
    email = models.EmailField(verbose_name='Email Id')
    phone = models.CharField(max_length=25, verbose_name='Phone Numnber')
    d_o_b = models.CharField(max_length=15,verbose_name='Dat of Birth')
    job_title = models.CharField(max_length=300, verbose_name='Job Title')

    def __str__(self):
        return self.first_name + '' + self.last_name

