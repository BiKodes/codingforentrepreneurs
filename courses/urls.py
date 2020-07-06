from django.contrib import admin

from django.urls import path
from .views import (
    CourseView,
    CourseListView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView,
    # my_fbv,

)

app_name = "courses"

urlpatterns = [
    path('',CourseView.as_view(template_name="contact.html"), name = 'courses_list'),
    path('<int:id>/',CourseView.as_view(template_name="courses_detail.html"), name = 'courses_detail'),
    path('',CourseView.as_view(), name = 'courses_list'),
    path('create/',CourseCreateView.as_view(), name = 'courses_create'),
    path('<int:id>/update',CourseUpdateView.as_view(), name = 'courses_update'),
    path('<int:id>/delete',CourseDeleteView.as_view(), name = 'courses_delete'),

]
