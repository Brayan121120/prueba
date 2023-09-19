from django.shortcuts import render
from rest_framework.views import A

# Create your views here.
class Home(APIView):
    template_name="index.html"
    def get(self,request):
        return render(request,self.template_name)        
