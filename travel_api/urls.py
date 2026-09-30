from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

# Root view
def home(request):
    return JsonResponse({"message": "Welcome to the Travel API"})

urlpatterns = [
    path('', home, name='home'),  # root endpoint
    path('admin/', admin.site.urls),

    # JWT auth endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API schema & docs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # App routes
    path('api/accounts/', include('accounts.urls')),
    path('api/destinations/', include('destinations.urls')),
    path('api/itineraries/', include('itineraries.urls')),
    path('api/bookings/', include('bookings.urls')),
    path('api/reviews/', include('reviews.urls')),
    path('api/budgets/', include('budgets.urls')),
]
