from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from basicapp.models import Explores,Hotels,Homestays,MalnadSpecials
app_name='basicapp'

# Create your views here.
class Baseview(TemplateView):
    template_name='html/basicapp/home_page.html'

class ContactView(TemplateView):
    template_name='basicapp/contact.html'

class ExploresListView(ListView):
    model=Explores
    def get_queryset(self):
        return Explores.objects.all().order_by('rank')

class ExploresDetailView(DetailView):
    context_object_name='place_detail'
    model=Explores
    template_name='basicapp/explores_detail.html'


class HotelsListView(ListView):
    context_object_name='hotel_list'
    model=Hotels
    def get_queryset(self):
         return Hotels.objects.all().order_by('rank')


class HotelsDetailView(DetailView):
    context_object_name='hotel'
    model=Hotels
    template_name='basicapp/hotels_detail.html'


class HomestaysListView(ListView):
    context_object_name='homestays'
    model=Homestays
    def get_queryset(self):
         return Homestays.objects.all().order_by('rank')


class HomestaysDetailView(DetailView):
    context_object_name='homestay_detail'
    model=Homestays
    template_name='basicapp/homestays_detail.html'


class MalnadSpecialsListView(ListView):
    context_object_name='malnadspecials'
    model=MalnadSpecials
    template_name='basicapp/malnadspecials_list.html'
    def get_queryset(self):
         return MalnadSpecials.objects.all().order_by('rank')


class HotelVegList(ListView):
    context_object_name='veglist'
    model=Hotels
    template_name='basicapp/veglist.html'
    def get_queryset(self):
         return Hotels.objects.all().order_by('rank')


class HotelVegDetailView(DetailView):
    context_object_name='hotel'
    model=Hotels
    template_name='basicapp/veg_detail.html'
