from django.conf.urls import url
from django.contrib import admin
from main import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sabado-de-ubuntu/$',views.Sabado.as_view()),
]
