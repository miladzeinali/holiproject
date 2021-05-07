from django.db import models
from ..models.origin import Product
from .origin import *


class TV(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand')
    image = models.ImageField(null=True, blank=True, upload_to='product-img/')
    image1 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    image2 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    title = models.CharField(max_length=50)
    price = models.FloatField(default=0)
    off_percent = models.IntegerField(default=0, null=True, blank=True)
    club_point = models.IntegerField(default=0, null=True, blank=True)
    count = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True, blank=True)
    guarantee = models.ForeignKey(Guarantee, on_delete=models.CASCADE)
    hashtag = models.TextField(max_length=60, null=True, blank=True)
    point = models.PositiveSmallIntegerField(default=0)
    code=models.CharField(max_length=15)
    country_made = models.CharField(max_length=25)
    year_made = models.CharField(max_length=8)
    screen_dimension_choice = (
        (32, 32),
        (40, 40),
        (42, 42),
        (43, 43),
        (49, 49),
        (50, 50),
        (55, 55),
        (60, 60),
        (75, 75),
        (85, 85),
    )
    screen_dimension = models.CharField(choices=screen_dimension_choice, default=43, max_length=10)
    panel_type = models.CharField(max_length=15)
    type_screen_choice = (
        ('curve', 'curve'),
        ('flat', 'flat')
    )
    type_screen = models.CharField(choices=type_screen_choice, default='flat', max_length=10)
    resulotion_choice = (
        ('led', 'led'),
        ('lcd', 'lcd'),
        ('4k', '4k'),
        ('8k', '8k'),
        ('qhd', 'qhd'),
    )
    resulotion = models.CharField(choices=resulotion_choice, default='4k', max_length=15)
    sound_desc = models.TextField(max_length=150)
    software_desc = models.TextField(max_length=150)
    contact_gates = models.TextField(max_length=200)
    hardware = models.TextField(max_length=200)
    CountSell = models.PositiveSmallIntegerField(default=0)
    owner = models.ForeignKey(Sellers, on_delete=models.CASCADE)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE, auto_created=True)
    Sale=models.BooleanField(default=False)
    def save(self):
        created = not self.pk
        super().save()
        if created:
            Product.objects.create(title=self.title,
                                   brand=self.brand,category=self.category,
                                   code=self.code,Sale=self.Sale,color=self.color,count=self.count,image=self.image,
                                   price=self.price,off_percent=self.off_percent,club_point=self.club_point,guarantee=self.guarantee,
                                   hashtag=self.hashtag,point=self.point,owner=self.owner)



class CarPlayer(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='product-img/')
    image1 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    image2 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    title = models.CharField(max_length=50)
    price = models.FloatField(default=0)
    off_percent = models.IntegerField(default=0, null=True, blank=True)
    club_point = models.IntegerField(default=0, null=True, blank=True)
    count = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True, blank=True)
    guarantee = models.ForeignKey(Guarantee, on_delete=models.CASCADE)
    hashtag = models.TextField(max_length=60, null=True, blank=True)
    point = models.PositiveSmallIntegerField(default=0)
    code=models.CharField(max_length=15)
    dexless = models.BooleanField()
    cd_player = models.BooleanField(default=True)
    flash_player = models.BooleanField(default=True)
    aux_player = models.BooleanField(default=True)
    bt_player = models.BooleanField(default=False)
    lcd_type = models.CharField(max_length=35)
    backlight = models.BooleanField(default=True)
    typesong_play = models.CharField(max_length=40)
    optimize_sound = models.BooleanField(default=True)
    mosfet = models.CharField(max_length=50)
    supertuner = models.BooleanField()
    subtuner = models.BooleanField()
    eq_count = models.CharField(max_length=50)
    app_support = models.BooleanField()
    spreate_panel = models.BooleanField()
    round_sound = models.BooleanField()
    remote = models.BooleanField()
    usb_control_remote = models.BooleanField()
    RC_count = models.PositiveSmallIntegerField()
    mixable_songs = models.BooleanField()
    summary_desc = models.TextField(max_length=250)
    CountSell = models.PositiveSmallIntegerField(default=0)
    owner = models.ForeignKey(Sellers, on_delete=models.CASCADE)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE, auto_created=True)
    Sale=models.BooleanField(default=False)
    def save(self):
        created = not self.pk
        super().save()
        if created:
            Product.objects.create(title=self.title,
                                   brand=self.brand,category=self.category,
                                   code=self.code,Sale=self.Sale,color=self.color,count=self.count,image=self.image,
                                   price=self.price,off_percent=self.off_percent,club_point=self.club_point,guarantee=self.guarantee,
                                   hashtag=self.hashtag,point=self.point,owner=self.owner)



