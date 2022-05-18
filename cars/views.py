from django.contrib import messages
from .forms import CarsForm
from django.shortcuts import render
from .models import Cars
from django.views import View
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


class CarListView(ListView):
    paginate_by = 2
    model = Cars
    filterset_class = None
    template_name = 'cars/home.html'

    def get(self, request, *args, **kwargs):

        queryset = self.get_queryset()
        if self.request.GET.get('make'):
            queryset = queryset.filter(make=self.request.GET.get('make'))
        if self.request.GET.get('year'):
            queryset = queryset.filter(year__year=self.request.GET.get('year'))

        paginator = Paginator(queryset, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        car_make_list = set(self.get_queryset().values_list('make', flat=True))
        car_year_list = set(
            self.get_queryset().values_list('year__year', flat=True))
        return render(request, self.template_name, {'page_obj': page_obj, 'car_make_list': car_make_list, 'car_year_list': car_year_list})


class CarAddView(View):
    form_class = CarsForm
    template_name = 'cars/add_car.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(None)
        # cars = Cars.objects.all()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            messages.success(request, 'Form submission successful')
            form.save()
            # <process form cleaned data>
            return render(request, 'cars/thankyou.html', {'form': form})

        return render(request, self.template_name, {'form': form})


class CarBuyView(View):
    template_name = "cars/buy_car.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        car_obj = get_object_or_404(Cars, pk=self.kwargs.get('id'))
        if car_obj.is_sell:
            messages.success(request, 'car is already sold')
        else:
            car_obj.is_sell = True
            car_obj.save()
            messages.success(request, 'Iron mike will be in touch')
            commission_ammount = (5 * car_obj.price) / 100
            email_context = {
                "seller_name": car_obj.seller_name,
                "seller_mob": car_obj.seller_mob,
                "make": car_obj.make,
                "model": car_obj.model,
                "year": car_obj.year,
                "condition": car_obj.condition,
                "price": car_obj.price,
                "buyer_name": request.POST.get('buyer_name'),
                "buyer_contact": request.POST.get('buyer_contact'),
                "commission": commission_ammount,
                "final_amount": car_obj.price - commission_ammount
            }
            # msg_plain = render_to_string('templates/email.txt', {'some_params': some_params})
            msg_html = render_to_string(
                'cars/car_buy_inquiry_email.html', email_context)

            send_mail(
                subject='Vehicle inquiry',
                message="message",
                from_email="ghans.dudhatra@gmail.com",
                recipient_list=[settings.ADMIN_EMAIL],
                html_message=msg_html,
            )
        return render(request, 'cars/thankyou.html', {})


def buy_car(request, id):
    car_obj = get_object_or_404(Cars, pk=id)
    car_obj.is_sell = True
    car_obj.save()
    return HttpResponseRedirect('/')


def available_car(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied()

    car_obj = get_object_or_404(Cars, pk=id)
    car_obj.is_sell = False
    car_obj.save()
    return HttpResponseRedirect('/')
