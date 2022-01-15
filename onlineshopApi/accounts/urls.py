from rest_framework.routers import DefaultRouter
from .views import CreateUserView
from rest_framework_simplejwt import views as jwt_views
from django.urls import path
from . import views
router = DefaultRouter()
router.register(r'registration', CreateUserView)

urlpatterns = router.urls

urlpatterns += [
    # jwt authenticated
    path('login',jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/',jwt_views.TokenRefreshView.as_view(),name='token_refresh'),

    # Profile
    path('profile', views.ProfileListView.as_view()),
    path('profile/<int:pk>', views.ProfileUpdateView.as_view()),
    #path('profile/statistic',views.ProfileStatistic.as_view()),

    # address -> list and create
    path('address/create', views.AddressCreateView.as_view()),
]