from django.shortcuts import render
from .models import Retreat



def retreats(request):
    """ A view to show upcoming retreats """
    retreats = Retreat.objects.all()
    context = {
        'retreats': retreats,
    }
    return render(request, 'retreats/retreats.html', context)
