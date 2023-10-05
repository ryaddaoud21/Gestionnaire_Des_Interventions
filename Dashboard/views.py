import calendar
from datetime import datetime, date, timedelta

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Sum
from django.shortcuts import redirect
from .models import *
from django.shortcuts import render
from .forms import InterventionForm, SignUpForm,ClientForm
from django.dispatch import receiver
from django.db.models.signals import (post_save,)


def page_not_found_view(request, exception):
    return render(request, 'Dashboard/error-404.html',status=404)

def list_interventions(request):
    date = datetime.now().date()
    print(date)
    interventions = Intervention.objects.all()

    reclamation = Reclamation.objects.all()

    context={'interventions':interventions ,'reclamations':reclamation, 'date':date}
    return render(request, 'Dashboard/list_intervetions.html',context)

def list_reclamations(request):
    date = datetime.now().date()
    print(date)
    interventions = Intervention.objects.all()

    reclamations = Reclamation.objects.all()

    context={'interventions':interventions ,'reclamations':reclamations, 'date':date}
    return render(request, 'Dashboard/list_reclamation.html',context)

def users_profile(request):
    date = datetime.now().date()
    print(date)
    interventions = Intervention.objects.all()
    context={'interventions':interventions , 'date':date}
    return render(request, 'Dashboard/users-profile.html',context)
import geocoder
import folium
def intervention_detail(request,pk):
    int = Intervention.objects.get(pk=pk)
    date = datetime.now().date()
    print(date)
    interventions = Intervention.objects.all()


    addresses= int.Address
    location = geocoder.osm(addresses)
    lat = location.lat
    lng = location.lng
    country = location.country
    map = folium.Map(location=[45,5],zoom_start=6)
    folium.Marker([lat,lng],tooltip='Cliquer pour plus de détails',popup=country).add_to(map)

    map =map._repr_html_()
    context={'int':int , 'date':date,'map':map}
    return render(request, 'Dashboard/intervention_detail.html',context)



def list_techniciens(request):
    date = datetime.now().date()
    print(date)
    techs = Technicien.objects.all()
    print(techs)
    context={ 'date':date,'techs':techs}
    return render(request, 'Dashboard/list_techniciens.html',context)

def list_interventions_enattente(request):
    interventions = Intervention.objects.all()
    context={'interventions':interventions}
    return render(request, 'Dashboard/list_intervetions_enattente.html',context)

def list_interventions_effectuees(request):
    interventions = Intervention.objects.all()
    context={'interventions':interventions}
    return render(request, 'Dashboard/list_intervetions_effectuees.html',context)

def clients(request):
    clients = Client.objects.all()
    interventions = Intervention.objects.all()
    context={'clients':clients,'interventions':interventions}
    return render(request, 'Dashboard/list_clients.html',context)

def list_interventions_historique(request):
    interventions = Intervention.objects.all()
    context={'interventions':interventions}
    return render(request, 'Dashboard/list_intervetions_historique.html',context)
from django.contrib import messages #import messages



def ajouter_intervention(request):
    if request.method == 'POST':
        form = InterventionForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('list_interventions_historique')
            messages.success(request, "Message sent.")

    else:
        form = InterventionForm()
    techs = UserProfile.objects.all()
    context= {'form': form , 'techs':techs}
    return render(request, 'Dashboard/ajouter_intervention.html',context)

def ajouter_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('clients')
    else:
        form = ClientForm()
    techs = UserProfile.objects.all()
    context= {'form': form , 'techs':techs}
    return render(request, 'Dashboard/ajouter_client.html',context)



def get_intervention_addresses(request):
    interventions = Intervention.objects.all()
    addresses = [intervention.Address for intervention in interventions if intervention.Address]
    return addresses


from geopy.geocoders import Nominatim


@login_required
def index(request):
    geolocator = Nominatim(user_agent="Dashboard")
    location = geolocator.geocode("France")
    if location:
        print(location.address)
    else:
        print("Adresse non trouvée")

    interventions = Intervention.objects.all()
    coordinates = []

    for intervention in interventions:
        if intervention.Address:
            location = geolocator.geocode(intervention.Address)
            if location:
                coordinates.append([location.latitude, location.longitude])
    interventions = Intervention.objects.all()
    Total_C = Client.objects.all().count()
    Total_I = Intervention.objects.all().count()
    Total_U = UserProfile.objects.all().count()



    Total_CA = Intervention.objects.filter(Status="en attendant").count()
    Total_IA = Intervention.objects.filter(Status="Fait").count()
    Total_UA = Intervention.objects.filter(Status="annulée").count()

    labels = []
    data = []
    data_ints = []
    labels_ints = []
    labels.append(' En attentes')
    labels.append(' Faites')
    labels.append(' Annulées ')
    data.append(Total_CA)
    data.append(Total_IA)
    data.append(Total_UA)

    queryset = Intervention.objects.values('Date').annotate(interventions=Sum('valeur'))

    for entry in queryset:
        labels_ints.append(entry['Date'])
        data_ints.append(entry['interventions'])




    context={'interventions':interventions,'Total_I':Total_I,'Total_C':Total_C,'Total_U':Total_U, 'labelz': labels,
        'data': data,'data_ints':data_ints,'labelz_ints':labels_ints,'coordinates': coordinates}
    return render(request, 'Dashboard/index.html',context)




