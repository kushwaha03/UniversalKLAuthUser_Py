from django.contrib.auth.base_user import BaseUserManager

class UserKLManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, email, password=None,FirstName=None,LastName=None,**extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have an password')
        if not FirstName:
            raise ValueError('Users must have an First Name')
        user = self.model(
            email=self.normalize_email(email),
            FirstName = FirstName,
            LastName = LastName,
            **extra_fields,
            # Country=Country,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
