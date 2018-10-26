import uuid
from django.db import models

# Representation of a trash can deployment in the system
class TrashCan(models.Model):
    class Meta:
        pass
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

# Representation of a trash can fill state
class TrashState(models.Model):
      # Reference to the trash can
      trash_can = models.ForeignKey(TrashCan, on_delete=models.CASCADE)
      # Measurement acquisition time
      timestamp = models.DateTimeField()
      # In centimeters from the top cover
      fill_state = models.IntegerField()

