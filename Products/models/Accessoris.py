from django.db import models
from .origin import *

class Headset(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True,upload_to='product-img/')
    image1 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    image2 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    title=models.CharField(max_length=50)
    price=models.FloatField(default=0)
    off_percent=models.IntegerField(default=0,null=True,blank=True)
    club_point=models.IntegerField(default=0,null=True,blank=True)
    count=models.PositiveSmallIntegerField(default=0,null=True,blank=True)
    color=models.ForeignKey(Color,on_delete=models.CASCADE,null=True,blank=True)
    guarantee=models.ForeignKey(Guarantee,on_delete=models.CASCADE)
    hashtag=models.TextField(max_length=60,null=True,blank=True)
    point=models.PositiveSmallIntegerField(default=0)
    code=models.CharField(max_length=15)
    weight=models.CharField(max_length=10,null=True,blank=True)
    publish_date=models.CharField(max_length=20,null=True,blank=True)
    contact_type=models.BooleanField(default=False)
    summary_disc=models.TextField(max_length=150,null=True,blank=True)
    owner=models.ForeignKey(Sellers,on_delete=models.CASCADE)
    CountSell=models.PositiveSmallIntegerField(default=0)
    Sale=models.BooleanField(default=False)
    date_created=models.DateField(auto_now=True)
    date_edited=models.DateTimeField(auto_now=True)
    def save(self):
        created = not self.pk
        super().save()
        if created:
            Product.objects.create(title=self.title,
                                   brand=self.brand,category=self.category,
                                   code=self.code,Sale=self.Sale,color=self.color,count=self.count,image=self.image,
                                   price=self.price,off_percent=self.off_percent,club_point=self.club_point,guarantee=self.guarantee,
                                   hashtag=self.hashtag,point=self.point,owner=self.owner)

class PowerBank(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True,upload_to='product-img/')
    image1 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    image2 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    title=models.CharField(max_length=50)
    price=models.FloatField(default=0)
    off_percent=models.IntegerField(default=0,null=True,blank=True)
    club_point=models.IntegerField(default=0,null=True,blank=True)
    count=models.PositiveSmallIntegerField(default=0,null=True,blank=True)
    color=models.ForeignKey(Color,on_delete=models.CASCADE,null=True,blank=True)
    guarantee=models.ForeignKey(Guarantee,on_delete=models.CASCADE)
    hashtag=models.TextField(max_length=60,null=True,blank=True)
    point=models.PositiveSmallIntegerField(default=0)
    code=models.CharField(max_length=15)
    publish_date=models.CharField(max_length=20, null=True, blank=True)
    dimensions=models.CharField(max_length=25, null=True, blank=True)
    weight_class=models.CharField(max_length=30, null=True, blank=True)
    weight=models.CharField(max_length=10, null=True, blank=True)
    capacity_limit=models.CharField(max_length=35, null=True, blank=True)
    capacity=models.CharField(max_length=35, null=True, blank=True)
    enter_volt=models.CharField(max_length=10, null=True, blank=True)
    out_volt=models.CharField(max_length=10, null=True, blank=True)
    enter_current=models.CharField(max_length=10, null=True, blank=True)
    out_current=models.CharField(max_length=10, null=True, blank=True)
    gate_count=models.CharField(max_length=10, null=True, blank=True)
    summary_disc=models.TextField(max_length=250, null=True, blank=True)
    body_material=models.CharField(max_length=20, null=True, blank=True)
    owner=models.ForeignKey(Sellers,on_delete=models.CASCADE)
    CountSell=models.PositiveSmallIntegerField(default=0)
    # product=models.ForeignKey(Product,on_delete=models.CASCADE,auto_created=True)
    Sale=models.BooleanField(default=False)
    def save(self):
        created = not self.pk
        super().save()
        if created:
            Product.objects.create(title=self.title,
                                   brand=self.brand, category=self.category,
                                   code=self.code, Sale=self.Sale, color=self.color, count=self.count,
                                   image=self.image,
                                   price=self.price, off_percent=self.off_percent, club_point=self.club_point,
                                   guarantee=self.guarantee,
                                   hashtag=self.hashtag, point=self.point,owner=self.owner)


