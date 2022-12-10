from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for entire month!!!",
    "february": "Walk for atleast 20 minutes every day",
    "march": "Learn Django for atleast 20 minutes every day",
    "april": "Work Breaks into Your Daily Routine",
    "may": "Make One New Connection a Week",
    "june": "Meal Prep Your Lunch",
    "july": "Avoid Social Media While Working",
    "august": "Pay In Cash Only",
    "september": "No Retail Shopping",
    "october": " Try a No-Spend Month",
    "november": " Track Your Spending",
    "december": "Zero Eating Out"
}


def index(response):
    months = "<ul>"
    for month in list(monthly_challenges.keys()):
        month_path = reverse("month-challenge", args=[month])
        months += f"<li><h1><a href='{month_path}'>{month.capitalize()}</a></h1></li>"

    months += "</ul>"
    return HttpResponse(months)


def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>You've entered the invalided month!!!</h1>")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])

    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenges_text = monthly_challenges[month]
        response_data = f"<h1>{challenges_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>You've entered the invalided month!!!</h1>")
