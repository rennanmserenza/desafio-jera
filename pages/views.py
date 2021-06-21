from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"

    def film_list(request):
        return render(request, 'templates/home.html')