class ChargerAdabter(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True,upload_to='product-img/')
    image1 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    image2 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    title=models.CharField(max_length=50)
    price=models.FloatField(default=0)
    off_percent=models.IntegerField(default=0,null=True,blank=True)
    club_point=models.IntegerField(default=0,null=True,blank=True)
    count=models.PositiveSmallIntegerField(default=0,null=True,blank=True)
    color=models.ForeignKey(Color, on_delete=models.CASCADE, null=True, blank=True)
    guarantee=models.ForeignKey(Guarantee,on_delete=models.CASCADE)
    hashtag=models.TextField(max_length=60,null=True,blank=True)
    point=models.PositiveSmallIntegerField(default=0)
    code=models.CharField(max_length=15)
    dimensions=models.CharField(max_length=25, null=True, blank=True)
    enter_volt=models.CharField(max_length=25, null=True, blank=True)
    out_gate_count=models.PositiveSmallIntegerField()
    output_type_gate=models.CharField(max_length=20, null=True, blank=True)
    summary_disc=models.TextField(max_length=250, null=True, blank=True)
    owner=models.ForeignKey(Sellers,on_delete=models.CASCADE)
    CountSell=models.PositiveSmallIntegerField(default=0)
    type_choice=(
        ('normal','normal'),
        ('lighter','lighter')
    )
    type=models.CharField(choices=type_choice,max_length=9,default=1)
    # product=models.ForeignKey(Product,on_delete=models.CASCADE,auto_created=True)
    Sale=models.BooleanField(default=False)
    def save(self):
        created = not self.pk
        super().save()
        if created:
            Product.objects.create(title=self.title,
                                   brand=self.brand, category=self.category,
                                   code=self.code, Sale=self.Sale, color=self.color, count=self.count,
                                   image=self.image,
                                   price=self.price, off_percent=self.off_percent, club_point=self.club_point,
                                   guarantee=self.guarantee,
                                   hashtag=self.hashtag, point=self.point,owner=self.owner)


class FlashMemory(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True,upload_to='product-img/')
    image1 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    image2 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    title=models.CharField(max_length=50)
    price=models.FloatField(default=0)
    off_percent=models.IntegerField(default=0,null=True,blank=True)
    club_point=models.IntegerField(default=0,null=True,blank=True)
    count=models.PositiveSmallIntegerField(default=0,null=True,blank=True)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    guarantee=models.ForeignKey(Guarantee,on_delete=models.CASCADE)
    hashtag=models.TextField(max_length=60,null=True,blank=True)
    point=models.PositiveSmallIntegerField(default=0)
    code=models.CharField(max_length=15)
    dimensions=models.CharField(max_length=25, null=True, blank=True)
    capacity=models.CharField(max_length=5, null=True, blank=True)
    weight=models.CharField(max_length=10, null=True, blank=True)
    gate_type=models.CharField(max_length=10, null=True, blank=True)
    owner=models.ForeignKey(Sellers,on_delete=models.CASCADE)
    CountSell=models.PositiveSmallIntegerField(default=0)
    Sale=models.BooleanField(default=False)
    def save(self):
        created = not self.pk
        super().save()
        if created:
            Product.objects.create(title=self.title,
                                   brand=self.brand, category=self.category,
                                   code=self.code, Sale=self.Sale, color=self.color, count=self.count,
                                   image=self.image,
                                   price=self.price, off_percent=self.off_percent, club_point=self.club_point,
                                   guarantee=self.guarantee,
                                   hashtag=self.hashtag, point=self.point,owner=self.owner)


