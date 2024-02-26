from django.urls import path
from CBVapp import views


urlpatterns = [
    path('addstu', views.AddStudent.as_view()),                #Create
    path('viewstu', views.StudentList.as_view()),              #Read
    path('updatestu/<sid>', views.UpdateStudent.as_view()),    #Update
    path('deletestu/<sid>', views.DeleteStudent.as_view()),    #Delete
]