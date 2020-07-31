from rest_framework import serializers
from BlogAppapp1.models import *
from django.contrib.auth.models import User

class register_user(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password', 'email','first_name','last_name')
        write_only_fields = ('password',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            )

        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        password = serializers.CharField(required=True)
        email = serializers.CharField(required=True)
        fields = ['email','password']

class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class EditProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name']

class GetProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email']

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=User_info
        fields='__all__'

class GetUserInfoSerializer(serializers.ModelSerializer):
    user_details=UserInfoSerializer(many=True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email','user_details']


class AddUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model =User_info
        fields='__all__'


# for follower list 

class followSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Following_info
        fields=['who']
        depth=1

class follownestedSerializer(serializers.ModelSerializer):
    person_list2=followSerializer(many=True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email','person_list2']

class followingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Following_info
        fields=['whom']
        depth = 1

class followingnestedSerializer(serializers.ModelSerializer):
    person_list1=followingSerializer(many=True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email','person_list1']

class followtableserializer(serializers.ModelSerializer):

    class Meta:
        model = Following_info
        fields = '__all__'

## Blog APIs

class bloginfoserializer(serializers.ModelSerializer):

    class Meta:
        model = Blog_info
        fields = ['id','url','title','body','date','category','author']
        depth = 1

class CreateGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Groups
        fields = ['group_id','group_description','creator_id','group_code']

class JoinGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ['group_code']

class GroupMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model= GroupMembers
        fields = '__all__'

class GetMemberInfoSerailizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name']

class GroupMemberInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMembers
        fields = ['member_id']
        depth =1



class GroupInfoSerializer(serializers.ModelSerializer):
    # members = serializers.SerializerMethodField

    # def get_member_info(self, obj):
    #     # this will find all categories with a venue in given area
    #     print(obj)
    #     members = User.objects.filter(id=obj)
    #     serializer = GetMemberInfoSerailizer(members, many=True)
    #     return serializer.data
    members = GroupMemberInfoSerializer(many=True)

    class Meta:
        model = Groups
        fields = ['group_id','group_description','members','creator_id']
    
    


        
