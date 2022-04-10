from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.
class Profile(models.Model):
	GENDER={
		('Homme', 'Homme'),
		('Femme', 'Femme')
	}
	code_verification=models.CharField(max_length=20)
	gender=models.CharField(max_length=255, choices=GENDER, default='Homme')
	age=models.IntegerField(null=True)
	user=models.ForeignKey(User, related_name='real_user', null=True, on_delete=models.SET_NULL)
	def __str__(self):
		return self.user
class Product(models.Model):
	ETAT={
		("neuf", "neuf"),
		("ancien", "ancien"),
		("presq-neuf", "presq-neuf"),
	}
	libelle=models.CharField(max_length=255)
	description=models.TextField()
	date_publier=models.DateTimeField(auto_now_add=True)
	user=models.ForeignKey(User, related_name='user', null=True, on_delete=models.CASCADE)
	etat=models.CharField(max_length=255, choices=ETAT)
	prix=models.IntegerField(null=True)
	def __str__(self):
		return self.libelle
		"""
class Category(models.Model):
	titre=models.CharField(max_length=255)
	description=models.TextField()
	slug=models.SlugField(max_length=255, unique=True)
	image=models.ImageField(blank=True, upload_to='images/category/')
	def __str__(self):
		return self.titre

class SubCategory(models.Model):
	titre=models.CharField(max_length=255)
	description=models.TextField()
	slug=models.SlugField(max_length=255, unique=True)
	image=models.ImageField(blank=True, upload_to='images/category/')
	category=models.ForeignKey(Category, related_name='category', null=True, on_delete=models.SET_NULL)
	def __str__(self):
		return self.titre
"""
class Voiture_occasion(models.Model):
	BOITE={
		('Manuelle', 'Manuelle'),
		('Automatique', 'Automatique')
	}
	Prix=models.FloatField(null=True)
	Marque=models.CharField(max_length=255)
	Modéle=models.CharField(max_length=255)
	Type_de_chassis=models.CharField(max_length=255)
	Premiére_immatriculation=models.CharField(max_length=255)
	Pays=models.CharField(max_length=255)
	Ville=models.CharField(max_length=255)
	Carburant=models.CharField(max_length=255)
	Année=models.CharField(max_length=255)
	Kilométrage=models.IntegerField()
	Puissance_fiscale=models.IntegerField(null=True)
	Nombre_de_portes=models.IntegerField(default=4)
	Nombre_de_siége=models.IntegerField(null=True)
	Couleur_de_carrosserie=models.CharField(max_length=255)
	Boite_de_vitesse=models.CharField(choices=BOITE, max_length=50)
	Permis=models.BooleanField(default=True)
	images=models.ImageField(blank=True, default="sansImageCar.png", upload_to="images/voituresOccasion/")
	user=models.ForeignKey(User, related_name='vendeur', on_delete=models.CASCADE)
	def __str__(self):
		return self.id
class ImageVoitureOccasion(models.Model):
	image=models.ImageField(blank=True, upload_to="images/voituresOccasion/")
	product=models.ForeignKey(Voiture_occasion, related_name='voiture', null=True, on_delete=models.CASCADE)

"""
class MetaInformationsProduct(models.Model):
	MinimalistBigCategory = {
		("Marketplace", "Marketplace"),
		("Location Minimaliste", "Location Minimalist"),
		("Echange", "Echange"),
		("Objets gratuits", "Objets gratuits")
	}
	MinimalistSmallCategory = {
		("Véhicule", "Véhicule"),
		("Vélo", "Vélo"),
		("Trotinettes éléctrique", "Trotinettes éléctrique"),
		("Immobilier", "Immobilier"),
		("Loisirs", "Loisirs"),
		("Jeu et jouets", "Jeu et jouets"),
		("Jeux vidéos et consoles", "Jeux vidéos et consoles"),
		("Collection", "Collection"),
		("Alimentation", "Alimentation"),
		("Billeterie", "Billeterie"),
		("Mode", "Mode"),
		("Périculture", "Périculture"),
		("Multimédia High tech", "Multimédia High tech"),
		("Maison et jardin", "Maison et jardin"),
		("Matériel professionnel", "Matériel professionnel"),
		("Divers", "Divers"),
		("Autres", "Autres")
		
	}
	ETAT={
		("neuf", "neuf"),
		("ancien", "ancien"),
		("presq-neuf", "presq-neuf"),
	}
	libelle=models.CharField(max_length=255)
	user=models.ForeignKey(User, related_name='auteur', null=True, on_delete=models.CASCADE)
	#etat=models.CharField(max_length=255, choices=ETAT)
	category=models.CharField(max_length=255, choices=MinimalistBigCategory)
	subCategory=models.CharField(max_length=255, choices=MinimalistSmallCategory)
	#prix=models.IntegerField(null=True)
	date_publier=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.libelle
"""
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)



#class Voitures