# from django.urls import path
# from . views import api_views

# urlpatterns = [
#     path("", api_views.StudentList.as_view(), name="list"),
#     path("detail/<int:id>", api_views.StudentGetUpdateDelete.as_view(), name="detail"),
# ]




#+ generic views

# from django.urls import path
# from .views import Student,StudentDetail

# urlpatterns = [
#     path("", Student.as_view(), name="list"),
#     path("list/<int:id>", StudentDetail.as_view(), name="detail"),
# ]






#!concreteview
from django.urls import path
from .views import StudentList,StudentGetUpdateDelete
urlpatterns = [
    path("list/", StudentList.as_view(), name="list"),
    path("list/<int:id>", StudentGetUpdateDelete.as_view(), name="detail"),
]