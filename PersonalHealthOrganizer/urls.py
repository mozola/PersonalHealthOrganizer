from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('About.urls')),
    path('meal/', include('Meal.urls')),
    path('plan/', include('Plan.urls')),
]
