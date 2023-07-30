from django.urls import path


from . import views
urlpatterns = [
    path("", views.home,name="home"),
    path("reach/", views.reach_out,name="reach"),
    path("appreciation/", views.appreciation,name="appreciation"),
    path("korea/", views.korea,name="korea"),
    path("gap/", views.gap,name="gap")
]
