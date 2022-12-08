from django.db import models
class ChatQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    quseston = models.TextField()
    answer = models.TextField()
    create_time = models.DateField(auto_now_add=True)


    @property
    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True
