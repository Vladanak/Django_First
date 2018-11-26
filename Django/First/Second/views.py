from django.http import HttpResponse


def Hello(request):
    return HttpResponse('<p>Darova</p>')