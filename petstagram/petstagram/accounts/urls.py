from django.urls import path, include

from petstagram.pets.views import register, login, profile_details, profile_edit, profile_delete

urlpatterns = (
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('account/<int:pk>/', include([
        path('', profile_details, name='accounts details'),
        path('edit/', profile_edit, name='accounts edit'),
        path('delete/', profile_delete, name='accounts delete'),
    ])),
)
