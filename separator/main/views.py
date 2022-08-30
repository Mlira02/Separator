from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<head><title>DP Separator</title></head><body style="background-color:black;"><header style="background-color:white; margin:20px;"><h2>DP Separator</h2></header><div style="width:100%;height:0;padding-bottom:60%;position:relative; display:flex; justify-content:center; border-radius:25px;"><iframe src="https://giphy.com/embed/z6EG2su1f5jOTourNL" width="50%" height="50%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div></body>')