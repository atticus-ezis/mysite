from django.http import HttpResponse, Http404
from django.shortcuts import render
import datetime

from django.template.loader import get_template

def index(request):
    return HttpResponse('Hello world!')

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, "current_datetime.html", {"now":now})

def hours_ahead(request, offset):
    try:
        # test_string = "this is a test"
        # breakpoint()
        offset_value = int(offset)
    except ValueError:
        return Http404
    
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset_value)
    html = "<html><body>It will be {}.</body></html>".format(dt)
    return HttpResponse(html)


# Exercises
    
def sum(request, number_1, number_2):
    final_sum = int(number_1) + int(number_2)
    result = f"The sum of {number_1} and {number_2} is {final_sum}"
    return render(request, "exercise1.html", {"result":result})

def date_check(request, year, month, day):
    date_string = f"{str(year)}/{str(month)}/{str(day)}"
    try:
        datetime.datetime.strptime(date_string, "%Y/%m/%d")
        html = "<html><body>{} is correct format YYYY/MM/DD</body></html>".format(date_string)
        result = f"{date_string} is correct format"
    except ValueError:
        html = "<html><body>{} is incorrect format. Expected YYYY/MM/DD</body></html>".format(date_string)
        result = f"{date_string} is incorrect format. Expected YYYY/MM/DD"
        
    return render(request, "exercise2.html", {"result":result})