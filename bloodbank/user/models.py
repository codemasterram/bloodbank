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
	
