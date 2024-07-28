from django.db import models
from django.contrib.auth.models import User

from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    image = models.ImageField(default='default.jpg', upload_to = 'profile_pics')
    full_name = models.CharField(max_length = 25)


    def __str__(self) -> str:
        return f"{self.user.username}'s Profile"


    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.width > 300 or img.height > 300:
            output_size: set = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)