from django.db import models
from django.contrib.auth.models import User


class State(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'state'


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta:
        db_table = 'city'


class District(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

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

    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    # image = models.ImageField(upload_to='/static', null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=False)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=False)
    address = models.TextField(null=True, blank=True)
    area = models.IntegerField(null=False, blank=False)
    construction_year = models.DateField(null=False, blank=False)
    price = models.PositiveBigIntegerField(null=False, blank=False)
    floor = models.PositiveSmallIntegerField(choices=[('Basement', 0), ('Ground Floor', 1), (2, 2), (3, 3), (4, 4),
                                                      (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11),
                                                      (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17),
                                                      (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23),
                                                      (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29),
                                                      (30, 30), ('Higher', 31)], null=False, blank=False)
    rooms = models.PositiveSmallIntegerField(choices=RoomsNumber.choices, null=True, blank=True)
    warehouse = models.BooleanField(null=True, blank=True)
    parking = models.BooleanField(null=True, blank=True)
    elevator = models.BooleanField(null=True, blank=True)
    sold = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "estate"
