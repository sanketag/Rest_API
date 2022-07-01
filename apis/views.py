from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import *
from .serializers import *
import pdb

@api_view(['GET'])
def ApiOverview(request):
	api_urls = {
		'all_items': '/',
		'Search by Category': '/?category=category_name',
		'Search by Subcategory': '/?subcategory=category_name',
		'Add': '/create',
		'Update': '/update/pk',
		'Delete': '/item/pk/delete'
	}

	return Response(api_urls)

@api_view(['POST'])
def add_items(request):
	item = TestSerializer(data=request.data)

	# validating for already existing data
	if TestModel.objects.filter(**request.data).exists():
		raise serializers.ValidationError('This data already exists')

	if item.is_valid():
		item.save()
		return Response(item.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def view_items(request):
	if request.query_params:
		# http://127.0.0.1:8000/api/all/?category=food
		items = TestModel.objects.filter(**request.query_params.dict())
	else:
		items = TestModel.objects.all()

	# if there is something in items else raise error
	if items:
		data = TestSerializer(items, many=True)
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_items(request, pk):
	item = TestModel.objects.get(pk=pk)
	data = TestSerializer(instance=item, data=request.data)

	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_items(request, pk):
	item = TestModel.objects.get(pk=pk)
	item.delete()
	return Response(status=status.HTTP_202_ACCEPTED)
