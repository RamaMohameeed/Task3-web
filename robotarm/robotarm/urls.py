"""
URL configuration for robotarm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from arm import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Page
    path('', views.control_panel, name='control_panel'),

    # Pose CRUD
    path('api/pose/save/', views.pose_save, name='pose_save'),
    path('api/pose/<int:pk>/load/', views.pose_load, name='pose_load'),
    path('api/pose/<int:pk>/delete/', views.pose_delete, name='pose_delete'),

    # “PHP-style” endpoints
    path('api/get_run_pose/', views.get_run_pose, name='get_run_pose'),
    path('api/update_status/', views.update_status, name='update_status'),

    # Create a new “run” command
    path('api/pose/run/', views.pose_run, name='pose_run'),
]
