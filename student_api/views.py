# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .serializers import StudentSerializer
# from .models import Student

#* Sınıf Tabanlı yapıyı kullanarak, bir önceki sayfada İşlev Tabanı yapısını kullandığımız işlemleri yapıyoruz. Aşağıda görebileceğiniz gibi, daha organize bir kod yapısı sağlar. Mantık ve kodlar hemen hemen aynı. Kodları inceleyin lütfen.

# class StudentList(APIView):
    
#     def get(self, request):
#         students = Student.objects.all()
#         serializer =StudentSerializer(students, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class StudentGetUpdateDelete(APIView):
    
#     def get_object(self, id):
#         try:
#             return Student.objects.get(id=id)
#         except Student.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#     def get(self, request, id):
#         #student = get_object_or_404(Student, id=id)
#         student = self.get_object(id)
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)
    
#     def post(self, request, id):
#         student = self.get_object(id)
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 "message":"Student updated"
#             }
#             return Response(data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def  delete(self, request, id):
#         student = self.get_object(id)
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



#* Django'da CRUD işlemleri için yaptığımız işlemler genelde benzer işlemler olduğu için arka planda bizim için bu işlemleri yapan yapılar geliştirilmiştir. Bu sayede aynı kodları tekrar yazmaktan kurtuluyor ve aynı işi daha az kodla yapıyoruz.
#* Bu amaçla DRF tarafından GenericAPIViews ve Mixins oluşturulmuştur. Genel APIView'ler, Sınıf Tabanlı Görünümlerde kullandığımız APIView'den devralınır ve onlara ekstra özellikler verir. GenericApiView'ler genellikle karışımlarla birlikte kullanılır. Mixins, GenericAPIView'lere .create() ve .list() yetenekleri ekler. Bunları .get() ve .post() gibi düşünebilirsiniz.
# #+ generic views
# from .models import Student
# from .serializers import StudentSerializer
# from rest_framework import generics, mixins

# class StudentDetail(generics.GenericAPIView,mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin ):
    
#     serializer_class = StudentSerializer
#     queryset = Student.objects.all()
#     lookup_field = "id"
#     #-NOT: Django.urls'den GET, PUT, DELETE işlemleri için belirli bir nesneyi çağıracağımız için lookup_field ve id kullanıyoruz.
#     def get(self, request,id):
#         return self.retrieve(request)
             
#     def put(self, request, id):
#         return self.update(request, id)
    
#     def delete(self, request, id):
#         return self.destroy(request,id)


# class Student(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    
#     serializer_class = StudentSerializer
#     queryset = Student.objects.all()
 
        
#     def get(self, request):
#         return self.list(request)
    
#     def post(self, request):
#         return self.create(request)


# rest_framework'ten jenerik ve karışımları içe aktardık
# daha önce oluşturduğumuz serializer_class'ı (ad standarttır) tanımlıyoruz.
# Kuracağımız view mantığına göre query_set (adı standart) tanımlıyoruz
# Lookup_field: Nesneleri hangi alandan çağıracağımızı belirtir. benzersiz olmalı
# NOT: Django.urls'den GET, PUT, DELETE işlemleri için belirli bir nesneyi çağıracağımız için lookup_field ve id kullanıyoruz.




#* GenericAPIView ve Mixins ile arka planda neler olduğunu öğrendik. Asıl amacımız concrete viewsleri öğrenmektir. Concrete view bize ihtiyaç duyacağımız tüm işlevselliği çok daha az kodla sunar.
#* Her concrete view, bir GenericAPIView ve ilişkili Mixin'lerden oluşur. örneğin: ListCreateApiView, ListModelMixin, CreateModelMixin ve GenericAPIView'in bir birleşimidir.
#!concrete view
from .models import Student
from .serializers import StudentSerializer
from rest_framework import generics

class StudentList(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    

class StudentGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = "id"