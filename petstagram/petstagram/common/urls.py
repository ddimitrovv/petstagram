from django.urls import path

from petstagram.common.views import home_page

urlpatterns = (
    path('', home_page, name='home'),
)

#TODO:
# Home Page: http://127.0.0.1:8000/
