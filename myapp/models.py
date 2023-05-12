from django.db import models
from cloudinary.models import CloudinaryField
from django.core.validators import FileExtensionValidator,MaxValueValidator
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150,verbose_name="Category name",help_text="Enter category name")
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Category'
        verbose_name = 'Category'
        verbose_name_plural= 'Categories'
class Test(models.Model):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,verbose_name="Category",help_text="Choose category",null=True,blank=True,related_name='category')
    file = models.FileField(verbose_name="Test File",help_text="Upload test file",validators=[FileExtensionValidator(allowed_extensions=["pdf",'doc','docx'])],upload_to="testfiles")
    uploaded = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)
    code = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return f"Test - {self.code}"
    def save(self, *args, **kwargs):
        super(Test, self).save(*args, **kwargs)
        self.code =int(self.id) + 1000
        super(Test, self).save(*args, **kwargs)
    @property
    def filesize(self):
        x = self.file.size
        y = 512000
        if x < y:
            value = round(x / 1000, 2)
            ext = ' kb'
        elif x < y * 1000:
            value = round(x / 1000000, 2)
            ext = ' Mb'
        else:
            value = round(x / 1000000000, 2)
            ext = ' Gb'
        return str(value) + ext
    class Meta:
        db_table = 'Test'
        verbose_name = 'Test '
        verbose_name_plural= 'Tests '
class Answers(models.Model):
    choice_answers = (
        ('A','A'),
        ('B','B'),
        ('C','C'),
        ('D','D')
    )
    test = models.ForeignKey(Test,on_delete=models.CASCADE,related_name='answers')
    answer = models.CharField(max_length=150,choices=choice_answers)
    def __str__(self):
        return self.answer
    class Meta:
        db_table = 'Answer'
        verbose_name = 'Answer '
        verbose_name_plural= 'Answers '
class BotUser(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True,verbose_name="Full Name")
    telegram_id = models.CharField(max_length=20,unique=True,verbose_name="Telegram ID")

    def __str__(self):
        if self.name:
            return self.name
        else:
            return f"{self.telegram_id} IDli foydalanuvchi"
class TestDone(models.Model):
    telegram_id = models.CharField(max_length=150,verbose_name="Telegram ID")
    name = models.CharField(max_length=150,verbose_name="Name",null=True,blank=True)
    test_code = models.CharField(max_length=150,verbose_name="Test Code")
    true_answers = models.CharField(max_length=150,verbose_name="True Answers",null=True,blank=True)
    false_answers = models.CharField(max_length=150, verbose_name="False Answers",null=True,blank=True)
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        if self.name:
            return f"{self.name}ning testi"
        else:
            return f"{self.telegram_id} IDli foydalanuvchining testi"
    class Meta:
        verbose_name= 'Test User'
        verbose_name_plural = 'Test Users'
class DailyTest(models.Model):
    telegram_id = models.CharField(max_length=150,verbose_name="Telegram ID")
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.telegram_id} IDli foydalanuvchi!"
    class Meta:
        verbose_name  = "Daily Test "
        verbose_name_plural = "Daily Tests "