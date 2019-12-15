from django.http import HttpResponse
from osmdatamodel.models import Nodes

def nodes(request):

    points = Nodes.objects.all()

    return HttpResponse(points)
