from django.db import models
from django.utils import timezone


# YEAR_IN_SCHOOL_CHOICES = (
#         (FRESHMAN, 'Freshman'),
#         (SOPHOMORE, 'Sophomore'),
#         (JUNIOR, 'Junior'),
#         (SENIOR, 'Senior'),
#     )
#     year_in_school = models.CharField(
#         max_length=2,
#         choices=YEAR_IN_SCHOOL_CHOICES,
#         default=FRESHMAN,
#     )



class Bloodbank(models.Model):
    Institution_name = models.CharField(max_length=100)
    District = models.CharField(max_length=50)
    GOVERNMENT='GOVE'
    PRIVATE='NGOV'
    INSTITUTION_TYPE = (
        (GOVERNMENT, 'GOVERNMENT'),
        (PRIVATE, 'PRIVATE'),
    )
    institution_name = models.CharField(
        max_length=4,
        choices=INSTITUTION_TYPE,
        default=GOVERNMENT,
    )
    Landline = models.IntegerField()
    Email = models.CharField(max_length=50)
    A_positive = models.IntegerField()
    A_negative = models.IntegerField()
    B_positive = models.IntegerField()
    B_negative = models.IntegerField()
    AB_positive = models.IntegerField()
    AB_negative = models.IntegerField()
    O_positive = models.IntegerField()
    O_negative =  models.IntegerField()
    UpDated_On = models.DateTimeField(default=timezone.now)


class Donors(models.Model):
    FirstName = models.CharField(max_length=60)
    LastName = models.CharField(max_length=60)
    Address = models.CharField(max_length=60)



    MALE='MALE'
    FEMALE='FEMALE'
    OTHERS='OTHERS'
    GENDER = (
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
        (OTHERS, 'OTHERS'),
    )
    GENDER = models.CharField(
        max_length=6,
        choices=GENDER,
        default=MALE,
    )


    A_positive='A_positive'
    A_negative='A_negative'
    B_positive='B_positive'
    B_negative='B_negative'
    AB_positive='AB_positive'
    AB_negative='AB_negative'
    O_positive='O_positive'
    O_negative='O_negative'
    BLOODGROUP = (
        (A_positive,'A_positive'),
        (A_negative,'A_negative'),
        (B_positive,'B_positive'),
        (B_negative,'B_negative'),
        (AB_positive,'AB_positive'),
        (AB_negative,'AB_negative'),
        (O_positive,'O_positive'),
        (O_negative,'O_negative'),
        )
    BLOODGROUP = models.CharField(
        max_length=12,
        choices=BLOODGROUP

        )
    ContactNumber = models.IntegerField()
    Email = models.CharField(max_length=50,blank=True)
    lastDonated = models.DateTimeField()





	
