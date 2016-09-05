from django.contrib.auth.models import User

from rest_framework.serializers import (
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
    )


class UserCreateSerializer(ModelSerializer): 
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']
        extra_kwargs = {"password":
                            {"write_only": True}
                            }
    
    def create(self, validated_data):
        username = validated_data['email']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(username=username, email=email, first_name=first_name, last_name=last_name)
        user_obj.set_password(password)
        user_obj.save()
        return validated_data
        
    
class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField()
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'token',
            
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                            }
    def validate(self, data):
        # email = data['email']
        # user_qs = User.objects.filter(email=email)
        # if user_qs.exists():
        #     raise ValidationError("This user has already registered.")
        return data