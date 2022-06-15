from rest_framework import serializers
from django.utils.timezone import now
from .models import Path, Student

# class StudentSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=30)
#     last_name = serializers.CharField(max_length=30)
#     number = serializers.IntegerField()
#     id = serializers.IntegerField()

#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.number = validated_data.get('number', instance.number)
#         instance.save() 
#         return instance

class StudentSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()
    class Meta:
        model = Student
        # fields = ('first_name','id', 'last_name', 'number')
        fields = '__all__'
    #-is_valid() dediğimizde aşağıdaki bu metotlar çalışıyor
    def validate_first_name(self, value):#first_name için validate methodu yazıyoruz
            if value.lower() == 'rafe':#kayıt olmaya çalışan ismi rafe ise hata döndürüyoruz
                raise serializers.ValidationError("Rafe can not be our student")
            return value
    # def validate_number(self, value): 
        
    #         if value > 1000: 
    #             raise serializers.ValidationError("Numbers must be lower than 1000") 
    #         return value

    def get_days_since_joined(self, obj):
        return (now() - obj.register_date).days 

class PathSerializer(serializers.ModelSerializer):
    # students=StudentSerializer(many=True)#+obje olarak gösteriyor bütünbilgiler ve many=True yapıyoruz ki birden fazla öğrenci gelebilsin diye
    #students modeldeki related name den geliyor
    # students = serializers.StringRelatedField(many=True)#+string olrak gösteriyor ama modeldeki __str__ içindekine göre yani admin de nasıl gözüküyorsa
    students = serializers.PrimaryKeyRelatedField(many=True, read_only=True)#öğrencinin id sini gösteriyor
    class Meta:
        model = Path
        fields = "__all__"

# StudentSerializer(many=True) = obje olarak gösteriyor serialize olan bütün bilgileri ve many=True yapıyoruz ki birden fazla öğrenci gelebilsin diye
# StringRelatedField(many=True)#+string olrak gösteriyor ama modeldeki __str__ içindekine göre yani admin de nasıl gözüküyorsa
# PrimaryKeyRelatedField(many=True, read_only=True)#öğrencinin primary key ini gösteriyor
#read_only=True örneğin id gönderseniz bile djagno kendisi id oluşturur
#write_only=True de 