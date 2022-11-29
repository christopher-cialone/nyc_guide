from django.shortcuts import render
from django.views import View

from nyc.boroughs import boroughs


class CityView(View):
    '''The class views correspond to urls.py, with the paths matching the view '''
    def get(self, request):
        return render(request=request, template_name='city.html', context={'boroughs': boroughs.keys()})


class BoroughView(View):
    '''This represents one of the five boroughs'''
    def get(self, request, borough):
        return render(
            request=request,
            template_name='borough.html',
            context={'borough': borough, 'activities': boroughs[borough].keys()},
        )

# 
class ActivityView(View):
    '''This represents the particular activity going on in a borough'''
    def get(self, request, borough, activity):
        return render(
             request = request, 
             template_name = 'activities.html',
             context={'activity' : activity , 'borough' : borough, 'venues': boroughs[borough][activity].keys()}
        )
       

class VenueView(View):
    '''This represents the specific venue, site or locale'''
    def get(self, request, borough, activity, venue):
        return render(
            request=request,
            template_name='venue.html',
            context={'borough' : borough, 'activity' : activity, 'venue' : venue, 'description':boroughs[borough][activity][venue].get('description')}
        )