from django.shortcuts import render

# Create your views here.

def postszia_view(request):

    if request.method=="POST":
        print(request.POST['nev'])
        print(request.POST)
    else:
        print("ez nem post request!")


    template = "index.html"
    context = {
        'a':5,
        'b':7,
        'uzenet':'hellóka',
    }
    return render(request, template, context)