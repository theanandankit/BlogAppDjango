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

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=User_info
        fields='__all__'

class EditProfileSerializer(serializers.ModelSerializer):
    user_details=UserInfoSerializer(many=True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','user_details']
        depth = 1

class GetProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email']


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

    who=GetUserInfoSerializer()

    class Meta:
        model = Following_info
        fields=['who']

class follownestedSerializer(serializers.ModelSerializer):
    person_list2=followSerializer(many=True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email','person_list2']

class followingSerializer(serializers.ModelSerializer):

    whom=GetUserInfoSerializer()

    class Meta:
        model = Following_info
        fields=['whom']

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

    author=GetUserInfoSerializer()

    class Meta:
        model = Blog_info
        fields = ['id','url','title','status','date','category','author','status','body']
        depth = 1

class blogaddserializer(serializers.ModelSerializer):
    class Meta:
        model = Blog_info
        fields = ['url','title','body','category','author','status','group']

class CreateGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Groups
        fields = ['group_id','group_description','creator_id','group_code','date','url']

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

class AuthorNameOnlySerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name','last_name']


class GroupInfoSerializer(serializers.ModelSerializer):

     creator_id = AuthorNameOnlySerializer

     class Meta:
        model = Groups
        fields = ['group_id','group_description','creator_id','date','url']
        depth=1



# profile full info

class ListFollow(serializers.ModelSerializer):
    class Meta:
        model = Following_info
        fields = ['who']

class ListFollowing(serializers.ModelSerializer):
    class Meta:
        model = Following_info
        fields = ['whom']

class ListOfBlog(serializers.ModelSerializer):

    author=GetUserInfoSerializer()

    class Meta:
        model = Blog_info
        fields = ['id','url','title','category','date','author','status']

class GetFullProfileInfoSerializer(serializers.ModelSerializer):

    author_name=ListOfBlog(many=True)
    user_details=UserInfoSerializer(many=True)
    person_list1=ListFollowing(many=True)
    person_list2=ListFollow(many=True)

    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','author_name','person_list1','person_list2','user_details']

class userPublicInfoserializer(serializers.ModelSerializer):

    user_details= UserInfoSerializer(many=True)
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','user_details']

class GetCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['category_name','url']
class GetGroupStrengthSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMembers
        fields = ['member_id']
class GetCreatedGroupsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Groups
        fields = '__all__'
        depth=1

class GroupsBlogSerializer(serializers.ModelSerializer):

    groups=ListOfBlog(many=True)

    class Meta:
        model = Groups
        fields = ['group_id','group_description','members','creator_id','date','groups']


class memberdetials(serializers.ModelSerializer):

    class Meta:
        model = GroupMembers
        fields =['group_id']
        depth=1

class meme(serializers.ModelSerializer):

     member_info = memberdetials

     class Meta:
        model = User
        fields = ['first_name','id','member_info'] 
        depth=2

class publicblogserializer(serializers.ModelSerializer):

    author=GetUserInfoSerializer()

    class Meta:
        model = Blog_info
        fields = ['id','url','title','status','date','category','author','status']
        depth = 1
