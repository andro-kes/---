from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, create_profile_page

router = DefaultRouter()
# pd - profilesmodel
router.register(r'pm', ProfileViewSet, basename='pm')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', create_profile_page, name='create_profile_page'),
]
