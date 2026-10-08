from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView  # Required for TemplateView
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # path for registration
     path('register/', TemplateView.as_view(template_name="index.html")),

    # path for login API/backend view
    path(route='login', view=views.login_user, name='login'),

    # path for rendering the index/login page template
    path('login/', TemplateView.as_view(template_name="index.html"), name='index'),

    # path for dealer reviews view
    # path(route='dealer/<int:dealer_id>/reviews', view=views.get_dealer_reviews, name='dealer_reviews'),

    # path for add a review view
    # path(route='add_review', view=views.add_review, name='add_review'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)