from django.views.generic import ListView,DetailView
from .models import Incident

# Create your views here.
# def incident_list(request):
#     incidents = Incident.objects.all()
#     return render(request, 'incident/incident_list.html', {'incidents':incidents})

class IncidentListView(ListView):
    model = Incident
    template_name = 'incident/incident_list.html'
    context_object_name = 'incidents'
    
class IncidentDetailView(DetailView):
    model = Incident
    template_name = 'incident/incident_form.html'
    context_object_name = 'incident'