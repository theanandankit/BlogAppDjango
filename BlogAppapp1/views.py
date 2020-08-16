from django.shortcuts import render
from BlogAppapp1.models import *
from BlogAppapp1.serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import datetime
from django.contrib.auth import logout
from rest_framework import generics
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class register_new_user(APIView):
    def post(self, request):
        serializers=register_user(data=request.data)
        val= {}
        self.object = User.objects.filter(email=request.data.get('email')).first()
        if self.object is None:
            if serializers.is_valid():
                users=serializers.save()
                val['Response']="Successfully registered a new user"
                val['Token']=Token.objects.get(user=users).key
            else:
                val= serializers.errors
            return Response(val)
        else:
            return Response({'error':"Email already in use."})
   
        




class login(APIView):
    #permission_classes = (AllowAny,)
    def post(self,request):
        serializers = LoginSerializer(data=request.data)
        if(serializers.is_valid()):
            print(serializers.data.get('email'), serializers.data.get("password"))
            email=serializers.data.get("email")
            password = serializers.data.get("password")
            self.object = User.objects.filter(email=email).first()
            if self.object == None:
                return Response({'error':'User with this email and password not found'})
            else:
                if self.object.check_password(password):
                    authenticate(self.object)
                    self.object.last_login = datetime.datetime.now()
                    self.object.save(update_fields=['last_login'])
                    val={}
                    val['Token']=Token.objects.get(user=self.object).key
                    val['Id']= self.object.id
                    if User_info.objects.filter(user_id=self.object.id).exists():
                        val['status']="found"
                        return Response(val,status=status.HTTP_302_FOUND)
                    else:
                        val['status']="Not"
                        return Response(val,status=status.HTTP_202_ACCEPTED)
                else:
                    return Response({'error':'Incorrect password'},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
    


class ChangePasswordView(APIView):
        
        
        model = User
        permission_classes = (IsAuthenticated,)

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def put(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = ChangePasswordSerializer(data=request.data)
            

            if serializer.is_valid():
                # Check old password
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({'Response':'Wrong password'})
                # set_password also hashes the password that the user will get
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                return Response({'Response':'Password change'})

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EditProfileView(APIView):

        model = User
        permission_classes = (IsAuthenticated,)
        def put (self, request, *args, **kwargs):
                self.object = self.request.user
                serializer = EditProfileSerializer(self.object, data=request.data)
                if serializer.is_valid():
                    user = User.objects.filter(username=serializer.validated_data["username"]).first()
                    if user is not None and Token.objects.get(user=self.object).key!=Token.objects.get(user=user).key:
                        return Response({'error':"Username not available"})
                    else:
                        serializer.save()
                        return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetProfileView(APIView):

        permission_classes = (IsAuthenticated,)
        def get(self, request):
            token = request.META['HTTP_AUTHORIZATION']
            token = token[6:]
            self.object = Token.objects.get(key= token ).user
            serializer = GetProfileSerializer(self.object)
            return Response(serializer.data)

class GetUserInfoView(generics.ListAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = GetUserInfoSerializer

    def get_queryset(self):
        queryset=User.objects.all()
        user_id=self.request.query_params.get('user_id', '')
        return queryset.filter(id=user_id)

class EditUserInfoView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request):
        self.object=User_info.objects.get(user_id=request.data.get("user_id"))
        # serializer = AddUserInfoSerializer(data=request.data)
        serializer=UserInfoSerializer(self.object,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FollowView(generics.ListAPIView):
    # permission_classes=(IsAuthenticated,)
    serializer_class = follownestedSerializer

    def get_queryset(self):
        queryset=User.objects.all()
        user_id=self.request.query_params.get('id', '')
        return queryset.filter(id=user_id)

class FollowingView(generics.ListAPIView):
    # permission_classes=(IsAuthenticated,)
    serializer_class = followingnestedSerializer

    def get_queryset(self):
        queryset=User.objects.all()
        user_id=self.request.query_params.get('id', '')
        return queryset.filter(id=user_id)

class register_Follow(APIView):
    def post(self, request):
        serializers=followtableserializer(data=request.data)
        val= {}
        if Following_info.objects.filter(who=request.data.get('who'),whom=request.data.get('whom')).exists():
            val['Response']="Already exist"
            return Response(val)

        if serializers.is_valid():
            users=serializers.save()
            val['Response']="Success"
            return Response(val)
        else:
            val= serializers.errors
            return Response(val)

## Blog Views

class BlogInfoView(generics.ListAPIView):

    serializer_class=bloginfoserializer

    def get_queryset(self):
        queryset=Blog_info.objects.all()
        _id=self.request.query_params.get('id', '')
        return queryset.filter(id=_id)
    
class BlogaddView(APIView):

    def post(self,request):
        serializer = blogaddserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class CreateGroupView(APIView):

    def post(self,request):
        serializer = CreateGroupSerializer(data=request.data)
        self.object  = self.request.user
        
        if serializer.is_valid():
            serializer.save()
            data={'group_id':request.data['group_id'],'member_id':request.data['creator_id']}
            serializer2= GroupMemberSerializer(data=data)
            if serializer2.is_valid():
                serializer2.save()
            return Response(serializer.data.get('group_code'))
        else:
            return Response(serializer.errors)

class JoinGroupView(APIView):
    permission_classes=(IsAuthenticated,)

    def post(self,request):
        model =Groups
        serializer = JoinGroupSerializer(data=request.data)
        if serializer.is_valid():
            try:
                group = Groups.objects.get(group_code=request.data.get('group_code'))         
            except Groups.DoesNotExist:
                group = None
            if group is not None:
                self.object = self.request.user
                group_row=None
                
                try:
                    group_row = GroupMembers.objects.filter(group_id=group.group_id, member_id=self.object.id).first()
                except GroupMembers.DoesNotExist:
                    group_row = None
                if group_row is None:
                    data={'group_id':group.group_id,'member_id':self.object.id}
                    serializer2= GroupMemberSerializer(data=data)
                    if serializer2.is_valid():
                        serializer2.save()
                        return Response({'status':"Saved"})
                    else:
                        return Response(serializer2.errors)
                else:
                    return Response({'status':"Already a member"})
                return Response("Valid")
            else:
                return Response("Invalid Code")
        else:
            return Response(serializer.errors)


class GroupInfoView(generics.ListAPIView):
    serializer_class = GroupInfoSerializer

    def get_queryset(self):
        queryset = Groups.objects.all()
        group_id = self.request.query_params.get('group_id', '')
        return queryset.filter(group_id=group_id)

class FullProfileInfoView(generics.ListAPIView):
    serializer_class = GetFullProfileInfoSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        user_id = self.request.query_params.get('user_id','')
        return queryset.filter(id=user_id)

class BlogSearchView(generics.ListCreateAPIView):
    serializer_class = bloginfoserializer
    filter_backends =[filters.SearchFilter,]
    search_fields=['title']

    def get_queryset(self):
        category=self.request.query_params.get('category','food')
        queryset=Blog_info.objects.all()
        return queryset.filter(status='public',category=category)
    
class ProfileSearchView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = userPublicInfoserializer
    filter_backends =[filters.SearchFilter,]
    search_fields=['username','first_name','last_name']

class GetCategoryView(APIView):

    def get(self, request):
        model = Category.objects.all().order_by('category_name')
        serializer = GetCategorySerializer(model, many= True)
        return Response(serializer.data)

class GetCreatedGroupsView(generics.ListAPIView):

    serializer_class = GetCreatedGroupsSerializer

    def get_queryset(self):
        queryset = Groups.objects.all()
        user_id = self.request.query_params.get('user_id','')
        return queryset.filter(creator_id=user_id)

class PublicPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'

class publicBlogView(generics.ListAPIView):
    serializer_class = publicblogserializer
    pagination_class=PublicPagination
    
    def get_queryset(self):
        queryset = Blog_info.objects.all()
        return queryset.filter(status="public").order_by("-date")

class Grouplistview(generics.ListAPIView):
    serializer_class = CreateGroupSerializer

    def get_queryset(self):
        queryset = Groups.objects.all()
        user_id=self.request.query_params.get('user_id')
        return queryset.filter(creator_id=user_id)

class GroupsBlogView(generics.ListAPIView):

    serializer_class=GroupsBlogSerializer

    def get_queryset(self):
        queryset = Groups.objects.all()
        id=self.request.query_params.get('group_id','')
        return queryset.filter(group_id=id)

class FollowCheckView(generics.ListAPIView):

     def post(self, request):
        serializers=followtableserializer(data=request.data)
        val= {}
        if Following_info.objects.filter(who=request.data.get('who'),whom=request.data.get('whom')).exists():
            val['Response']="Already exist"
            return Response(val)
        else:
            val['Response']="Not exist"
            return Response(val)

     def delete(self,request):
        serializers=followtableserializer(data=request.data)
        val= {}
        if Following_info.objects.filter(who=request.data.get('who'),whom=request.data.get('whom')).exists():
            Following_info.objects.filter(who=request.data.get('who'),whom=request.data.get('whom')).delete()
            val['Response']="Deleted"
        else:
            val["Response"]="User don't exist"
        return Response(val)


class GroupsMemberList(generics.ListAPIView):

    serializer_class=meme

    def get_queryset(self):
        queryset = User.objects.all()
        user_id=self.request.query_params.get('user_id','')
        return queryset.filter(id=user_id)


class BlogCategoriesList(generics.ListAPIView):
    serializer_class = bloginfoserializer
    pagination_class=PublicPagination
    
    def get_queryset(self):
        queryset = Blog_info.objects.all()
        request_category=self.request.query_params.get('category')
        return queryset.filter(status="public",category=request_category).order_by("-date")

class DeleteFollowView(generics.ListAPIView):

    def post(self,request):
        serializers=followtableserializer(data=request.data)
        val= {}
        if Following_info.objects.filter(who=request.data.get('who'),whom=request.data.get('whom')).exists():
            Following_info.objects.filter(who=request.data.get('who'),whom=request.data.get('whom')).delete()
            val['Response']="Deleted"
        else:
            val["Response"]="User don't exist"
        return Response(val)

class AddUserInfoView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer=UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileInfoCheck(APIView):

    def post(self,request):
        val= {}
        if User_info.objects.filter(user_id=request.data.get('user_id')).exists():
            val['Response']="exist"
        else:
            val["Response"]="User don't exist"
        return Response(val)