from django.contrib import admin
from django.urls import path,include
from user_management.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', home, name='home'),# home page
    path('api/user/', include('user_management.urls'), name='user_management'),# user management urls
    path('api/data-management/', include('data_management.urls'), ),# data management urls
    path('api/financial-management/', include('financial_management.urls')),
    path('api/supply-chain/', include('supply_chain.urls')),
   path('user/', include('user_management.urls')),
]
