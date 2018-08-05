from django.urls import path, include
from acc import views

from acc.views import FlokiBotView
############################api#############################
#from rest_framework.urlpatterns import format_suffix_patterns
#############################################################

from rest_framework import routers


############################################################

router = routers.DefaultRouter()
router.register('', views.userView)

############################################################


urlpatterns = [
    

    path('apireg/', views.userCreateView.as_view()),

    path('apilogin/', views.userLoginView.as_view()),
    path('msg/', views.Msg.as_view()),
    path('data/', include(router.urls)),
    path('374ee80922e1c0e51a0c45e6bf097c1f6cfa6990945ed6592a/', FlokiBotView.as_view()),
   


]
