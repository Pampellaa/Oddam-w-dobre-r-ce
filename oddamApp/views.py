from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
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

        # if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        #     html_content = render_to_string('ajax_content.html', ctx)
        #     html_pagination = render_to_string('ajax_pagination.html', ctx)
        #     return JsonResponse({'html_content': html_content, 'html_pagination': html_pagination})

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
    def post(self, request):
        username = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('name')
        last_name = request.POST.get('surname')
        user = User.objects.create(username=username, first_name=first_name, last_name=last_name, email=username)
        user.set_password(password)
        user.save()
        login(request, user)
        return redirect('login')

