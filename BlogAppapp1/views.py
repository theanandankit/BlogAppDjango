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
                    return Response(val)
                else:
                    return Response({'error':'Incorrect password'})
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
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }

                return Response(response)

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



                    


                