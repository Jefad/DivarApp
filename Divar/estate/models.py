from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class State(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'state'


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'city'


class District(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'district'


class Estate(models.Model):
    class RoomsNumber(models.IntegerChoices):
        No_Room = 0
        One = 1
        Two = 2
        Three = 3
        Four = 4
        Five = 5
        More = 6

    year_choices = [(year, year) for year in range(1350, 1402)]
    floor_choices = [(floor, floor) for floor in range(2, 30)]

    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    # image = models.ImageField(upload_to='/static', null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=False)
    address = models.TextField(null=True, blank=True)
    area = models.PositiveIntegerField(null=False, blank=False)
    construction_year = models.PositiveSmallIntegerField(null=False, blank=False, validators=[MinValueValidator(1350),
                                                                                              MaxValueValidator(1402)])
    price = models.PositiveBigIntegerField(null=False, blank=False, validators=[MinValueValidator(2e5),
                                                                                MaxValueValidator(1e12)])
    floor = models.PositiveSmallIntegerField(choices=[(0, 'Basement'), (1, 'Ground Floor')] + floor_choices +
                                                     [(31, 'Higher')], null=False, blank=False)
    rooms = models.PositiveSmallIntegerField(choices=RoomsNumber.choices, null=True, blank=True)
    warehouse = models.BooleanField(null=True, blank=True)
    parking = models.BooleanField(null=True, blank=True)
    elevator = models.BooleanField(null=True, blank=True)
    sold = models.BooleanField(null=True, blank=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "estate"
