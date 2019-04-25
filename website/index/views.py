import psycopg2
import json

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


conn = psycopg2.connect("dbname=omnidbwebsite user=postgres")


def index(request):


    cur = conn.cursor()

    cur.execute("SELECT * FROM public.documentation;")

    result = cur.fetchall()

    items = [];

    for item in result:
        items.append(
            {
                'title' : item[0],
                'description' : item[1],
                'text' : item[2]
            }
        )


    data = {
        'content_sections': [
            {
                'id': 'omnidb-highlights',
                'wrap_type': 'container-fluid',
                'content': '<p>Conteúdo da documentação</p>'
            }
        ]
    }

    widgets = None;

    context = {
        'data': data,
        'widgets': widgets
    }

    template = loader.get_template('home.html')

    return HttpResponse(template.render(context, request))




def documentation(request):

    cur = conn.cursor()

    cur.execute("SELECT * FROM public.documentation;")

    result = cur.fetchall()

    items = [];

    for item in result:
        items.append(
            {
                'title' : item[0],
                'description' : item[1],
                'text' : item[2]
            }
        )

    data = {
        'content_sections': [
            {
                'id': 'omnidb-highlights',
                'wrap_type': 'container-fluid',
                'content': items
            }
        ]
    }

    widgets = {
        'sidebar': {
            'position': 'right',
            'items': [ {'title': item['title']} for item in items ]
        }
    }

    context = {
        'data': data,
        'widgets': json.dumps( widgets )
    }

    template = loader.get_template('documentation.html')

    return HttpResponse(template.render(context, request))
