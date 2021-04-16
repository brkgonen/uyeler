from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.app.serializers import UserSerializer
from api.models import User

#class views
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

class UserListCreateView(APIView):
    def get(self, request):
        users = User.objects.filter(aktif=True)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors ,status= status.HTTP_400_BAD_REQUEST)


class UserDetailAPIView(APIView):
    def get_object(self, pk):
        user_instance = get_object_or_404(User, pk=pk)
        return user_instance
        
    
    def get(self, request, pk):
        user = self.get_object(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
   
    def put(self, request, pk):
        user = self.get_object(pk=pk)
        serializer = UserSerializer(user, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)


    def delete(self, request,pk):
        user = self.get_object(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





#FUNCTION  METHOD#
# @api_view(['GET', 'POST'])
# def user_list_create_api_view(request):
    
#     if request.method == 'GET':
#         users = User.objects.filter(aktif=True)
#         serializer = UserSerializer(users, many= True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status= status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def user_detail_api_view(request, pk):
#     try:
#         user_instance = User.objects.get(pk=pk)
#     except:
#         User.DoesNotExist
#         return Response(
#             {
#                 'errors': {
#                     'code': 404,
#                     'message': f'Böyle bir id ({pk}) ile ilgili kullanıcı bulunamadı'
#                 }
#             },
#             status= status.HTTP_404_NOT_FOUND
#         )

#     if request.method == 'GET':
#         serializer = UserSerializer(user_instance)
#         return Response(serializer.data)


#     elif request.method == 'PUT':
#         serializer = UserSerializer(user_instance , data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status= status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         user_instance.delete()
#         return Response(
#             status= status.HTTP_204_NO_CONTENT
#         )