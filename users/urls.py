from django.urls import path
from .views import (LandingPageView, AboutListView, ContactListView, BlogListView, UserLogOutView,
                    UserRegisterView, UserLoginView, AgentListView, AgentDetailView,
                    AgentUpdateView, AgentDeleteView, TestimonialView)


urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
    path('about/', AboutListView.as_view(), name='about'),
    path('agent/', AgentListView.as_view(), name='agent'),
    path('agent/<int:id>/admin/', AgentUpdateView.as_view(), name='agent-update'),
    path('agent/<int:id>/admin/', AgentDeleteView.as_view(), name='agent-delete'),
    path('contact/', ContactListView.as_view(), name='contact'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path("auth/login/", UserLoginView.as_view(), name="login"),
    path("auth/register/", UserRegisterView.as_view(), name="register"),
    path("auth/logout/", UserLogOutView.as_view(), name="logout"),
    path("agent/<int:id>/", AgentDetailView.as_view(), name="agent-detail"),
    path("test/", TestimonialView.as_view(), name="testimonial"),

]