# def my_middleware(get_resaponse):
#     print('init 调用')
#     def middleware(request):
#         print('视图前')
#         response=get_resaponse(request)
#         print("视图后")
#         return  response
#     return middleware