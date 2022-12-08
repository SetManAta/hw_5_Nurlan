from django.db import models

class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.email
    class Meta:
        abstract = True
    

class Client(User):
    name = models.CharField(max_length=20)
    card_number = models.IntegerField()

    def __str__(self):
        return self.name
    

    class Meta(User.Meta):
        pass

class Worker(User):
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta(User.Meta):
        pass

class Ingridient(models.Model):
    name = models.CharField(max_length=20)
    extra_price = models.IntegerField()
    calories = models.IntegerField()

    def __str__(self):
        return self.name
    

class Food(models.Model):
    name = models.CharField(max_length=20)
    start_price = models.IntegerField()
    orders = models.ManyToManyField(Ingridient, related_name='food', through='Order')
    type_of_cuisine = models.CharField(max_length=20)
    calories = models.IntegerField()

    def __str__(self):
        return self.name
    


meat = {'chicken', 'beef', 'fish' }    

class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    ingridient = models.ForeignKey(Ingridient,on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker,on_delete=models.CASCADE)
    vegetarian = models.BooleanField(default=True,null=True)
    food_status = models.CharField(max_length=20,null=True)
    final_price = models.IntegerField(null=True)
    order_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.food.name} - {self.ingridient.name} - {self.client.name} - {self.worker.name}'



class Resultat(Order):
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if self.ingridient.name in ['chicken', 'beef', 'fish']:
            self.vegetarian = False
        else:
            self.vegetarian = True
        # if any([x in self.ingridient for x in meat]):
        #     self.vegetarian = False

        resultat_cal = self.food.calories + self.ingridient.calories

        if resultat_cal <= 700:
            self.food_status = 'Перекус'
        elif resultat_cal <= 1200:
            self.food_status = 'Обед'
        elif resultat_cal > 1200:
            self.food_status = 'обжиралова'

        self.final_price = self.food.start_price + self.ingridient.extra_price
        # if self.final_price > 1000:
        #     self.final_price = 'болше 1000'
        # elif self.final_price < 1000:
        #     self.final_price = 'меньше 1000'
        super().save(*args, **kwargs)  


    