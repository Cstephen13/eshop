from .models import Link
"""
    funciones para menejar los procesadores de contexto
"""


def context_dict(request):
    context = {}
    links = Link.objects.all()
    for link in links:
        context[link.key] = link.url

    return context

