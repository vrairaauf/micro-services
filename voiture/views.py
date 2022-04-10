from django.shortcuts import render

from django.http import HttpResponse , JsonResponse, Http404
from rest_framework.parsers import JSONParser
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .permissions import *
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, mixins
# Create your views here.

class Generateuser(generics.ListCreateAPIView):
	queryset=User.objects.all()
	serializer_class=UserSerializer
#en utilisant les viewset
#lavantage de viewset est de placer les deux classe en CBV et generics et mixins par un  seul classe
#cette classe permet seulement de lire soit tous les produits soit un seulproduit
class viewsetproduct(viewsets.ReadOnlyModelViewSet):
	queryset=Product.objects.all()
	serializer_class=ProductSerializers

class viewsettotalproduct(viewsets.ModelViewSet):
	queryset=Product.objects.all()
	serializer_class=ProductSerializers
	#pour appliquer les filter
	#filter_fields=('etat')
	#on peut aussi specifier les droit est lauth
	authentication_classes=[TokenAuthentication]
	permission_classes=[permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]
	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

#cette classe permet de tous les taches pour la voiture occasion

class viewsetCarsProduct(viewsets.ModelViewSet):
	queryset=Voiture_occasion.objects.all()
	serializer_class=Voiture_occasionSerializers
	#pour appliquer les filter
	#filter_fields=('Prix', 'Marque', 'Modéle', 'Type_de_chassis', 'Premiére_immatriculation', 'Pays', 'Ville')
	#pour le trie de resultat
	#ordering_fields=('Prix')
	#on peut aussi specifier les droit est lauth
	authentication_classes=[TokenAuthentication]
	permission_classes=[permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]
	def perform_create(self, serializer):
		serializer.save(user=self.request.user)