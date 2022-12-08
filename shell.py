from filial1 .models import *


# client1 = Client(email= 'nikname21@gmail.com', password ='defender42', name = 'Азат Соколов', card_number = '4147565798789009')

# worker1 = Worker(email = 'altywa1998@gmail.com', password= 'nono34',name = 'Алтынай Алиева', position = 'Оператор кассы')
# client1.save()
# worker1.save()

# ingridients_chees = Ingridient.objects.create(name='chees',extra_price=10)
# ingridients_chicken = Ingridient.objects.create(name='chicken',extra_price=70)
# ingridients_beef = Ingridient.objects.create(name='beef',extra_price=80)
# ingridients_salad = Ingridient.objects.create(name='salad',extra_price=15)
# ingridients_free = Ingridient.objects.create(name='free',extra_price=15)

# food_shaurma = Food.objects.create(name='shaurma',start_price=50)
# food_gamburger = Food.objects.create(name='gamburger',start_price=25)


# food_shaurma.orders.set([ingridients_beef, ingridients_chees, ingridients_salad,ingridients_free], through_defaults={'client':client1, 'worker':worker1})
# shaurma_price = food_shaurma.start_price + ingridients_beef.extra_price + ingridients_chees.extra_price + ingridients_salad.extra_price + ingridients_free.extra_price
# print(shaurma_price)

# food_gamburger.orders.set([ingridients_chicken, ingridients_salad], through_defaults={'client':client1, 'worker':worker1})
# gamburger_price = food_gamburger.start_price + ingridients_chicken.extra_price + ingridients_salad.extra_price
# print(gamburger_price)



client1 = Client.objects.create(name= 'Нурсултан Бердиев', card_number= '4147565798789009',email = 'nikname21@gmail.com', password='defender42')

worker1 = Worker.objects.create(email = 'altywa1998@gmail.com', password= 'nono34',name = 'Алтынай Алиева', position = 'Оператор кассы')


food_shaurma = Food.objects.create(name='shaurma',start_price=200,type_of_cuisine='фастфуд',calories=500)
food_gamburger = Food.objects.create(name='gamburger',start_price=180,type_of_cuisine='фастфуд',calories=350)
food_pasta = Food.objects.create(name='pasta',start_price=450,type_of_cuisine='Итальянская',calories=400)
food_boul = Food.objects.create(name='boul',start_price=600,type_of_cuisine='европейское',calories=500)
food_sushi = Food.objects.create(name='sushi',start_price=400,type_of_cuisine='японская',calories=450)

ingridients_chees = Ingridient.objects.create(name='chees',extra_price=80,calories=150)
ingridients_chicken = Ingridient.objects.create(name='chicken',extra_price=100, calories=250)
ingridients_beef = Ingridient.objects.create(name='beef',extra_price=120,calories=300)
ingridients_salad = Ingridient.objects.create(name='salad',extra_price=50,calories=50)
ingridients_free = Ingridient.objects.create(name='free',extra_price=50,calories=70)
ingridients_fish = Ingridient.objects.create(name='fish',extra_price=120,calories=270)
ingridients_rice = Ingridient.objects.create(name='rice',extra_price=70,calories=100)
ingridients_tvorog = Ingridient.objects.create(name='tvorog',extra_price=100,calories=170)
ingridients_egg = Ingridient.objects.create(name='eeg',extra_price=50,calories=120)

result_shaurma = food_shaurma.orders.set([ingridients_beef, ingridients_chees, ingridients_salad,ingridients_free], through_defaults={'client':client1, 'worker':worker1})

result_gamburger = food_gamburger.orders.set([ingridients_chicken, ingridients_salad], through_defaults={'client':client1, 'worker':worker1})
result_pasta = food_pasta.orders.set([ingridients_salad,ingridients_egg,ingridients_chees,ingridients_tvorog],through_defaults={'client':client1, 'worker':worker1})
result_sushi = food_sushi.orders.set([ingridients_rice,ingridients_fish,ingridients_egg],through_defaults={'client':client1, 'worker':worker1})
result_boul = food_boul.orders.set([ingridients_rice,ingridients_chees,ingridients_free,ingridients_salad,ingridients_tvorog],through_defaults={'client':client1, 'worker':worker1})

for fp in Resultat.objects.all():
    fp.save()








