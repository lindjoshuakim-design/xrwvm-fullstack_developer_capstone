from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # path for registration template view
    path('register/', TemplateView.as_view(template_name="index.html")),

    # path for login API/backend view
    path('login', views.login_user, name='login'),

    # path for logout API/backend view
    path('logout', views.logout_request, name='logout'),

    # path for getting cars
    path('get_cars', views.get_cars, name='getcars'),

    # path for dealer reviews view (uncomment when ready)
    # path('dealer/<int:dealer_id>/reviews', views.get_dealer_reviews, name='dealer_reviews'),

    # path for add a review view (uncomment when ready)
    # path('add_review', views.add_review, name='add_review'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)