class mouse(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True,upload_to='product-img/')
    image1 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    image2 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    title=models.CharField(max_length=50)
    price=models.FloatField(default=0)
    off_percent=models.IntegerField(default=0,null=True,blank=True)
    club_point=models.IntegerField(default=0,null=True,blank=True)
    count=models.PositiveSmallIntegerField(default=0,null=True,blank=True)
    color=models.ForeignKey(Color,on_delete=models.CASCADE,null=True,blank=True)
    guarantee=models.ForeignKey(Guarantee,on_delete=models.CASCADE)
    hashtag=models.TextField(max_length=60,null=True,blank=True)
    point=models.PositiveSmallIntegerField(default=0)
    code=models.CharField(max_length=15)
    class_type=models.CharField(max_length=20,null=True,blank=True)
    dimetions=models.CharField(max_length=35, null=True, blank=True)
    weight=models.CharField(max_length=10, null=True, blank=True)
    contact_type_choice=(
        ('wire','wire'),
        ('bluetooth','bluetooth'),
        ('wifi','wifi'),
    )
    contact_type=models.CharField(choices=contact_type_choice,max_length=20)
    cable_lenght=models.CharField(max_length=25, null=True, blank=True)
    contact_gate=models.CharField(max_length=25, null=True, blank=True)
    charge_gate=models.CharField(max_length=25, null=True, blank=True)
    battery_monitoring=models.BooleanField(default=False)
    OnOff_key=models.BooleanField(default=False)
    hand_choice=(
        ('left','left'),
        ('right','right'),
    )
    hand=models.CharField(default='right',choices=hand_choice,max_length=15)
    sensor_type_choice=(
        ('laser','laser'),
        ('oprical','oprical')
    )
    resolution=models.CharField(max_length=50, null=True, blank=True)
    mouse_key_count=models.PositiveSmallIntegerField()
    key_lifeTime=models.CharField(max_length=50,null=True,blank=True)
    programmable_gate=models.BooleanField(default=False)
    rgb=models.BooleanField(default=False)
    owner=models.ForeignKey(Sellers,on_delete=models.CASCADE)
    CountSell=models.PositiveSmallIntegerField(default=0)
    # product=models.ForeignKey(Product,on_delete=models.CASCADE,auto_created=True)
    Sale=models.BooleanField(default=False)
    def save(self):
        created = not self.pk
        super().save()
        if created:
            Product.objects.create(title=self.title,
                                   brand=self.brand, category=self.category,
                                   code=self.code, Sale=self.Sale, color=self.color, count=self.count,
                                   image=self.image,
                                   price=self.price, off_percent=self.off_percent, club_point=self.club_point,
                                   guarantee=self.guarantee,
                                   hashtag=self.hashtag, point=self.point,owner=self.owner)


class BluetoothDongle(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True,upload_to='product-img/')
    image1 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    image2 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    title=models.CharField(max_length=50)
    price=models.FloatField(default=0)
    off_percent=models.IntegerField(default=0,null=True,blank=True)
    club_point=models.IntegerField(default=0,null=True,blank=True)
    count=models.PositiveSmallIntegerField(default=0,null=True,blank=True)
    color=models.ForeignKey(Color,on_delete=models.CASCADE,null=True,blank=True)
    guarantee=models.ForeignKey(Guarantee,on_delete=models.CASCADE)
    hashtag=models.TextField(max_length=60,null=True,blank=True)
    point=models.PositiveSmallIntegerField(default=0)
    code=models.CharField(max_length=15)
    owner=models.ForeignKey(Sellers,on_delete=models.CASCADE)
    material_body=models.CharField(max_length=30, null=True, blank=True)
    blutooth_version=models.CharField(max_length=20, null=True, blank=True)
    summary_desc=models.TextField(max_length=150, null=True, blank=True)
    CountSell=models.PositiveSmallIntegerField(default=0)
    # product=models.ForeignKey(Product,on_delete=models.CASCADE,auto_created=True)
    Sale=models.BooleanField(default=False)
    def save(self):
        created = not self.pk
        super().save()
        if created:
            Product.objects.create(title=self.title,
                                   brand=self.brand, category=self.category,
                                   code=self.code, Sale=self.Sale, color=self.color, count=self.count,
                                   image=self.image,
                                   price=self.price, off_percent=self.off_percent, club_point=self.club_point,
                                   guarantee=self.guarantee,
                                   hashtag=self.hashtag, point=self.point,owner=self.owner)


