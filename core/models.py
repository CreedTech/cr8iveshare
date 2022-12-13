from django.db import models
# from django.core.validators import FileExtensionValidator
from django.utils.text import slugify
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


# class Profile(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     id_user = models.IntegerField()
#     bio = models.TextField(blank=True)
#     profileImg = models.ImageField(
#         upload_to='profile_images', default="book-icon.png")
#     location = models.CharField(max_length=100, blank=True)

#     def __str__(self):
#         return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        slug = self.name
        self.slug = slugify(slug, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("core:video_category", kwargs={"pk": self.pk})
