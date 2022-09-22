from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
# Create your models here.
class UserManager(UserManager):
   def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
   def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
   def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    comment =models.TextField( verbose_name='自己紹介',blank=True, null=True, max_length=1000,)
    birthday = models.DateField( verbose_name='生年月日',blank=True, null=True)
    email = models.EmailField('メールアドレス', unique=True)
    nickname = models.CharField('ニックネーム', max_length=50)
    # プロフィール画像をavatarとして設定
    avatar = models.ImageField(upload_to='images', verbose_name='プロフィール画像', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')
    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)