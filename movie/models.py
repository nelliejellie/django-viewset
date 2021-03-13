from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=300)

    # get the number of people who rated the movie
    def no_of_rating(self):
        ratings = Rating.objects.filter(movie=self) # returns an array
        return len(ratings)

    def avg_rating(self):
        sum = 0
        ratings = Rating.objects.filter(movie=self) # returns an array
        for rating in ratings:
            sum+=rating.star
        if len(ratings) > 0:
            return sum/len(ratings)
        else:
            return 0
    
    def __str__(self):
        return self.title

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # used to limit the integer to 1 and 5
    star = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)] )

    class Meta:
        # user cant rate the same movie twice
        unique_together = (('user', 'movie'))
        index_together = (('user', 'movie'))