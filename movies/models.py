from django.db import models
class Movies(models.Model):
	movie_genre_choices=[
	('Mystery/Thriller','Mystery/Thriller'),
	('Romance','Romance'),
	('Horror','Horror'),('Comedy','Comedy'),('Documentary','Documentary'),('Random','Random')]
	movie_name=models.CharField(max_length=200)
	movie_genre=models.CharField(max_length=75,choices=movie_genre_choices,default="Random")
	movie_rating=models.IntegerField()
	movie_YearOfRelease=models.IntegerField()
	movie_summary=models.CharField(max_length=500)
	def __str__(self):
		return self.movie_name

