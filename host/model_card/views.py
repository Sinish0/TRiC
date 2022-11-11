from django.shortcuts import render



def home(request):
    return render(request, "model_card/index.html", {})


def generate_text(request):
    return render(request, "model_card/generate_text.html", {})


def about(request):
    return render(request, "model_card/about.html")