from .MobileVsTablets import Mobile
class MobileCovers(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True,upload_to='product-img/')
    image1 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    image2 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    title=models.CharField(max_length=50)
    price=models.FloatField(default=0)
    off_percent=models.IntegerField(default=0,null=True,blank=True)
    club_point=models.IntegerField(default=0,null=True,blank=True)
    count=models.PositiveSmallIntegerField(default=0,null=True,blank=True)
    color=models.ForeignKey(Color,on_delete=models.CASCADE,null=True,blank=True)
    guarantee=models.ForeignKey(Guarantee,on_delete=models.CASCADE)
    hashtag=models.TextField(max_length=60,null=True,blank=True)
    point=models.PositiveSmallIntegerField(default=0)
    code=models.CharField(max_length=15)
    owner=models.ForeignKey(Sellers,on_delete=models.CASCADE)
    mobile=models.ForeignKey(Mobile,on_delete=models.CASCADE)
    material_body=models.CharField(max_length=30, null=True, blank=True)
    summary_desc=models.TextField(max_length=150, null=True, blank=True)
    CountSell=models.PositiveSmallIntegerField(default=0)
    # product=models.ForeignKey(Product,on_delete=models.CASCADE,auto_created=True)
    Sale=models.BooleanField(default=False)
    def save(self):
        created = not self.pk
        super().save()
        if created:
            Product.objects.create(title=self.title,
                                   brand=self.brand, category=self.category,
                                   code=self.code, Sale=self.Sale, color=self.color, count=self.count,
                                   image=self.image,
                                   price=self.price, off_percent=self.off_percent, club_point=self.club_point,
                                   guarantee=self.guarantee,
                                   hashtag=self.hashtag, point=self.point,owner=self.owner)


class ScreenGlass(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True,upload_to='product-img/')
    image1 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    image2 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    title=models.CharField(max_length=50)
    price=models.FloatField(default=0)
    off_percent=models.IntegerField(default=0,null=True,blank=True)
    club_point=models.IntegerField(default=0,null=True,blank=True)
    count=models.PositiveSmallIntegerField(default=0,null=True,blank=True)
    color=models.ForeignKey(Color,on_delete=models.CASCADE,null=True,blank=True)
    guarantee=models.ForeignKey(Guarantee,on_delete=models.CASCADE)
    hashtag=models.TextField(max_length=60,null=True,blank=True)
    point=models.PositiveSmallIntegerField(default=0)
    code=models.CharField(max_length=15)
    owner=models.ForeignKey(Sellers,on_delete=models.CASCADE)
    # mobile=models.ForeignKey(Mobile, on_delete=models.CASCADE)    
    anti_hurt=models.BooleanField(default=True)
    reflex=models.BooleanField(default=True)
    Scratch=models.BooleanField(default=True)
    Thickness=models.CharField(max_length=25, null=True, blank=True)
    FrontOrBack_choice=(
        ('front','front'),
        ('back','back')
    )
    FrontOrBack=models.CharField(default='1',choices=FrontOrBack_choice,max_length=10, null=True, blank=True)
    summary_desc=models.TextField(max_length=200, null=True, blank=True)
    CountSell=models.PositiveSmallIntegerField(default=0)
    # product=models.ForeignKey(Product,on_delete=models.CASCADE,auto_created=True)
    Sale=models.BooleanField(default=False)
    def save(self):
        created = not self.pk
        super().save()
        if created:
            Product.objects.create(title=self.title,
                                   brand=self.brand, category=self.category,
                                   code=self.code, Sale=self.Sale, color=self.color, count=self.count,
                                   image=self.image,
                                   price=self.price, off_percent=self.off_percent, club_point=self.club_point,
                                   guarantee=self.guarantee,
                                   hashtag=self.hashtag, point=self.point,owner=self.owner)


