from django.db import models

class Exercises(models.Model):

    choices = \
        (
            ('Barki', 'headers'),
            ('Plecy', 'plecy'),
            ('Uda', 'thigs'),
            ('Bicepsy', 'biceps'),
            ('Tricepsy', 'triceps'),
            ('Brzuch', 'stomag'),
            ('Klatka', 'chest'),
            ('Piszczele', 'crossbones')

        )

    exercise_name = models.CharField(max_length = 100)
    exercise_description = models.CharField(max_length = 500)
    exercise_type = models.CharField(max_length = 200, choices = choices)

# Create your models here.
