from django.shortcuts import render
from django.http import HttpResponse
from .models import *
def home(request):
	movie_set=Movies.objects.all()
	if(request.method=="POST"):
		if 'submit2' in request.POST:
			name=request.POST['film_name']
			yr=request.POST['date_of_release'][0:4]
			gr=request.POST['genre']
			rat=request.POST['rating']
			summ=request.POST['summary']
			Info=Movies(movie_name=name,movie_genre=gr,movie_rating=int(rat),movie_YearOfRelease=int(yr),
				movie_summary=summ)
			Info.save()
			notification="The film {} is successfully added to database".format(name)
			context={"status":notification}
			return render(request,'movies/frontpage.html',context)
		elif 'submit1' in request.POST:
			name=request.POST['search']
			for i in movie_set:
				if(i.movie_name==name):
					return render(request,'movies/movie_description.html',{'movie':i})
	movie_names=[]
	for i in movie_set:
		movie_names.append(i.movie_name)
	context={'movie_names':movie_names}
	return render(request,'movies/frontpage.html',context)
def movies(request):
	movie_set=Movies.objects.all()
	return render(request,'movies/movie_database.html',{'movie_set':movie_set})
def movie_description(request,m_name):
	movie=Movies.objects.get(id=m_name)
	return render(request,'movies/movie_description.html',{'movie':movie})
def genre_list(request,g_name):
	movie_set=Movies.objects.all()
	if(g_name=='1'):
		movie_set=Movies.objects.all().filter(movie_genre='Mystery/Thriller')
	elif(g_name=='2'):
		movie_set=Movies.objects.all().filter(movie_genre='Romance')
	elif(g_name=='3'):
		movie_set=Movies.objects.all().filter(movie_genre='Horror')
	elif(g_name=='4'):
		movie_set=Movies.objects.all().filter(movie_genre='Comedy')
	elif(g_name=='5'):
		movie_set=Movies.objects.all().filter(movie_genre='Documentary')
	elif(g_name=='6'):
		movie_set=Movies.objects.all().filter(movie_genre='Random')
	return render(request,'movies/genrewiselist.html',{'genre_movies':movie_set})