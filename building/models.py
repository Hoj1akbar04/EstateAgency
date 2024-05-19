
from django.db import models
from users.models import Address, Agents
from users.helpers import SaveMediaFile, Choices


class Build(models.Model):
    name = models.CharField(max_length=30)
    agents = models.ForeignKey(Agents, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to=SaveMediaFile.home_image)
    price = models.FloatField()
    saw = models.PositiveBigIntegerField(default=0)
    price_type = models.CharField(max_length=8, choices=Choices.PriceType.choices, default=Choices.PriceType.s)
    area = models.FloatField()
    beds = models.IntegerField()
    baths = models.IntegerField()
    garages = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.price} {self.area} {self.beds} {self.baths} {self.garages} {self.address}"