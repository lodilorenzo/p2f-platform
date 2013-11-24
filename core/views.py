from django.http import HttpResponse
from django.template import RequestContext, loader

from core.models import Project

LIMIT_LAST_PROJECTS = 5


def index(request):
    latest_prj_list = Project.objects.order_by('-creation_date')[:LIMIT_LAST_PROJECTS]
    template = loader.get_template('core/index.html')

    # Stampa dei titoli dei progetti separati da virgola
    # output = ', '.join([p.title for p in latest_prj_list])

    context = RequestContext(request, {
        'latest_prj_list': latest_prj_list,
    })
    return HttpResponse(template.render(context))


def project(request, prj_id):
    prj = Project.objects.get(pk=prj_id)
    return HttpResponse("You are viewing the details of %s." % prj.title)