from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
u=router.register("phone",views.MobileViewset,basename="phone")

urlpatterns=[

    path("register/",views.SignUpView.as_view()),
    path("get/",views.SignUpView.as_view(),)
]+router.urls