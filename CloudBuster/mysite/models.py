from django.db import models

class MovieUser(models.Model):
  fName = models.CharField(max_length=50)
  lName = models.CharField(max_length=50)
  emailAddr = models.EmailField(max_length=254)
  def __str__(self):
    return self.fName


class Movie(models.Model):
  title = models.CharField(max_length=200)
  inStock = models.IntegerField()
  total = models.IntegerField()
  def __str__(self):
    return self.title


class CheckoutDB(models.Model):
  user = models.ForeignKey(MovieUser,  on_delete=models.CASCADE)
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  def __str__(self):
    return self.movie.title