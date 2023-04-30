from django.db import models


class RatingChoices(models.TextChoices):
    G = "G"
    PG = "PG"
    PG13 = "PG-13"
    R = "R"
    NC17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, default=None, null=True)
    rating = models.CharField(max_length=20, choices=RatingChoices.choices, default=RatingChoices.G, null=True)
    synopsis = models.TextField(null=True, default=None)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="movies", null=True)


class MovieOrder(models.Model):
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="movies_orders")
    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE, related_name="movies_orders")
