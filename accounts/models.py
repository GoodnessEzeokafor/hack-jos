from django.db import models
from django.contrib.auth.models import(
    AbstractBaseUser,
    BaseUserManager
)
from django.contrib.auth.models import Group
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,username,password=None):
        if not username:
            raise ValueError("User must provide a username")
        if not password:
            raise ValueError("User must provide a password")
        
        user_obj = self.model(
            username=username,
            password=password
        )
        user_obj.set_password(password)
        user_obj.staff = False # set staff to False
        user_obj.admin=False # set admin property to false
        user_obj.is_active=True # set is_active property to trure
        user_obj.save(using=self._db)
        return user_obj # return user object

    def create_superuser(self,username, password=None):
        user = self.create_user(
            username,
            password=password
        )
        user.is_active = True
        user.admin = True
        user.staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username    = models.CharField(max_length=200,blank=False,null=False, unique=True)
    email       = models.EmailField(blank=False, null=False, unique=True)
    is_active   = models.BooleanField(default=True)
    staff       = models.BooleanField(default=False)
    admin       = models.BooleanField(default=False)
    objects     = UserManager()
    
    USERNAME_FIELD = 'username' # for authentication 
    REQUIRED_FIELDS = [] # required fields


    def __str__(self):
        return str(self.username)
    
    def has_perms(self, perm_list, obj=None):
        return True
    
    def has_perm(self, perm, obj=None):
        return True
    # def has_perm(self, perm, obj=None):
    #     """
    #     Return True if the user has each of the specified permissions. If
    #     object is passed, check if the user has all required perms for it.
    #     """
    #     return all(self.has_perm(perm, obj) for perm in perm_list)

    def has_module_perms(self, app_label):
        return True

    
    @property
    def is_staff(self):
        if self.admin:
            return True
        return self.admin

    @property
    def is_admin(self):
        return self.admin



class Participant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name   = models.CharField(max_length=200, blank=False, null=False)
    email       = models.EmailField(unique=True)

    def __str__(self):
        return str(self.full_name)


class Team(models.Model):
    team_name = models.CharField(max_length=200, blank=False, null=False)
    team_lead = models.CharField(max_length=200, blank=False, null=False)
    team_members= models.ManyToManyField(Participant)

    def __str__(self):
        return str(self.team_name)
