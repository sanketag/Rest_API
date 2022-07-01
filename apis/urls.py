# basic URL Configurations
from django.urls import include, path

# import everything from views
from .views import *
from .serializers import *

# specify URL Path for rest_framework
urlpatterns = [
	# path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls')),
    path('', ApiOverview, name='home'),
    path('create/', add_items, name='add-items'),
    path('all/', view_items, name='view_items'),
    path('update/<int:pk>/', update_items, name='update-items'),
    path('delete/<int:pk>/', delete_items, name='delete-items'),
]
