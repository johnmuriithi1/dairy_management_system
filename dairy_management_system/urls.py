from django.contrib import admin
from django.urls import path,include
#from user_management.normal_views import home

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('user_management.urls', namespace='user_management')),
    path('data-management/', include('data_management.urls', namespace='data_management')),
    #path('finance/', include('financial_management.urls', namespace='financial_management')),
    #path('supply-chain/', include('supply_chain.urls', namespace='supply_chain')),

    path('api/user-management/', include('user_management.api_urls', namespace='user_management_api')),
    path('api/data-management/', include('data_management.api_urls', namespace='data_management_api')),
]
