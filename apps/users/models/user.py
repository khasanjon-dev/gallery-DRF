from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin
from django.db.models import CharField, ImageField, EmailField, BooleanField, DateTimeField


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_user_(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self.create_user_(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    image = ImageField(upload_to='images/users', null=True, blank=True)
    first_name = CharField('first name', max_length=150, null=True, blank=True)
    last_name = CharField('last name', max_length=150, null=True, blank=True)
    email = EmailField(max_length=250, unique=True, null=True, blank=True)
    phone = CharField(max_length=12, unique=True)
    is_staff = BooleanField('staff status', default=False)
    is_active = BooleanField('active', default=False)
    is_superuser = BooleanField('superuser', default=False)

    updated_at = DateTimeField(auto_now=True, null=True)
    created_at = DateTimeField(auto_now_add=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'phone'

    @property
    def user_category(self):
        return self.category.obj.all()
