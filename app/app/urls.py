from django.conf.urls import url
from django.contrib import admin
from polls import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^event/', views.event),
]
