from django.db import models

   # Create your models here.
   class Contact(models.Model):

       name = models.CharField(max_length=30, null=True, blank=True)
       company_id = models.CharField(max_length=30)

       def __unicode__(self):
           return self.name