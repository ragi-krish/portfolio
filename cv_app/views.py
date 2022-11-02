
from multiprocessing import context
from django.shortcuts import render
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
import mimetypes
import os
from cv_app.models import CvModel
from portfolio_ragi.settings import BASE_DIR
# Create your views here.
def home(request):
    mydata = CvModel.objects.all()
    context = {'mydata':mydata}
    return render(request,'index.html',context)
#def downloadfile(request):
    #BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #filename = 'RAGIKRISHNA.pdf'
    #filepath = BASE_DIR + '/Files/' + filename
    #thefile = filepath
    #filename = os.path.basename(thefile)
    #chunk_size = 8192
    #response = StreamingHttpResponse(FileWrapper(open(thefile,'rb'),chunk_size),
     #   content_type=mimetypes.guess_type(thefile)[0])
    #response['Content-Length'] = os.path.getsize(thefile)
    #response['Content-Disposition'] = "Atachment;filename=%s" % filename
    #return response