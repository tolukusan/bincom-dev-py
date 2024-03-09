from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from .models import State, LGA, PollingUnit, PartyResult

def polling_unit_result(request):
    states = State.objects.all()
    lgas = PollingUnit.objects.filter(lga__state__state_name='Delta').values('lga__lga_name').distinct()

    if request.method == 'POST':
        state_name = request.POST.get('state')
        lga_name = request.POST.get('lga')
        polling_unit_number = request.POST.get('polling_unit')

        polling_unit = get_object_or_404(
            PollingUnit,
            lga__state__state_name=state_name,
            lga__lga_name=lga_name,
            polling_unit_number=polling_unit_number
        )

        results = PartyResult.objects.filter(polling_unit=polling_unit)
        return render(request, 'results/polling_unit_result.html', {'results': results})

    return render(request, 'results/polling_unit_result.html', {'states': states, 'lgas': lgas})