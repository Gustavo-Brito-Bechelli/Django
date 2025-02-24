from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = 'Walk for at least 20 minuts avery day!'
    elif month == 'february':
        challenge_text = 'Study Django for 20 min every day'
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)
