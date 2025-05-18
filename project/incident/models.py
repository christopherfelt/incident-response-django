from django.db import models

class IncidentTypes(models.TextChoices):
    FIRE = "fire", "Fire"
    ACCIDENT = "accident", "Accident"
    OTHER = "other", "Other"
    

class Incident(models.Model):
    
    name = models.CharField(max_length=200)
    incident_type = models.CharField(max_length=20, choices=IncidentTypes.choices, default=IncidentTypes.OTHER)
    
    
    def __str__(self):
        return f"{self.name}"
