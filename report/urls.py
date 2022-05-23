from django.contrib import admin
from django.urls import path, include
# from zayed_university_app import views
from zayed_university_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("authentication.urls")),
    path("", include("report_app.urls")),
    path("chatbot/", include("zayed_university_app.urls")),
    # path("^advanced_filters/", include("advanced_filters.urls"))
    path('multiple_filter/', views.multiple_filter), #added
]
