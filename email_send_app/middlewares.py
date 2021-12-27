from django.shortcuts import redirect
def my_middleware(get_response):
    def middleware(request):
        print("Middleware is working")
        # username = request.user.username
        # if username:
        #     print(username)
        #     return redirect('/')
        response = get_response(request)
        return response

    return middleware


"""
    For normal function
    --> for email_send_app.middlewares import my_middleware
    views.py:
    @my_middleware
    def test(request):
        st1
        st2
    For method
    --> from django.utils.decorators import method_decorator
    @method_decorator(my_middleware)
    def test(request):
        st1
        st2
"""