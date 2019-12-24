def my_middleware1(get_response):
    print('chushi')
    def middleware1(request):
        get_response(request)
