from books.models import Author
from books.views import login_user

class MakeUserAuthor:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # code before view
        if request.user.is_authenticated:
            try:
                request.user.author
            except Author.DoesNotExist:
                Author.objects.create(
                    user = request.user,
                    first_name = request.user.username
                )
        else:
            request.user.author = None
        # code after view    
        response = self.get_response(request)  
        return response
    

    
