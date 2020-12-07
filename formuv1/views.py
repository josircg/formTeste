from django.shortcuts import render

from .forms import FormDinamico


def form_teste(request):

    if request.POST:
        form = FormDinamico(request.POST)
        print(form.data)

    else:
        form = FormDinamico()
    return render(request, 'revista/form.html', { 'form': form })