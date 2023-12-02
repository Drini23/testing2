from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse , Http404
from .models import Movie

# Create your views here.


#def index(request):
  #  return HttpResponse("Hello World!")


#def index(request): # kete e perdoim per te mare info nga database 
 #   movies = Movie.objects.all()
  #  output = ', '.join([m.title for m in movies])
   # return HttpResponse(output)

def index(request):
    movies = Movie.objects.all()
    return render(request, 'filma/index.html', {'movies': movies})


def detail(request, movie_id ):
    
      movie = get_object_or_404(Movie,pk = movie_id) # PERDORIM GET_OBJECT_OR_404 QE MOS TE NA SHFAQET ERROR POR 404 PAGE NOT FOUND 
      return render(request, 'filma/detail.html', {'movie': movie})
