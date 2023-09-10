from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'author_name': 'Samuel Taniel Mulyadi',
        'author_class': 'PBP D',
        'name_card1': 'Mewtwo', 'name_card2': 'Starmie', 'name_card3': 'Eevee', 'name_card4': 'Suicune', 'name_card5': 'Sceptile', 'name_card6': 'Haunter', 'name_card7': 'Samurott', 'name_card8': 'Mimikyu',
        'category1': 'Psychic', 'category2': 'Water', 'category3': 'Normal', 'category4': 'Water', 'category5': 'Grass', 'category6': 'Dark', 'category7': 'Water', 'category8': 'Dark', 
        'price1': 100000, 'price2': 5, 'price3': 2, 'price4': 100, 'price5': 10, 'price6': 10, 'price7': 50, 'price8': 5,
        'amount1': 1, 'amount2': 100000, 'amount3': 100000, 'amount4': 10000, 'amount5': 100000, 'amount6': 100000, 'amount7': 50000, 'amount8': 100000,
        'description1': "Mewtwo, the result of an experiment on Mew Pokemon by humans. It wants revenge on humanity, therefore there's only one of it in the world.",
        'description2': "Starmie is a celestial and enigmatic Pokémon with a striking appearance.",
        'description3': "Eevee is a small, fox-like Pokémon known for its unique ability to evolve into various different forms, depending on certain conditions.",
        'description4': "Suicune is a majestic Pokémon with a slender, blue body and a flowing, aurora-like mane that ripples as it moves.",
        'description5': "With its incredible speed and impressive moves like Leaf Blade, Sceptile can swiftly slice through its opponents.",
        'description6': "With its gas-like body, it can float through walls and appear and disappear at will.",
        'description7': "It boasts a regal and warrior-like demeanor, often wielding a pair of sharp scalchops, which it uses both as weapons and tools.",
        'description8': "It is known for its desire to be loved and accepted by humans and other Pokémon, which has led it to disguise itself.",
    }

    return render(request, "main.html", context)
