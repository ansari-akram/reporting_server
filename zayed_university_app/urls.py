from django.urls import path
from .views import *

urlpatterns = [
    # for zayed_chatbot
    path('watson-assistant/', get_response_from_watson, name="watson-assistant"),
    path('login/', login),
    path('reset/', reset_count),
    path('wrong_answer/', wrong_answer, name="wrong_answer"),
    # path('multiple_filter/', multiple_filter, name="multiple_filter"),

]
