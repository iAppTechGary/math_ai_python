from django.db import models


class AppUser(models.Model):
    id = models.AutoField(primary_key=True)

    udid = models.CharField(max_length=255, unique=True)
    token = models.CharField(max_length=255, null=True)
    device_model = models.CharField(max_length=255, blank=True, null=True)
    app_version = models.CharField(max_length=255, blank=True, null=True)
    device_name = models.CharField(max_length=255, blank=True, null=True)
    os_version = models.CharField(max_length=255, blank=True, null=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.udid
    


class MathQuery(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    question = models.TextField()
    image_base64 = models.TextField(blank=True, null=True)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class UserSearch(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    input_type = models.CharField(max_length=20)  # "1 = text", "2 = image", "3 =pdf"
    prompt = models.TextField()  # what the user asked
    response = models.TextField()  # what GPT returned
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.udid} | {self.input_type} | {self.created_at.strftime('%Y-%m-%d %H:%M')}"