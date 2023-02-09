from django.db import models

class Products(models.Model):
    ID_PRODUCT = models.CharField('id_products', max_length=100, null=False, primary_key=True)
    NAME_PRODUCT = models.CharField('name_products', max_length=49, null=False)
    PRICE_PRODUCT = models.CharField('price_products', max_length=48, null=False)
    IMG_PRODUCT = models.URLField('img_products', null=False)
    EKRAN_PRODUCT = models.CharField('ekran_products', max_length=100, null=True)
    KAMERA_PRODUCT = models.CharField('kamera_products', max_length=100, null=True)
    DINAMIK_PRODUCT = models.CharField('dinamic_products', max_length=100, null=True)
    GODVIPUSKA_PRODUCT = models.CharField('godvipuska_products', max_length=100, null=True)
    
    def str(self):
            return self.NAME_PRODUCT

    class Meta:
        verbose_name = 'products'
        verbose_name_plural = 'products'

class Home_content(models.Model):
    ID_HOME = models.CharField('id_home', max_length=100, null=False, primary_key=True)
    PAGE_LINK_1 = models.CharField('ssilka_na_stranichku_1', max_length=30, blank=True)
    PAGE_LINK_2 = models.CharField('ssilka_na_stranichku_2', max_length=30, blank=True)
    IMAGE = models.ImageField(upload_to='product', null=True, blank=True, verbose_name='Изображение')

    
    def str(self):
            return self.title
    
    class Meta:
        verbose_name = 'content'
        verbose_name_plural = 'content'

class Home_Slider(models.Model):
    ID_H_SLIDER = models.CharField('id_home_slider', max_length=1, null=False, primary_key=True)
    TEXT_1 = models.CharField('text 1', max_length=150, blank=True)
    TEXT_2 = models.CharField('text 2', max_length=150, blank=True)
    PAGE_LINK = models.CharField('page_url', max_length=30, blank=True)
    IMG_SLIDER = models.URLField('img_slider', null=False)

    def str(self):
            return self.title
    
    class Meta:
        verbose_name = 'slider'
        verbose_name_plural = 'slider'



class Subs(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    MAIL = models.CharField('mail', max_length=300, blank=True)

    def str(self):
            return self.title

    class Meta:
        verbose_name = 'mail'
        verbose_name_plural = 'Sub'
