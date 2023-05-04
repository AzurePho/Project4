from django.db import models

# Create your models here.

class Game(models.Model): 
    title = models.CharField(max_length=50)
    cover_image = models.CharField(max_length=300, blank=True, null=True)
    dev=models.ForeignKey('devs.Dev', related_name="games", on_delete=models.CASCADE)
    genres = models.ManyToManyField('genres.Genre', related_name="games")
    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name='albums',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title}"