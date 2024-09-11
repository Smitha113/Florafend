# urls.py
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('predict/', views.predict, name='predict'),
    path('recommendation/', views.recommendation, name='recommendation'),
    path('latest-news/', views.latest_news, name='latest_news'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('ask/', views.ask, name='ask'),
    path('blog/', include('blog.urls')),
]
