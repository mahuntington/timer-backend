from django.db import models
from datetime import timedelta 

class Session(models.Model):
    seconds = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def local_date(self):
        local_date = self.created_at - timedelta(hours=4)
        return local_date.strftime('%h %d, %Y at %I:%M:%S %p')

    def time_in_minutes(self):
        return int(self.seconds / 60)
