from django.http import HttpResponse, Http404
import datetime

def index(request):
    return HttpResponse('Hello world!')

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

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
    
def sum(request, number_1, number_2):
    final_sum = int(number_1) + int(number_2)
    html = "<html><body>Sum is {}.</body></html>".format(final_sum)
    return HttpResponse(html)

def date_check(request, year, month, day):
    date_string = f"{str(year)}/{str(month)}/{str(day)}"
    try:
        datetime.datetime.strptime(date_string, "%Y/%m/%d")
        html = "<html><body>{} is correct format YYYY/MM/DD</body></html>".format(date_string)
    except ValueError:
        html = "<html><body>{} is incorrect format. Expected YYYY/MM/DD</body></html>".format(date_string)
        
    return HttpResponse(html)