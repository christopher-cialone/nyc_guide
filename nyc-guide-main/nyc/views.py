from django.shortcuts import render
from django.views import View

from nyc.boroughs import boroughs


class CityView(View):
    def get(self, request):
        return render(request=request, template_name='city.html', context={'boroughs': boroughs.keys()})


class BoroughView(View):
    def get(self, request, borough):
        return render(
            request=request,
            template_name='borough.html',
            context={'borough': borough, 'activities': boroughs[borough].keys()},
        )


class ActivityView(View):
    def get(self, request, borough, activity):
        return render(
             request = request, 
             template_name = 'activities.html',
             context={'activity' : activity , 'borough' : borough, 'venues': boroughs[borough][activity].keys()}
        )
       

# Added this, but too be honest Im not quite sure of myself here, also added the venue.html file to coinside with this
class VenueView(View):
   def get(self, request, borough, activity, venue):
        return render(
            request = request,
            template_name= 'venue.html',
            context={'venues' :  boroughs[borough][activity].keys(), 'borough' : borough }
        )
