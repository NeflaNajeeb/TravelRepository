from travelproject import settings
from . import views
from django.urls import path
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    # your URL patterns
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



urlpatterns = [

   path('',views.demo,name='demo'),
   # path('about/', views.about, name='about'),
    #path('contact/', views.contact, name='contact'),
    #path('pasVal/',views.pasVal, name='pasVal'),
   # path('',views.add,name='add'),
   # path('add/', views.addition, name='addition')
]
if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL, ducument_root=settings.STATIC_ROOT)
   urlpatterns += static(settings.MEDIA_URL, ducument_root=settings.MEDIA_ROOT)