class Amplifire(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='product-img/')
    image1 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    image2 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    title = models.CharField(max_length=50)
    price = models.FloatField(default=0)
    off_percent = models.IntegerField(default=0, null=True, blank=True)
    club_point = models.IntegerField(default=0, null=True, blank=True)
    count = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True, blank=True)
    guarantee = models.ForeignKey(Guarantee, on_delete=models.CASCADE)
    hashtag = models.TextField(max_length=60, null=True, blank=True)
    point = models.PositiveSmallIntegerField(default=0)
    code=models.CharField(max_length=15)
    channel_choice = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
    )
    PeakPower = models.CharField(max_length=45)
    Rms4Ohm = models.CharField(max_length=50)
    Rms2Ohm = models.CharField(max_length=50)
    Bridghable = models.BooleanField()
    sub_eq = models.BooleanField()
    signaltoNoise = models.CharField(max_length=50)
    NoiseReact = models.CharField(max_length=50)
    Lpf = models.BooleanField()
    Hpf = models.BooleanField()
    Fuse = models.CharField(max_length=50)
    summary_desc = models.TextField(max_length=250)
    CountSell = models.PositiveSmallIntegerField(default=0)
    owner = models.ForeignKey(Sellers, on_delete=models.CASCADE)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE, auto_created=True)
    Sale=models.BooleanField(default=False)
    def save(self):
        created = not self.pk
        super().save()
        if created:
            Product.objects.create(title=self.title,
                                   brand=self.brand,category=self.category,
                                   code=self.code,Sale=self.Sale,color=self.color,count=self.count,image=self.image,
                                   price=self.price,off_percent=self.off_percent,club_point=self.club_point,guarantee=self.guarantee,
                                   hashtag=self.hashtag,point=self.point,owner=self.owner)



class Speaker(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='product-img/')
    image1 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    image2 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    title = models.CharField(max_length=50)
    price = models.FloatField(default=0)
    off_percent = models.IntegerField(default=0, null=True, blank=True)
    club_point = models.IntegerField(default=0, null=True, blank=True)
    count = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True, blank=True)
    guarantee = models.ForeignKey(Guarantee, on_delete=models.CASCADE)
    hashtag = models.TextField(max_length=60, null=True, blank=True)
    point = models.PositiveSmallIntegerField(default=0)
    code=models.CharField(max_length=15)
    PeakPower = models.CharField(max_length=20)
    Rms = models.CharField(max_length=20)
    CountSell = models.PositiveSmallIntegerField(default=0)
    owner = models.ForeignKey(Sellers, on_delete=models.CASCADE)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE,  auto_created=True)
    Sale=models.BooleanField(default=False)
    def save(self):
        created = not self.pk
        super().save()
        if created:
            Product.objects.create(title=self.title,
                                   brand=self.brand,category=self.category,
                                   code=self.code,Sale=self.Sale,color=self.color,count=self.count,image=self.image,
                                   price=self.price,off_percent=self.off_percent,club_point=self.club_point,guarantee=self.guarantee,
                                   hashtag=self.hashtag,point=self.point,owner=self.owner)



