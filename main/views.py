from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from main import forms
from django.urls import reverse
from main.models import Product

# Create your views here.
def show_main(request):
    products = Product.objects.all()

    context = {
        'author_info': {
            'name': 'Samuel Taniel Mulyadi',
            'class': 'PBP D',
        },
        'app_name': 'Pokemon Shop',
        'cards': [
            {
                'picture': "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c3dfdb24-369a-4251-9313-3bb185ea2453/dbowzl8-dbbc4631-6489-4bbb-ab7b-80a870341a9b.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2MzZGZkYjI0LTM2OWEtNDI1MS05MzEzLTNiYjE4NWVhMjQ1M1wvZGJvd3psOC1kYmJjNDYzMS02NDg5LTRiYmItYWI3Yi04MGE4NzAzNDFhOWIuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.9Xv2avCprYz5Hcru0i6m5NdJmiMYGjo123ea46m34GU",
                'name': 'MewTwo',
                'category': 'Psychic',
                'price': 100000,
                'amount': 1,
                'description': "Mewtwo, the result of an experiment on Mew Pokemon by humans. It wants revenge on humanity, therefore there's only one of it in the world.",
            },
            {
                'picture': "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c3dfdb24-369a-4251-9313-3bb185ea2453/dc10e3r-61463653-472e-414d-8f09-151649249bc9.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2MzZGZkYjI0LTM2OWEtNDI1MS05MzEzLTNiYjE4NWVhMjQ1M1wvZGMxMGUzci02MTQ2MzY1My00NzJlLTQxNGQtOGYwOS0xNTE2NDkyNDliYzkuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.Hq72SiZGNltB5sfqtX9gHUxHiOfWNGLDGRnvRBGvv0Y",
                'name': 'Starmie',
                'category': 'Water',
                'price': 5,
                'amount': 100000,
                'description': "Starmie is a celestial and enigmatic Pokémon with a striking appearance.",
            },
            {
                'picture': "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c3dfdb24-369a-4251-9313-3bb185ea2453/dbroj7n-3c5feb65-fd05-4956-aa6d-3c3f48e5bb75.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2MzZGZkYjI0LTM2OWEtNDI1MS05MzEzLTNiYjE4NWVhMjQ1M1wvZGJyb2o3bi0zYzVmZWI2NS1mZDA1LTQ5NTYtYWE2ZC0zYzNmNDhlNWJiNzUuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.YNYEcGpslvx9kslnjmWIjBPEvwphNRrN0V_Q8tjtv7k",
                'name': 'Eevee',
                'category': 'Normal',
                'price': 2,
                'amount': 100000,
                'description': "Eevee is a small, fox-like Pokémon known for its unique ability to evolve into various different forms, depending on certain conditions.",
            },
            {
                'picture': "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c3dfdb24-369a-4251-9313-3bb185ea2453/dboqe8v-057ffe77-3bde-4d03-928e-42cfa74d445a.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2MzZGZkYjI0LTM2OWEtNDI1MS05MzEzLTNiYjE4NWVhMjQ1M1wvZGJvcWU4di0wNTdmZmU3Ny0zYmRlLTRkMDMtOTI4ZS00MmNmYTc0ZDQ0NWEuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.whlylyHeITaqYVSNkICmjde3rShB2QgYADnxATsOBOM",
                'name': 'Suicune',
                'category': 'Water',
                'price': 100,
                'amount': 10000,
                'description': "Suicune is a majestic Pokémon with a slender, blue body and a flowing, aurora-like mane that ripples as it moves.",
            },
            {
                'picture': "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c3dfdb24-369a-4251-9313-3bb185ea2453/dbnj4sz-53864d26-9787-40d1-a0f3-47e222727a20.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2MzZGZkYjI0LTM2OWEtNDI1MS05MzEzLTNiYjE4NWVhMjQ1M1wvZGJuajRzei01Mzg2NGQyNi05Nzg3LTQwZDEtYTBmMy00N2UyMjI3MjdhMjAuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.dxGdJd13QQ5i7YIk4MTLUewSMNYMA6xd7-DWPD4Vctk",
                'name': 'Sceptile',
                'category': 'Grass',
                'price': 10,
                'amount': 100000,
                'description': "With its incredible speed and impressive moves like Leaf Blade, Sceptile can swiftly slice through its opponents.",
            },
            {
                'picture': "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c3dfdb24-369a-4251-9313-3bb185ea2453/dbirhpt-ba192d17-592f-4dd7-9ff4-ce40f506dbfe.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2MzZGZkYjI0LTM2OWEtNDI1MS05MzEzLTNiYjE4NWVhMjQ1M1wvZGJpcmhwdC1iYTE5MmQxNy01OTJmLTRkZDctOWZmNC1jZTQwZjUwNmRiZmUuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.Q0xeLFQ1EzDUDzL61mskPEG-OXxs3RfdO-v7sbutuMY",
                'name': 'Haunter',
                'category': 'Dark',
                'price': 10,
                'amount': 100000,
                'description': "With its gas-like body, it can float through walls and appear and disappear at will.",
            },
            {
                'picture': "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c3dfdb24-369a-4251-9313-3bb185ea2453/dbksp56-84f8a7ad-e544-47b4-84c8-3baae7451172.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2MzZGZkYjI0LTM2OWEtNDI1MS05MzEzLTNiYjE4NWVhMjQ1M1wvZGJrc3A1Ni04NGY4YTdhZC1lNTQ0LTQ3YjQtODRjOC0zYmFhZTc0NTExNzIuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.Y5GGenyjsVYA4Mr6V5E1k5soRElnlueYpDazcfOg3Bo",
                'name': 'Samurott',
                'category': 'Water',
                'price': 50,
                'amount': 50000,
                'description': "It boasts a regal and warrior-like demeanor, often wielding a pair of sharp scalchops, which it uses both as weapons and tools.",
            },
            {
                'picture': "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c3dfdb24-369a-4251-9313-3bb185ea2453/dbgiozh-e376c8f4-fdf2-4da8-93f5-a472449dea11.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2MzZGZkYjI0LTM2OWEtNDI1MS05MzEzLTNiYjE4NWVhMjQ1M1wvZGJnaW96aC1lMzc2YzhmNC1mZGYyLTRkYTgtOTNmNS1hNDcyNDQ5ZGVhMTEuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.6Maxac2QL51QssKPIx-OwVVq_NiLjf4vR05KOea18Pw",
                'name': 'Mimikyu',
                'category': 'Dark',
                'price': 5,
                'amount': 100000,
                'description': "It is known for its desire to be loved and accepted by humans and other Pokémon, which has led it to disguise itself.",
            },
        ],
        'products': products
    }

    for product in products:
        total_price = 0
        picture = ""
        for card in context['cards']:
            if card['name'] == product.name:
                total_price = float(card['price']) * int(product.amount)
                picture = card['picture']
                break
            
        product.picture = picture
        product.price = total_price

    return render(request, "main.html", context)

def create_product(request):
    form = forms.ProductForm(request.POST or None)
    
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def delete(request): #delete isi form
    Product.objects.all().delete()
    return HttpResponse("yoi delete")

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
