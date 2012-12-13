from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

def index(request):
    if request.method == "POST":
        text = request.POST['text']
        rot13 = text.encode('rot13')
        return render_to_response('rot13/rot13-index.html', {'text':rot13}, context_instance=RequestContext(request))
    return render_to_response('rot13/rot13-index.html', context_instance=RequestContext(request))