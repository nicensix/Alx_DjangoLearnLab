# LibraryProject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('LibraryProject.relationship_app.urls')),  # ✅ Add this
]
