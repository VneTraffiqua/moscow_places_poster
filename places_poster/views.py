from django.http import HttpResponse


def show_index(request):
    return HttpResponse('Здесь будет карта')