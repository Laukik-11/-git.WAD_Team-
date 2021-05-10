from django.db import models
from CommunityManagement import settings

# Create your models here.

# Model for Discussions


class Discussion(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    # Relation for the Resident Model
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Order by the latest first
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

# Model for the Replies on a discussion


class Reply(models.Model):
    body = models.TextField()
    # Relation with the user(Resident) posting the reply
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Relation with the parent discussion
    parent = models.ForeignKey(
        Discussion, on_delete=models.CASCADE, related_name="replies"
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ordered the latest last
        ordering = ["created_on"]

    def __str__(self):
        return str(self.created_by) + "'s Reply"