class SmartWatch(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True,upload_to='product-img/')
    image1 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    image2 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    title=models.CharField(max_length=50)
    price=models.FloatField(default=0)
    off_percent=models.IntegerField(default=0,null=True,blank=True)
    club_point=models.IntegerField(default=0,null=True,blank=True)
    count=models.PositiveSmallIntegerField(default=0,null=True,blank=True)
    color=models.ForeignKey(Color,on_delete=models.CASCADE,null=True,blank=True)
    guarantee=models.ForeignKey(Guarantee,on_delete=models.CASCADE)
    hashtag=models.TextField(max_length=60,null=True,blank=True)
    point=models.PositiveSmallIntegerField(default=0)
    code=models.CharField(max_length=15)
    owner=models.ForeignKey(Sellers,on_delete=models.CASCADE)
    gender_choice=(
        ('آقایان','آقایان'),
        ('خانم ها','خانم ها'),
        ('آقایان و خانم ها','آقایان و خانم ها')
    )
    gender=models.CharField(default='3',choices=gender_choice,max_length=35)
    dimension=models.CharField(max_length=50, null=True, blank=True)
    weight=models.CharField(max_length=25, null=True, blank=True)
    glass_material=models.CharField(max_length=35, null=True, blank=True)
    body_material=models.CharField(max_length=35, null=True, blank=True)
    body_desc=models.CharField(max_length=35, null=True, blank=True)
    dam_material=models.CharField(max_length=35, null=True, blank=True)
    dam_type=models.CharField(max_length=25, null=True, blank=True)
    colorfull_screen=models.BooleanField(default=True)
    touch_screen=models.BooleanField(default=True)
    screen_dimension=models.CharField(max_length=35, null=True, blank=True)
    simCard=models.BooleanField(default=False)
    gps=models.BooleanField()
    descriptions=models.TextField(max_length=900, null=True, blank=True)
    CountSell=models.PositiveSmallIntegerField(default=0)
    # product=models.ForeignKey(Product,on_delete=models.CASCADE,auto_created=True)
    Sale=models.BooleanField(default=False)
    def save(self):
        created = not self.pk
        super().save()
        if created:
            Product.objects.create(title=self.title,
                                   brand=self.brand, category=self.category,
                                   code=self.code, Sale=self.Sale, color=self.color, count=self.count,
                                   image=self.image,
                                   price=self.price, off_percent=self.off_percent, club_point=self.club_point,
                                   guarantee=self.guarantee,
                                   hashtag=self.hashtag, point=self.point,owner=self.owner)


class SDCards(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True,upload_to='product-img/')
    image1 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    image2 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    title=models.CharField(max_length=50)
    price=models.FloatField(default=0)
    off_percent=models.IntegerField(default=0,null=True,blank=True)
    club_point=models.IntegerField(default=0,null=True,blank=True)
    count=models.PositiveSmallIntegerField(default=0,null=True,blank=True)
    color=models.ForeignKey(Color,on_delete=models.CASCADE,null=True,blank=True)
    guarantee=models.ForeignKey(Guarantee,on_delete=models.CASCADE)
    hashtag=models.TextField(max_length=60,null=True,blank=True)
    point=models.PositiveSmallIntegerField(default=0)
    code=models.CharField(max_length=15)
    owner=models.ForeignKey(Sellers,on_delete=models.CASCADE)
    dimenson=models.CharField(max_length=35, null=True, blank=True)
    type_choice=(
        ('SD','SD'),
        ('Micro','Micro')
    )
    type=models.CharField(default='Micro',choices=type_choice,max_length=10)
    capacity_choice=(
        ('8','8'),
        ('16','16'),
        ('32','32'),
        ('64','64'),
        ('128','128'),
        ('256','256'),
    )
    capacity=models.CharField(choices=capacity_choice,default='32',max_length=10)
    classType=models.CharField(default='10',max_length=15, null=True, blank=True)
    read_speed=models.CharField(max_length=35, null=True, blank=True)
    write_speed=models.CharField(max_length=35, null=True, blank=True)
    Water_proof=models.BooleanField(default=True)
    anti_hurt=models.BooleanField(default=True)
    summary_desc=models.TextField(max_length=150,null=True,blank=True)
    CountSell=models.PositiveSmallIntegerField(default=0)
    # product=models.ForeignKey(Product,on_delete=models.CASCADE,auto_created=True)
    Sale=models.BooleanField(default=False)
    def save(self):
        created = not self.pk
        super().save()
        if created:
            Product.objects.create(title=self.title,
                                   brand=self.brand, category=self.category,
                                   code=self.code, Sale=self.Sale, color=self.color, count=self.count,
                                   image=self.image,
                                   price=self.price, off_percent=self.off_percent, club_point=self.club_point,
                                   guarantee=self.guarantee,
                                   hashtag=self.hashtag, point=self.point,owner=self.owner)


