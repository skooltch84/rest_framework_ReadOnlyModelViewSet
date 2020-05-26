from django.db import models

DESCRIPTIONS = (
    (0, "Sunny"),
    (1, "Rain"),
    (3, "Cloudy"),
    (4, "Snow")
)


class Description(models.Model):
    """Model to describe the weather"""
    weather_description = models.IntegerField(choices=DESCRIPTIONS, default=0)
    temperature = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return str(self.created_on)
