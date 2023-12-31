from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import status
from .serializer import NormalAdvocateSerializer
from rest_framework import serializers
from userapp.models import Advocate,UserData

class AdvocatesListView(APIView):
    def get(self, request):
        normal_advocate = Advocate.objects.filter(type_of_user='normal_advocate')
        serializer = NormalAdvocateSerializer(normal_advocate, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CreateAdvocatesListView(APIView):
    def post(self, request):        
        email = request.data.get('email')
        password = request.data.get('password')
        name = request.data.get('name')
        user = UserData.objects.create_user(email=email, password=password, name=name)
        data = request.data.copy()  
        data['user_id'] = user.id  
        data['type_of_user'] = 'normal_advocate'
        serializer = NormalAdvocateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": " Advocate successfully created", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message": "validation failed.. Please try again"}, status=status.HTTP_400_BAD_REQUEST)
    
    

class SuspendAdvocateView(APIView):
    def patch(self, request, id):
        try :
            advocate = Advocate.objects.get(id = id)
            serializer=NormalAdvocateSerializer(advocate)
            advocate.is_suspend = not advocate.is_suspend
            advocate.save()

            if advocate.is_suspend:
                return Response({"message" : "Advocate suspended successfully" ,"data":serializer.data}, status = status.HTTP_202_ACCEPTED)
            return Response({"message" : "Advocate suspension removed successfully" ,"data":serializer.data}, status = status.HTTP_202_ACCEPTED)

        except Advocate.DoesNotExist:
            return Response({
                "message" : "Advocate does not found"
                }, status= status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({
                "message": "An unexpected error occurred "
                
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
    

class EditAdvocateProfileView(APIView):
    def patch(self, request, id): 
        try:
            advocate=Advocate.objects.get(id=id)
            #Editing UserData Model    
            name = request.data.get('name')
            if name is not None:
                UserData.objects.filter(id=advocate.user.id).update(name=name)
            # request.data['user'] = advocate.user.id
            #Editing Advocates Model
            serializer = NormalAdvocateSerializer(advocate, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message" : "Advocate details updated sucessfully"},status=status.HTTP_200_OK)
            return Response({"message" : "Validation error"},status=status.HTTP_400_BAD_REQUEST)
        except Advocate.DoesNotExist:
            return Response({"message" : "Advocate could not be found"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message" : "An unexcepted error occured "},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AdvocateEditFormView(APIView):
    def get(self, request, id) :
        try:
            advocate=Advocate.objects.get(id=id)
            serializer=NormalAdvocateSerializer(advocate)
            return Response(serializer.data ,status=status.HTTP_200_OK)

        except Advocate.DoesNotExist:
                    return Response({
                         "message" : "Advocate  could not be found"
                         },status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
                    return Response({
                        "message": "An unexpected error occurred "  
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)