from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profile_pic = models.ImageField(default="default.jpeg", upload_to="profile_images")

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return f"/public-profile/{self.user.username}/"

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")