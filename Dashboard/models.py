from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class  UserProfile(models.Model):
    user = models.OneToOneField(User,related_name='userprofile', on_delete=models.SET_NULL,null=True)
    Nom = models.CharField(max_length=100, blank=False , null=False)
    Prénom = models.CharField(max_length=100, blank=True , null=True)
    Addresse = models.CharField(max_length=100, blank=True , null=True)
    Ville = models.CharField(max_length=100, blank=True , null=True)
    Téléphone = models.CharField(max_length=100, blank=True , null=True)
    Email = models.EmailField(blank=False , null=False)

    def __str__(self):
        return self.user.username



@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()



CHOICES = (
        ('Fait', 'Fait'),
        ('en attendant', 'en attendant'),
        ('annulée', 'annulée'),

)
class Intervention(models.Model):
    Date_Ajouté = models.DateTimeField(auto_now_add=True)
    Nom_Client= models.CharField(max_length=100, blank=False , null=False)
    Numéro = models.CharField(max_length=100, blank=False , null=False)
    Ville = models.CharField(max_length=100, blank=False , null=False)
    Date=models.DateField(null=True,blank=True)
    Address = models.CharField(max_length=100, blank=False , null=False)
    Code_postal = models.IntegerField()
    Par= models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, )
    Commentaire = models.CharField(max_length=500, blank=True, null=True)
    Prix = models.IntegerField(blank=True, null=True)
    Status = models.CharField(max_length=500,choices=CHOICES, default='en attendant', blank=True, null=True)
    valeur =models.IntegerField(default=1)




    @property
    def get_total_c(self):
        total = Intervention.objects.all().count()
        return  total


    def __str__(self):
        return (self.id and self.Nom_Client)


    @property
    def get_html_url(self):
        url = reverse('calendar')
        return f'<a style="background-color: wheat ; color: black;" href="{url}"> {str("#")+str(self.id)+str("  ")+str(self.Nom_Client)} </a>'



class Client(models.Model):
    Nom_Client= models.CharField(max_length=100, blank=False , null=False)
    Numéro = models.CharField(max_length=100, blank=False , null=False)
    Ville = models.CharField(max_length=100, blank=False , null=False)
    Address = models.CharField(max_length=100, blank=False , null=False)
    Code_postal = models.IntegerField()


    def __str__(self):
        return (self.Nom_Client)





class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('calendar')
        return f'<a href="{url}"> {self.title} </a>'