class MonopadVsHolder(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True,upload_to='product-img/')
    image1 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    image2 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    title=models.CharField(max_length=50)
    price=models.FloatField(default=0)
    off_percent=models.IntegerField(default=0,null=True,blank=True)
    club_point=models.IntegerField(default=0,null=True,blank=True)
    count=models.PositiveSmallIntegerField(default=0,null=True,blank=True)
    color=models.ForeignKey(Color,on_delete=models.CASCADE,null=True,blank=True)
    guarantee=models.ForeignKey(Guarantee,on_delete=models.CASCADE)
    hashtag=models.TextField(max_length=60,null=True,blank=True)
    point=models.PositiveSmallIntegerField(default=0)
    code=models.CharField(max_length=15)
    owner=models.ForeignKey(Sellers,on_delete=models.CASCADE)
    weight=models.CharField(max_length=25, null=True, blank=True)
    max_lenght=models.CharField(max_length=25, null=True, blank=True)
    min_lenght=models.CharField(max_length=25, null=True, blank=True)
    weight_carrier=models.CharField(max_length=35, null=True, blank=True)
    summary_desc=models.TextField(max_length=350, null=True, blank=True)
    CountSell=models.PositiveSmallIntegerField(default=0)
    # product=models.ForeignKey(Product,on_delete=models.CASCADE,auto_created=True)
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


class ElectricConverter(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True,upload_to='product-img/')
    image1 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    image2 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    title=models.CharField(max_length=50)
    price=models.FloatField(default=0)
    off_percent=models.IntegerField(default=0,null=True,blank=True)
    club_point=models.IntegerField(default=0,null=True,blank=True)
    count=models.PositiveSmallIntegerField(default=0,null=True,blank=True)
    color=models.ForeignKey(Color,on_delete=models.CASCADE,null=True,blank=True)
    guarantee=models.ForeignKey(Guarantee,on_delete=models.CASCADE)
    hashtag=models.TextField(max_length=60,null=True,blank=True)
    point=models.PositiveSmallIntegerField(default=0)
    code=models.CharField(max_length=15)
    owner=models.ForeignKey(Sellers,on_delete=models.CASCADE)
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


class CameraGlass(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True,upload_to='product-img/')
    image1 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    image2 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    title=models.CharField(max_length=50)
    price=models.FloatField(default=0)
    off_percent=models.IntegerField(default=0,null=True,blank=True)
    club_point=models.IntegerField(default=0,null=True,blank=True)
    count=models.PositiveSmallIntegerField(default=0,null=True,blank=True)
    color=models.ForeignKey(Color,on_delete=models.CASCADE,null=True,blank=True)
    guarantee=models.ForeignKey(Guarantee,on_delete=models.CASCADE)
    hashtag=models.TextField(max_length=60,null=True,blank=True)
    point=models.PositiveSmallIntegerField(default=0)
    code=models.CharField(max_length=15)
    owner=models.ForeignKey(Sellers,on_delete=models.CASCADE)
    mobile=models.ForeignKey(Mobile, on_delete=models.CASCADE)
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

class Modem(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True,upload_to='product-img/')
    image1 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    image2 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    title=models.CharField(max_length=50)
    price=models.FloatField(default=0)
    off_percent=models.IntegerField(default=0,null=True,blank=True)
    club_point=models.IntegerField(default=0,null=True,blank=True)
    count=models.PositiveSmallIntegerField(default=0,null=True,blank=True)
    color=models.ForeignKey(Color,on_delete=models.CASCADE,null=True,blank=True)
    guarantee=models.ForeignKey(Guarantee,on_delete=models.CASCADE)
    hashtag=models.TextField(max_length=60,null=True,blank=True)
    point=models.PositiveSmallIntegerField(default=0)
    code=models.CharField(max_length=15)
    owner=models.ForeignKey(Sellers,on_delete=models.CASCADE)
    gates=models.CharField(max_length=150,null=True,blank=True)
    Count_gates=models.CharField(max_length=10,null=True,blank=True)
    frequens_support=models.CharField(max_length=50,null=True,blank=True)
    Anten_count=models.PositiveSmallIntegerField(default=1)
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

class MobileBattery(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True,upload_to='product-img/')
    image1 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    image2 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    title=models.CharField(max_length=50)
    price=models.FloatField(default=0)
    off_percent=models.IntegerField(default=0,null=True,blank=True)
    club_point=models.IntegerField(default=0,null=True,blank=True)
    count=models.PositiveSmallIntegerField(default=0,null=True,blank=True)
    color=models.ForeignKey(Color,on_delete=models.CASCADE,null=True,blank=True)
    guarantee=models.ForeignKey(Guarantee,on_delete=models.CASCADE)
    hashtag=models.TextField(max_length=60,null=True,blank=True)
    point=models.PositiveSmallIntegerField(default=0)
    code=models.CharField(max_length=15)
    owner=models.ForeignKey(Sellers,on_delete=models.CASCADE)
    mobile=models.ForeignKey(Mobile, on_delete=models.CASCADE)
    capacity=models.CharField(max_length=55,null=True,blank=True)
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

