from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": 'Go to the gym every three days!',
    "february": 'Eat no meat',
    "march": "Learn Django for 1 hour every day",
    "april": "Eat no meat and drink no fizzy drinks",
    "may": "Learn new langauge 1 hour a day",
    "june": "Learn Django for 2 hours every day",
    "july": "Learn Django for 3 hours every day",
    "august": "Learn Django for 4 hours every day",
    "september": "Learn Django for 5 hours every day",
    "october": "Learn Django for 6 hours every day",
    "november": "Learn Django for 7 hours every day",
    "december": None,
}


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months,
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("This month is not supported")
    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        month_name = month
        return render(request, "challenges/challenge.html", {
            "month": month_name,
            "text": challenge_text
        })
    except:
        raise Http404()
