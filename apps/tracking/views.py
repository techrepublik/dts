from django.shortcuts import render,redirect, get_object_or_404
from django.template.loader import render_to_string, get_template
from django.http import HttpResponse, JsonResponse
from apps.user.models import Agency


# Create your views here.

def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html')

