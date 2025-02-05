from django.shortcuts import render

# Create your views here.
def home(request):
  '''
  this is our home page view
  '''
  
  return render(request, 'main/index.html')

def dashboard(request):
  '''
  this function is responsible to dashbord view
  '''
  return render(request, 'main/dashboard.html')

def our_history(request):
  '''
  this is history page view
  '''
  return render(request, 'main/our-history.html')


def services(request):
  '''
  this is services page view
  '''
  return render(request, 'main/services.html')

def contactus(request):
  '''
  this is contactus page view
  '''
  return render(request, 'main/contact-us.html')


def news_notices(request):
  '''
  this is news notices page view
  '''
  return render(request, 'main/news-notice.html')