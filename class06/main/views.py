from django.shortcuts import render
from datetime import datetime

# Create your views here.


# def learn_django(request):
# named argument
#     return render(template_name="main/index.html", request=request, context={'name': 'kshittiz'})


# def learn_django(request):
#     context = {'name': 'Unnati'}
#     # positional argument
#     return render(request, "main/index.html", context)


# def learn_django(request):
#     # filter
#     context = {'des': 'Nepal is beautiful country'}
#     # positional argument
#     return render(request, "main/index.html", context)


# def learn_django(request):
#     # datetime
#     today_datatime = datetime.now()

#     context = {
#         'name': 'unnati',
#         'dob': today_datatime,
#         'price': 20.0077,
#     }

#     return render(request, "main/index.html", context)
