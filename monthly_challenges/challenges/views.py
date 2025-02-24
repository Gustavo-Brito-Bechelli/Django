from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    'january': 'Eat no meat for the entire month !',
    'february': 'Walk for at least 20 minuts avery day !',
    'march': 'Study Django for 20 min every day !',
    'april': 'Eat no meat for the entire month !',
    'may': 'Walk for at least 20 minuts avery day !',
    'june': 'Study Django for 20 min every day !',
    'july': 'Eat no meat for the entire month !',
    'august': 'Walk for at least 20 minuts avery day !',
    'september': 'Study Django for 20 min every day !',
    'october': 'Eat no meat for the entire month !',
    'november': 'Walk for at least 20 minuts avery day !',
    'december': 'Study Django for 20 min every day !'
}

# Create your views here.

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('Invalid month !')
    
    redirect_month = months[month - 1]
    return HttpResponseRedirect('/challenges/' + redirect_month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound('this month is not supported')
    return HttpResponse(challenge_text)
