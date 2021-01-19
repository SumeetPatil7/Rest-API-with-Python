from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Update
from django.views.generic import View
from cfeapi.mixins import JsonResponseMixin
import json
# Create your views here.
def update_model_detail_view(request):
    '''
    Uniform resource Locator
    GET - Retrive data
    '''
    data={
        "count":100,
        "content":"Some content"
    }
    return JsonResponse(data)

class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        '''
        Uniform resource Locator
        GET - Retrive data
        '''
        data={
            "count":100,
            "content":"Some content"
        }
        json_data=json.dumps(data,)
        return HttpResponse(json_data,content_type="application/json")



class JsonCBV2(JsonResponseMixin,View):
    def get(self,request,*args,**kwargs):
        data={
            "count":100,
            "content":"XYZ"
        }
        return self.render_to_json_response(data)