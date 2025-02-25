from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
    'december': None
}

# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('Invalid month !')
    
    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenges.html", {
            "text": challenge_text,
            "month_name": month.capitalize()
        })
    except:
        return HttpResponseNotFound('<h1>this month is not supported !</h1>')
    
