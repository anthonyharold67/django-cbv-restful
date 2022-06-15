from django.db import models

# Create your models here.
class Path(models.Model):
    path_name = models.CharField(max_length=100)
    def __str__(self):
        return self.path_name

class Student(models.Model):
    path = models.ForeignKey(Path, on_delete=models.CASCADE,related_name="students")#related_name="students" bize studentlerin path ile ilişkisi olduğunu söyler ve daha sonra çağırmak için kullanılır kolaylık sağlar ve student.id ile path.id ile ilişkisi kontrol edebiliriz.
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)
    register_date = models.DateTimeField(auto_now_add=True)
    # blank=True for admin dashboard
    # null=True for db
    def __str__(self):
        return f"{self.number}-{self.first_name} {self.last_name}"