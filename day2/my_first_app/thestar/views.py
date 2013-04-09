from django.shortcuts import render_to_response
from thestar.models import Competitor, Vote
from django.http import HttpResponse

def home(request):
    template = 'home.html'

    competitors = Competitor.objects.all()
    data = {'competitors': competitors}
    return render_to_response(template, data)

def vote(request):
    no = request.GET['no']
    competitor = Competitor.objects.get(no=no)
    vote = Vote()
    vote.competitor = competitor
    vote.save()
    return HttpResponse('OK')
