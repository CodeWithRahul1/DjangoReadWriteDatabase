from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from .serializers import UserRegistrationSerializer, UserLoginSerializer, ProductSerializer
from rest_framework import generics
from .models import Product

User = get_user_model()

class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(using='read_db', username=username, password=password)

            if user:
                return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Product Registration (Writes to write_db)
class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.using('write_db').all()
    serializer_class = ProductSerializer

# Product Listing (Reads from read_db)
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.using('read_db').all()
    serializer_class = ProductSerializer