# Abstract User in Django

Django provides a flexible way to customize user authentication by allowing developers to extend the built-in `User` model. One of the most common approaches is using `AbstractUser`.

## Why Use AbstractUser?

By default, Django provides a built-in `User` model for authentication. However, in real-world applications, we often need to extend the user model to include additional fields like phone number, profile picture, or role-based permissions. Using `AbstractUser` allows us to do this while keeping Django's authentication framework intact.

## Difference Between AbstractUser and AbstractBaseUser

- **AbstractUser**: Extends Django’s built-in `User` model and provides default fields like `username`, `email`, `first_name`, `last_name`, etc. It is best when you only need to add extra fields without changing the default authentication behavior.
- **AbstractBaseUser**: Provides only the basic authentication functionality (`password`, `last_login`, etc.), allowing complete customization of the user model. It is best when you want to build a user model from scratch with a custom authentication mechanism.

## How to Use AbstractUser

### Step 1: Create a Custom User Model

```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.username
```

### Step 2: Update Django Settings

In `settings.py`, specify the custom user model:

```python
AUTH_USER_MODEL = 'your_app.CustomUser'
```

### Step 3: Apply Migrations

Run the following commands to create the necessary database tables:

```sh
python manage.py makemigrations
python manage.py migrate
```

### Step 4: Use the Custom User Model

When defining relationships, always reference the custom user model using `get_user_model()` instead of referencing `auth.User` directly:

```python
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
```

## Admin Panel Integration

To make the custom user model accessible in the Django admin panel, update `admin.py`:

```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("phone_number", "profile_picture")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
```

## Best Practices

- **Define the custom user model at the start of your project**. Changing it later requires significant database migrations.
- **Use `get_user_model()`** instead of directly referencing the model.
- **Customize authentication only when necessary**. If Django's default authentication suits your needs, extending `AbstractUser` is usually sufficient.

## Conclusion

Using `AbstractUser` in Django allows easy extension of the default authentication system without major modifications. It is the recommended approach when adding extra fields while keeping Django’s built-in authentication features intact.
