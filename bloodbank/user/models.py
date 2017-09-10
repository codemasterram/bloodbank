from django.db import models
from django.utils import timezone


DISTRICT=(
    ('Bhaktapur','Bhaktapur'),
    ('Dhading','Dhading'),
    ('Kathmandu','Kathmandu'),
    ('Kavrepalanchok','Kavrepalanchok'),
    ('Lalitpur','Lalitpur'),
    ('Nuwakot','Nuwakot'),
    ('Rasuwa','Rasuwa'),
    ('Sindhupalchok','Sindhupalchok'),
    ('Banke','Banke'),
    ('Bardiya','Bardiya'),
    ('Dailekh','Dailekh'),
    ('Jajarkot','Jajarkot'),
    ('Surkhet','Surkhet'),
    ('Baglung','Baglung'),
    ('Mustang','Mustang'),
    ('Myagdi','Myagdi'),
    ('Parbat','Parbat'),
    ('Gorkha','Gorkha'),
    ('Kaski','Kaski'),
    ('Lamjung','Lamjung'),
    ('Manang','Manang'),
    ('Syangja','Syangja'),
    ('Tanahu','Tanahu'),
    ('Dhanusa','Dhanusa'),
    ('Dolakha','Dolakha'),
    ('Mahottari','Mahottari'),
    ('Ramechhap','Ramechhap'),
    ('Sarlahi','Sarlahi'),
    ('Sindhuli','Sindhuli'),
    ('Dolpa','Dolpa'),
    ('Humla','Humla'),
    ('Jumla','Jumla'),
    ('Kalikot','Kalikot'),
    ('Mugu','Mugu'),
    ('Bhojpur','Bhojpur'),
    ('Dhankuta','Dhankuta'),
    ('Morang','Morang'),
    ('Sankhuwasabha','Sankhuwasabha'),
    ('Sunsari','Sunsari'),
    ('Terhathum','Terhathum'),
    ('Arghakhanchi','Arghakhanchi'),
    ('Gulmi','Gulmi'),
    ('Kapilvastu','Kapilvastu'),
    ('Nawalparasi','Nawalparasi'),
    ('Palpa','Palpa'),
    ('Rupandehi','Rupandehi'),
    ('Baitadi','Baitadi'),
    ('Dadeldhura','Dadeldhura'),
    ('Darchula','Darchula'),
    ('Kanchanpur','Kanchanpur'),
    ('Ilam','Ilam'),
    ('Jhapa','Jhapa'),
    ('Panchthar','Panchthar'),
    ('Taplejung','Taplejung'),
    ('Bara','Bara'),
    ('Chitwan','Chitwan'),
    ('Makwanpur','Makwanpur'),
    ('Parsa','Parsa'),
    ('Rautahat','Rautahat'),
    ('Dang','Dang'),
    ('Pyuthan','Pyuthan'),
    ('Rolpa','Rolpa'),
    ('Rukum','Rukum'),
    ('Salyan','Salyan'),
    ('Khotang','Khotang'),
    ('Okhaldhunga','Okhaldhunga'),
    ('Saptari','Saptari'),
    ('Siraha','Siraha'),
    ('Solukhumbu','Solukhumbu'),
    ('Udayapur','Udayapur'),
    ('Achham','Achham'),
    ('Bajhang','Bajhang'),
    ('Bajura','Bajura'),
    ('Doti','Doti'),
    ('Kailali','Kailali'),
)


class Bloodbank(models.Model):
    Institution_name = models.CharField(max_length=100)
    DISTRICT = models.CharField(
        max_length=25,
        choices=DISTRICT

    )
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
    Address = models.CharField(max_length=60)
    ContactNumber = models.CharField(max_length=15, help_text = '+977-9843010101 or 01-5204000')
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


GENDER = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE'),
    ('OTHERS', 'OTHERS'),
)



BLOODGROUP = (
    ('A_positive','A positive'),
    ('A_negative','A negative'),
    ('B_positive','B positive'),
    ('B_negative','B negative'),
    ('AB_positive','AB positive'),
    ('AB_negative','AB negative'),
    ('O_positive','O positive'),
    ('O_negative','O negative'),
)


class Donors(models.Model):
    FirstName = models.CharField(max_length=60)
    LastName = models.CharField(max_length=60)
    district = models.CharField(
        max_length=25,
        choices=DISTRICT

        )
    Address = models.CharField(max_length=60)




    
    GENDER = models.CharField(
        max_length=6,
        choices=GENDER,
        default='MALE',
    )



    BLOODGROUP = models.CharField(
        max_length=12,
        choices=BLOODGROUP

        )
    ContactNumber = models.CharField(max_length=15, help_text = '+977-9843010101')
    Email = models.CharField(max_length=50,blank=True)
    lastDonated = models.DateField()










	
