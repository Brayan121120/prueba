from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse

class Home(APIView):
     template_name="index.html"
def get(self,request):
    return render(request,self.template_name)

