from django.db import models
from Products.models.origin import Product
from .origin import *


# digikala
class Mobile(models.Model):
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
    dimensions = models.CharField(max_length=30, null=True, blank=True)
    sim_card = models.CharField(max_length=30, null=True, blank=True)
    weight = models.CharField(max_length=10, null=True, blank=True)
    special_prop = models.CharField(max_length=100, null=True, blank=True)
    sim_count = models.CharField(max_length=20, null=True, blank=True)
    publish_date = models.CharField(max_length=20, null=True, blank=True)
    slot = models.BooleanField(default=False)
    model = models.CharField(max_length=35, null=True, blank=True)
    chipest = models.CharField(max_length=20, null=True, blank=True)
    cpu = models.CharField(max_length=20, null=True, blank=True)
    cpu_type = models.CharField(max_length=20, null=True, blank=True)
    frequencies = models.CharField(max_length=20, null=True, blank=True)
    gpu = models.CharField(max_length=20, null=True, blank=True)
    internal_memory = models.CharField(max_length=20, null=True, blank=True)
    ram = models.CharField(max_length=20, null=True, blank=True)
    microSd = models.BooleanField(default=False)
    touchScreen = models.BooleanField(default=False)
    screen_technology = models.CharField(max_length=15, null=True, blank=True)
    screen_limit = models.CharField(max_length=15, null=True, blank=True)
    screen_dimension = models.CharField(max_length=15, null=True, blank=True)
    screen_resolution = models.CharField(max_length=15, null=True, blank=True)
    screen_pixel = models.CharField(max_length=25, null=True, blank=True)
    screen_ratio = models.CharField(max_length=20, null=True, blank=True)
    net = models.CharField(max_length=25, null=True, blank=True)
    bluetooth = models.CharField(max_length=20, null=True, blank=True)
    bluetooth_version = models.CharField(max_length=20, null=True, blank=True)
    location_tech = models.CharField(max_length=20, null=True, blank=True)
    contact_gate = models.CharField(max_length=20, null=True, blank=True)
    camera = models.CharField(max_length=20, null=True, blank=True)
    camera_disc = models.TextField(max_length=400, null=True, blank=True)
    sound_jac = models.BooleanField(default=False)
    os_choice = (
        ('ios', 'ios'),
        ('android', 'android'),
        ('windows', 'windows'),
    )
    os = models.CharField(choices=os_choice, default='android', max_length=10, null=True, blank=True)
    os_version = models.CharField(max_length=15, null=True, blank=True)
    persian_language = models.BooleanField(default=False)
    default_softwares = models.TextField(max_length=150, null=True, blank=True)
    sensors = models.TextField(max_length=150, null=True, blank=True)
    battery_changable = models.BooleanField(default=False)
    battery_prop = models.TextField(max_length=200, null=True, blank=True)
    others_disc = models.TextField(max_length=150, null=True, blank=True)
    summary_disc = models.TextField(max_length=150, null=True, blank=True)
    owner = models.ForeignKey(Sellers, on_delete=models.CASCADE)
    CountSell = models.PositiveSmallIntegerField(default=0)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
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
    def __str__(self):
        return self.code



# lion
class Tablet(models.Model):
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
    internal_capacity = models.CharField(max_length=25)
    slot_capacity = models.CharField(max_length=35)
    sim_card = models.BooleanField(default=False)
    os_choice = (
        ('ios', 'ios'),
        ('android', 'android'),
        ('windows', 'windows'),
    )
    os = models.CharField(choices=os_choice, default='android', max_length=20, null=True, blank=True)
    ram = models.CharField(max_length=15, null=True, blank=True)
    chipset = models.CharField(max_length=35, null=True, blank=True)
    gpu = models.CharField(max_length=35, null=True, blank=True)
    screen_type = models.CharField(max_length=10, null=True, blank=True)
    resolution = models.CharField(max_length=25, null=True, blank=True)
    camera = models.CharField(max_length=15, null=True, blank=True)
    selfie = models.CharField(max_length=15, null=True, blank=True)
    wifi = models.CharField(max_length=25, null=True, blank=True)
    bluetooth = models.CharField(max_length=14, null=True, blank=True)
    usb_type = models.CharField(max_length=15, null=True, blank=True)
    battery = models.CharField(max_length=15, null=True, blank=True)
    weight = models.CharField(max_length=15, null=True, blank=True)
    summary_disc = models.TextField(max_length=250, null=True, blank=True)
    owner = models.ForeignKey(Sellers, on_delete=models.CASCADE)
    CountSell = models.PositiveSmallIntegerField(default=0)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
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



