from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
	email=serializers.EmailField(required=True,write_only=True, validators=[UniqueValidator(queryset=User.objects.all())])
	username=serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
	password=serializers.CharField(min_length=8, write_only=True)
	def create(self, validated_data):
		return User.objects.create_user(validated_data['username'], validated_data['email'],validated_data['password'])
        
	#product=serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
	#profile=serializers.PrimaryKeyRelatedField(many=False, queryset=Profile.objects.all())
	class Meta:
		model=User
		fields=['id','username','email', 'password']

		
class ProductSerializers(serializers.ModelSerializer):
	user=serializers.ReadOnlyField(source='user.username')
	
	class Meta:
		model=Product
		fields=['id', 'libelle', 'description', 'prix' ,'etat', 'user', 'date_publier']

class Voiture_occasionSerializers(serializers.ModelSerializer):
	class Meta:
		model=Voiture_occasion
		fields='__all__'