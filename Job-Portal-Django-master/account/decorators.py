from django.http import HttpResponseForbidden

def user_is_employee(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == "employee":
            return function(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You do not have permission to access this page.")
    return wrap
