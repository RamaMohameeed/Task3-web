from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

ANGLE = [MinValueValidator(0), MaxValueValidator(180)]

class Pose(models.Model):
    name = models.CharField(max_length=64, blank=True, default="")
    m1 = models.PositiveSmallIntegerField(validators=ANGLE)
    m2 = models.PositiveSmallIntegerField(validators=ANGLE)
    m3 = models.PositiveSmallIntegerField(validators=ANGLE)
    m4 = models.PositiveSmallIntegerField(validators=ANGLE)
    m5 = models.PositiveSmallIntegerField(validators=ANGLE)
    m6 = models.PositiveSmallIntegerField(validators=ANGLE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name or f"Pose #{self.id}"

class Command(models.Model):
    # A snapshot to run, separate from saved poses
    m1 = models.PositiveSmallIntegerField(validators=ANGLE)
    m2 = models.PositiveSmallIntegerField(validators=ANGLE)
    m3 = models.PositiveSmallIntegerField(validators=ANGLE)
    m4 = models.PositiveSmallIntegerField(validators=ANGLE)
    m5 = models.PositiveSmallIntegerField(validators=ANGLE)
    m6 = models.PositiveSmallIntegerField(validators=ANGLE)
    status = models.PositiveSmallIntegerField(default=1)  # 1=pending, 0=consumed
    created_at = models.DateTimeField(auto_now_add=True)

