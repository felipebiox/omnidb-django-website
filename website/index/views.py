from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.

def index(request):
    #return HttpResponse('And so it begins...')

    data = {
        'content_sections': [
            {
                'id': 'omnidb-highlights',
                'wrap_type': 'container-fluid',
                'content': '<p>Aqui vai um conteúdo</p>'
            },
            {
                'id': 'omnidb-overview',
                'wrap_type': 'container-fluid',
                'content': '<p>Aqui vai um conteúdo</p>'
            },
            {
                'id': None,
                'content': '<p>Aqui vai um conteúdo</p>'
            }
        ]
    }
    context = {
        'data': data
    }

    template = loader.get_template('base.html')

    return HttpResponse(template.render(context, request))
