from django.db import models

# Create your models here.


from django.contrib.auth.models import User

class Donor(models.Model):
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name



class Sobre(models.Model):
    date = models.DateTimeField()
    amount = models.IntegerField()
    concept = models.TextField(max_length=100)
    donor = models.ForeignKey(Donor)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.donor.name+" - "+self.concept

