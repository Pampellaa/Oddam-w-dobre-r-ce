from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Sum
from django.shortcuts import render
from django.views import View

from oddamApp.models import Donation, Institution


class LandingPageView(View):
    def get(self, request):
        total_bags = Donation.objects.aggregate(total_bags=Sum('quantity'))['total_bags']
        supported_organizations = Institution.objects.count()

        fundations = Institution.objects.filter(type=1)
        paginator = Paginator(fundations, 5)
        page = request.GET.get('page')
        fundations_page = paginator.get_page(page)

        organizations = Institution.objects.filter(type=2)
        paginator = Paginator(organizations, 5)
        page = request.GET.get('page')
        organizations_page = paginator.get_page(page)

        collections = Institution.objects.filter(type=3)
        paginator = Paginator(collections, 5)
        page = request.GET.get('page')
        collections_page = paginator.get_page(page)

        ctx = {'total_bags': total_bags, 'supported_organizations': supported_organizations, 'fundations': fundations,
              'fundations_page':fundations_page, 'organizations_page': organizations_page, 'collections_page': collections_page }
        return render(request, 'index.html', ctx)

class AddDonationView(View):
    def get(self, request):
        return render(request, 'form.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

