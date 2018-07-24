from django.urls import path, include
from acc import views


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
   


]
