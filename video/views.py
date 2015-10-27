from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm


from video.models import Video
from .forms import LoginForm

# Create your views here.


def home(request):
    last_video = Video.objects.all().order_by("-id")[0]
    return render(request, 'index.html', {'last_video': last_video})
    # return HttpResponse("Hello world")



def login(request):

    if request.method == "POST":
        # username = request.POST.get('username', None)
        # password = request.POST.get('password', None)
        #
        # if username is not None and password is not None and username !='' and password !='':
        #     user = authenticate(username=username, password=password)
        #     if user:
        #         return redirect('/')
        #     else:
        #         return HttpResponse("Login failed!")
        # else:
        #     return HttpResponse("Empty value detected")


        form = LoginForm(request.POST)
        user = form.authenticate()
        if user:
            return redirect("/")
        else:
            return HttpResponse("Login failed or form invalid!")



    else:
        form = LoginForm()
        return render(request, "login.html", {'form': form})

    return render(request, 'login.html')



def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user:
                return HttpResponse("User ID: " + str(user.id) + " created")
            else:
                return HttpResponse("User creation failed")
    else:
        form = UserCreationForm()


    return render(request, 'signup.html', {'form': form})







from django.views.generic.base import TemplateView
import video.models as videomodel
class LandingView(TemplateView):
    model = videomodel.Video
    template_name = "index.html"