# views.py

from .models import Notification



@receiver(post_save, sender=Reclamation)
def create_intervention(sender, instance, created, **kwargs):
    if created and not instance.intervention_cree:
        intervention = Intervention(
            Nom_Client=instance.Nom_Client,
            Numéro=instance.Numéro,
            Ville=instance.Ville,
            Address=instance.Address,
            Code_postal=instance.Code_postal,
            Commentaire=instance.Details,
            # Remplissez les autres champs d'intervention ici
        )
        intervention.save()
        instance.intervention = intervention
        instance.intervention_cree = True
        instance.save()



@receiver(post_save, sender=Reclamation)
def create_notification(sender, instance, created, **kwargs):
    if created :
        notification = Notification(
            username=instance.Nom_Client,
            message="Nouvelle réclamation ajoutée."
        )
        notification.save()
        instance.notification = notification
        instance.save()


def population_chart(request):
    labels = []
    data = []

    queryset = Intervention.objects.values('Date').annotate(jour_total=Sum('valeur'))
    for entry in queryset:
        labels.append(entry['Date'])
        data.append(entry['jour_total'])
    return JsonResponse(data={ 'labels': labels, 'data': data, })


from django.db.models import Sum
from django.http import JsonResponse







def log_in(request):
    if request.method == 'POST':
        form1 = AuthenticationForm(request=request, data=request.POST)
        if form1.is_valid():
            username = form1.cleaned_data.get('username')
            password = form1.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                 login(request, user)
                 return redirect('index')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form1 = AuthenticationForm()
    context = {'form1': form1}

    return render(request, 'Dashboard/login.html', context)
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')


            user = authenticate(username=username, password=raw_password)
            if username.startswith('tech@'):
                # Créer un nouvel utilisateur

                # Créer un technicien associé à l'utilisateur
                technicien = Technicien.objects.create(
                    user=user,
                    nom=username,

                )
            login(request, user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('index')
    else:
        print('erreur')
        form = SignUpForm()
    context = {'form':form}
    return render(request, 'Dashboard/register.html',context)



@receiver(post_save, sender=Intervention)
def client_post_save(sender, instance, created , *args, **kwargs):
    if created:
        client = Client.objects.create(Nom_Client=instance.Nom_Client,Numéro=instance.Numéro,Ville=instance.Ville,Address=instance.Address,Code_postal=instance.Code_postal)



def Planning(request):
    ints = Intervention.objects.all()
    context={'ints': ints}
    return render(request,'Dashboard/planning.html',context)





from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import generic
from django.utils.safestring import mark_safe

from .models import *
from .utils import Calendar

class CalendarView(generic.ListView):
    model = Intervention
    template_name = 'Dashboard/planning.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month




def Edit_intervention(request,inter_id):
    intervention = Intervention.objects.get(pk=inter_id)
    if request.method == 'POST':
        form = InterventionForm(request.POST, instance=intervention)
        if form.is_valid():
            intervention = form.save(commit=False)
            intervention.status = request.POST.get('status')
            form.save()
            return redirect('list_interventions_enattente')
    else:
        form = InterventionForm(instance=intervention)

    techs = UserProfile.objects.all()
    context ={'int':intervention, 'form':form  , 'techs': techs}
    return render(request,'Dashboard/Edit_intervention.html' ,context)

from .forms import ReclamationForm
def Add_reclamation(request):
    if request.method == 'POST':
        form = ReclamationForm(request.POST)
        if form.is_valid():
            nouvelle_reclamation = form.save(commit=False)
            # Assurez-vous d'associer la réclamation au client connecté (utilisateur)
            nouvelle_reclamation.client = request.user.username  # Supposons que vous avez une relation client-utilisateur
            nouvelle_reclamation.save()
            messages.success(request, 'Votre réclamation a été soumise avec succès!')
            # Ajoutez ici la logique de notification à l'administrateur, si nécessaire
            return redirect('index')
    else:
        form = ReclamationForm()
    context = {'form':form}
    return render(request,'Dashboard/Ajouter_reclamation.html',context )
