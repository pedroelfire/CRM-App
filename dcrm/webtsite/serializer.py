from rest_framework import serializers
from . models import *

class NotasSerializer(serializers.ModelSerializer):
	class Meta:
		model = Notas
		fields = ['title', 'description']
