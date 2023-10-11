from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,  redirect
from django.urls import reverse

from listings.models import Band, Listing
from listings.forms import BandForm, ListingForm, ContactUsForm

# Create your views here.


def band_list(request):
    bands = Band.objects.all()
    return render(request, 
                    'listings/band_list.html', 
                    context = {"bands" : bands})



def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request, 
                    'listings/band_detail.html', 
                    context = {"band" : band})


def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
             # Création d'un nouveau 'Band' (groupe) et sauvegarde dans la base de données
            band = form.save()
             # Redirection vers la page de détail correspondant au groupe que nous venons de créer
            return HttpResponseRedirect(reverse('band-detail', kwargs={'id': band.id}))
    else:
        form = BandForm()

    return render(request, 'listings/band_create.html', context = {"form" : form})


def band_update(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # Mise à jour du groupe existant dans la base de données
            form.save()
            return HttpResponseRedirect(reverse('band-detail', kwargs={'id': band.id}))
            #return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)

    return render(request, 'listings/band_update.html', context = {"form" : form})
    

def band_delete(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
         # Suppression du groupe dans la base de données
        band.delete()
        # Redirection vers la liste des groupes
        return HttpResponseRedirect(reverse('band-list'))
        #return redirect('band_list')

    return render(request, 'listings/band_delete.html', context = {"band" : band})



def listing_list(request):
    listings = Listing.objects.all()
    return render(request,
                  'listings/listing_list.html',
                  {'listings': listings})


def listing_detail(request, id):
    listing = Listing.objects.get(id=id)
    return render(request,
                  'listings/listing_detail.html',
                  {'listing': listing})



def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/listings/')
    else:
        form = ListingForm()

    return render(request,
                  'listings/listing_create.html',
                  {'form': form})


def listing_update(request, id):
    listing = Listing.objects.get(id=id)

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect(f'/listings/{id}/')
            return redirect('listing-detail', listing.id)
    else:
        form = ListingForm(instance=listing)

    return render(request,
                  'listings/listing_update.html',
                  {'form': form})


def listing_delete(request, id):
    listing = Listing.objects.get(id=id)

    if request.method == 'POST':
        listing.delete()
        return HttpResponseRedirect(reverse('listing-list'))

    return render(request,
                  'listings/listing_delete.html',
                  {'listing': listing})


# def contact(request):
#     return HttpResponse('<h1>Contact</h1> <p>Nous adorons merch !</p>')

def about(request):
    return render(request, 'listings/about.html')
    #return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')



def contact(request):
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["nom"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
            )
        return redirect('/email-sent/') 
    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).

    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()

    return render(request,
            'listings/contact.html',
            {'form': form})



def email_sent(request):
    return render(request, 'listings/email_sent.html')


def listings(request):
    return HttpResponse('<h1>Listings</h1>')