class AuxCable(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True,upload_to='product-img/')
    image1 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    image2 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    title=models.CharField(max_length=50)
    price=models.FloatField(default=0)
    off_percent=models.IntegerField(default=0,null=True,blank=True)
    club_point=models.IntegerField(default=0,null=True,blank=True)
    count=models.PositiveSmallIntegerField(default=0,null=True,blank=True)
    color=models.ForeignKey(Color,on_delete=models.CASCADE,null=True,blank=True)
    guarantee=models.ForeignKey(Guarantee,on_delete=models.CASCADE)
    hashtag=models.TextField(max_length=60,null=True,blank=True)
    point=models.PositiveSmallIntegerField(default=0)
    code=models.CharField(max_length=15)
    summary_desc=models.TextField(max_length=350, null=True, blank=True)
    owner=models.ForeignKey(Sellers,on_delete=models.CASCADE)
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

class Converter(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True,upload_to='product-img/')
    image1 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    image2 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    title=models.CharField(max_length=50)
    price=models.FloatField(default=0)
    off_percent=models.IntegerField(default=0,null=True,blank=True)
    club_point=models.IntegerField(default=0,null=True,blank=True)
    count=models.PositiveSmallIntegerField(default=0,null=True,blank=True)
    color=models.ForeignKey(Color,on_delete=models.CASCADE,null=True,blank=True)
    guarantee=models.ForeignKey(Guarantee,on_delete=models.CASCADE)
    hashtag=models.TextField(max_length=60,null=True,blank=True)
    point=models.PositiveSmallIntegerField(default=0)
    code=models.CharField(max_length=15)
    summary_desc=models.TextField(max_length=350, null=True, blank=True)
    type_choice=(
        ('Lighting To Type C','Lighting To Type C'),
        ('USB To Type C','USB To Type C'),
        ('Type C To Type C','Type C To Type C'),
        ('USB To Micro','USB To Micro'),
        ('Lighting To Micro','Lighting To Micro'),
        ('Type C To Micro','Type C To Micro'),
        ('Lighting To USB','Lighting To USB'),
        ('Lighting To AUX','Lighting To AUX'),
        ('Type C To AUX','Type C To AUX'),
        ('USB To AUX','USB To AUX')
    )
    type=models.CharField(max_length=40,choices=type_choice)
    owner=models.ForeignKey(Sellers,on_delete=models.CASCADE)
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

class Hcovers(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True,upload_to='product-img/')
    image1 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    image2 = models.ImageField(null=True, blank=True, upload_to='product-img/')
    title=models.CharField(max_length=50)
    price=models.FloatField(default=0)
    off_percent=models.IntegerField(default=0,null=True,blank=True)
    club_point=models.IntegerField(default=0,null=True,blank=True)
    count=models.PositiveSmallIntegerField(default=0,null=True,blank=True)
    color=models.ForeignKey(Color,on_delete=models.CASCADE,null=True,blank=True)
    guarantee=models.ForeignKey(Guarantee,on_delete=models.CASCADE)
    hashtag=models.TextField(max_length=60,null=True,blank=True)
    point=models.PositiveSmallIntegerField(default=0)
    code=models.CharField(max_length=15)
    summary_desc=models.TextField(max_length=350, null=True, blank=True)
    owner=models.ForeignKey(Sellers,on_delete=models.CASCADE)
    Sale=models.BooleanField(default=False)
    Headset=models.ForeignKey(Headset,on_delete=models.CASCADE,null=True,blank=True)
    def save(self):
        created = not self.pk
        super().save()
        if created:
            Product.objects.create(title=self.title,

                                   brand=self.brand,category=self.category,
                                   code=self.code,Sale=self.Sale,color=self.color,count=self.count,image=self.image,
                                   price=self.price,off_percent=self.off_percent,club_point=self.club_point,guarantee=self.guarantee,
                                   hashtag=self.hashtag,point=self.point,owner=self.owner)






    

    
    
    







    







    


    
    
    

    



    
    


