from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import PollingUnit, AnnouncedPuResults

def polling_unit_result(request):
    my_results = AnnouncedPuResults.objects.all().filter(polling_unit_uniqueid=8)
    return render(request, 'results/index.html', {'my_results':my_results})
