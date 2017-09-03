from django.shortcuts import render
# from django.http import HttpResponse
from first_app.models import AccessRecord, Topic, Webpage
from first_app import forms, signup


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'first_app/index.html', context=date_dict)


def basic_form_view(request):
    form = forms.BasicForm()

    if request.method == 'POST':
        form = forms.BasicForm(request.POST)

        if form.is_valid():
            print('validation success')
            print('name: ' + form.cleaned_data['name'])
            print('email: ' + form.cleaned_data['email'])
            print('text: ' + form.cleaned_data['text'])

    return render(request, 'first_app/basic_form.html', {'form': form})


def signup_view(request):
    form = signup.newWebpage()

    if request.method == 'POST':
        form = signup.newWebpage(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request, 'first_app/signup.html', {'form': form})
