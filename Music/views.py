from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from .models import Album, Song
from django.views import generic
from .models import Album


# Create your views here.
# def places(request):
#     all_albums = Album.objects.all()
#     # html = ''
#     # for album in all_albums:
#     #     url = '/Music/' + str(album.id) + '/'
#     #     html += '<a href="' + url + '">' + album.album_title + '</a><br>'
#     #     # return render(request, template_name='places/Places.html')
#     # return HttpResponse(html)
#     # template = loader.get_template('Music/hom.html')
#     # context = {'all_albums': all_albums}
#     # return HttpResponse(template.render(context,))
#     return render(request, 'Music/hom.html', {'all_albums': all_albums})
#
#
# def place1(request):
#     return render(request, template_name='places/place1.html')
#
#
# def detail(request, album_id):
#     # return HttpResponse('<h2>Details for Album id: ' + str(album_id) + '</h2>')
#     # try:
#     #     album = Album.objects.get(pk=album_id)
#     # except Album.DoesNotExist:
#     #     raise Http404('Album does not exist')
#     album = get_object_or_404(Album, pk=album_id)
#     return render(request, 'Music/detail.html', {'album': album})


# def favorite(request, album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     try:
#         selected_song = album.song_set.get(pk=request.POST['song'])
#     except (KeyError, Song.DoesNotExist):
#         return render(request, 'Music/detail.html', {
#             'album': album,
#             'error_message': 'You did not select a valid song',
#         })
#     else:
#         selected_song.is_favorite = True
#         selected_song.save()
#         return render(request, 'Music/detail.html', {'album': album})

class HomView(generic.ListView):
    template_name = 'Music/hom.html'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'Music/detail.html'

