from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.views.decorators.cache import cache_page
from django.core.exceptions import ObjectDoesNotExist

from ua_67.settings import FLICKR_API_KEY,FLICKR_SECRET,FLICKR_USERID
import flickrapi
import json
import yaml

from models import FlickR_Album

@cache_page(60 * 60 * 24)
def gallery(request):
        context= RequestContext(request)

        flickr = flickrapi.FlickrAPI(FLICKR_API_KEY,FLICKR_SECRET,format='parsed-json')
        sets = flickr.photosets.getList(user_id=FLICKR_USERID)

        for album in sets['photosets']['photoset']:
            try:
                existing_album = FlickR_Album.objects.get(flickr_id = album['id'])

                try:
                    photo_feed = flickr.photosets.getPhotos(user_id=FLICKR_USERID,photoset_id=existing_album.flickr_id)

                    existing_album.photo_feed = yaml.safe_load(json.dumps(photo_feed))
                    existing_album.save()

                except Exception as e:
                    pass

            except ObjectDoesNotExist:
                new_album = FlickR_Album.objects.create(name=album['title']['_content'],flickr_id=album['id'])
                try:
                    photo_feed = flickr.photosets.getPhotos(user_id=FLICKR_USERID,photoset_id=new_album.flickr_id)

                    new_album.photo_feed = yaml.safe_load(json.dumps(photo_feed))
                    new_album.save()

                except Exception as e:
                    print(e)

        albums_for_template = FlickR_Album.objects.all()
        context_dict = {'albums' : albums_for_template}

        return render_to_response('Union_1/gallery.html', context_dict, context)
