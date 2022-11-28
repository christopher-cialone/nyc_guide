from django.shortcuts import render
from django.views import View

from nyc.boroughs import boroughs

# The class views correspond to urls.py, with the paths matching the view 
class CityView(View):
    def get(self, request):
        return render(request=request, template_name='city.html', context={'boroughs': boroughs.keys()})

# This represents one of the five boroughs
class BoroughView(View):
    def get(self, request, borough):
        return render(
            request=request,
            template_name='borough.html',
            context={'borough': borough, 'activities': boroughs[borough].keys()},
        )

# This represents the particular activity going on in a borough
class ActivityView(View):
    def get(self, request, borough, activity):
        return render(
             request = request, 
             template_name = 'activities.html',
             context={'activity' : activity , 'borough' : borough, 'venues': boroughs[borough][activity].keys()}
        )
       
# This represents the specific venue, site or locale
class VenueView(View):
    def get(self, request, borough, activity, venue):
        return render(
            request=request,
            template_name='venue.html',
            context={'borough' : borough, 'activity' : activity, 'venue' : venue, 'description':boroughs[borough][activity][venue].get('description')}
        )