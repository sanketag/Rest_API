# import serializer from rest_framework
# from django.db.models import fields
from rest_framework import serializers, viewsets
# import model from models.py
from .models import *
# import routers
from rest_framework import routers

# Create a model serializer
class TestSerializer(serializers.ModelSerializer):
	# specify model and fields
	class Meta:
		model = TestModel
		fields = ('category', 'subcatgeory', 'name', 'amount')
'''
# create a viewset
class TestViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = TestModel.objects.all()
	# specify serializer to be used
	serializer_class = TestModel

# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used
router.register(r'test', TestViewSet)

'''