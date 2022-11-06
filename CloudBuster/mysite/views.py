from django.views import View 
from django.http import JsonResponse
from django.shortcuts import render
from .models import MovieUser, Movie, CheckoutDB

class Home(View):
  def get(self, request):
    return render(request,"home.html")
  def post(self, request):
    return render(request,"home.html")

class Account(View):
  def get(self, request):
    user = MovieUser.objects.all().values()
    return render(request,"account.html",{"user":user})


class AccountHandler(View):
  def get(self, request):
    return JsonResponse({})
  def post(self, request):
    email=request.POST["email"]
    success = "false"
    if not (MovieUser.objects.filter(emailAddr=email).exists()):
      success = "true"
      u = MovieUser(fName=request.POST["fName"],lName=request.POST["lName"],emailAddr=request.POST["email"])
      u.save()
    print(success)
    return JsonResponse({"success":success}, safe=False)



class Manage(View):
  def get(self, request):
    movies = Movie.objects.all().values()
    return render(request,"manage.html",{"movies":movies})
  def post(self, request):
    m = Movie(title=request.POST["add"],instock=1)
    m.save()
    movies = Movie.objects.all().values()
    return render(request,"manage.html",{"movies":movies})

class ManageHandler(View):
  def get(self, request):
    movies = list(Movie.objects.all().values().order_by('title'))
    print(movies)
    return JsonResponse(movies, safe=False)
  def post(self, request):
    title = request.POST["add"].strip()
    error=title+" has been added!"
    if not title:
        error = "You must enter a valid movie title!"
    elif Movie.objects.filter(title=title).exists():
        error = "Movie already exists"
    else:
      m = Movie(title=title,inStock=1,total= 0)
      m.save()
    return JsonResponse({"error":error})

class ManageStock(View):
  def post(self, request):
    title = request.POST["title"]
    stock = request.POST["stock"]
    action = request.POST["value"]
    if  Movie.objects.filter(title=title).exists():
      if action == "-":
        m = Movie(title=title,inStock= stock - 1,total= 0)
        m.save()
      if action == "+":
        m = Movie(title=title,inStock= stock + 1,total= 0)
        m.save()
    return JsonResponse({})


class Checkout(View):
  def get(self, request):
    movies = list(Movie.objects.all().values().order_by('title'))
    print(movies)
    return render(request,"checkout.html",{"movies":movies})
  def post(self, request):
    email=request.POST["email"]
    exists = "false"
    if (MovieUser.objects.filter(emailAddr=email).exists()):
      exists = "true"
      u = MovieUser.objects.get(emailAddr=email)
      if (CheckoutDB.objects.filter(user=u.id).exists()):
        print("Checkouts Found")
        userMovies = list(CheckoutDB.objects.filter(user=u.id).values())
        print(userMovies)
        return JsonResponse({"exists":exists, "fName":u.fName, "lName":u.lName,"movies":str(userMovies)}, safe=False)
      return JsonResponse({"exists":exists, "fName":u.fName, "lName":u.lName}, safe=False)
    
    return JsonResponse({"exists":exists}, safe=False)

class CheckoutHandler(View):
  def get(self, request):
    movies = list(Movie.objects.all().values().order_by('title'))
    print(movies)
    return JsonResponse(movies, safe=False)
  def post(self, request):
    email=request.POST["email"]
    movieToCheck=request.POST["movie"]
    exists = "false"
    print(movieToCheck)
    if (MovieUser.objects.filter(emailAddr=email).exists()):
      exists = "true"
      u = MovieUser.objects.get(emailAddr=email)
      m = Movie.objects.get(title=movieToCheck)
      if (movieToCheck):
        print(m)
        x = CheckoutDB(user=u, movie=m)
        x.save()
      return JsonResponse({"exists":exists, "fName":u.fName, "lName":u.lName}, safe=False)
    return JsonResponse({"exists":exists}, safe=False)



