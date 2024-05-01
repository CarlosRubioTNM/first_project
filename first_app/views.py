from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord, User
from . import forms
import requests
import json

def get_json_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()  # Converts the JSON response to a Python dictionary
    except requests.RequestException as e:
        print(e)
        return None

# Create your views here.
def index(request):
    result = get_json_from_url("https://ybew6fpgvatiigak2vg2hlwoei0fkzxf.lambda-url.us-west-2.on.aws/")
    print(result)
    webpages_list = AccessRecord.objects.order_by('date')
    users_list = User.objects.order_by('first_name')
    date_dict = {'access_records' : webpages_list,
                 'users': users_list,
                 'result': result[0]['tasks']}
    my_dict = {'insert_me': "Hola!, ahora soy de first_app/views.py"}
    return render(request, 'first_app/index.html', context=date_dict)
    #return HttpResponse("Hello World!")

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("VALIDATION SUCCESS!")
            local_first_name = form.cleaned_data['name']
            local_last_name = ''
            local_mail = form.cleaned_data['email']
            
            t = User.objects.get_or_create(first_name=local_first_name, last_name=local_last_name, email=local_mail)[0]
            t.save()
            print("Name:",form.cleaned_data['name'])
            print("Email:",form.cleaned_data['email'])
            print("Text:",form.cleaned_data['text'])
    return render(request, 'first_app/form_page.html', {'form': form})

def otro(request):
    return render(request, 'first_app/otro.html')