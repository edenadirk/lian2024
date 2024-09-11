from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(default='user.png', upload_to='profile_pics', blank=True)
    location = models.CharField(max_length=80)
    bio = models.CharField(max_length=500)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('EMERGENCY', 'Emergency Relief'),
        ('MEDICAL', 'Medical Aid'),
        ('EDUCATION', 'Education'),
        ('ENVIRONMENT', 'Environmental Causes'),
        ('ANIMAL', 'Animal Welfare'),
        ('COMMUNITY', 'Community Development'),
        ('HUNGER', 'Hunger Relief'),
        ('HOUSING', 'Housing and Shelter'),
        ('OTHER', 'Other Causes'),
    ]

    POST_TYPE_CHOICES = [
        ('OFFER', 'Donation Offer'),
        ('REQUEST', 'Donation Request'),
    ]

    title = models.CharField(max_length=100)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    body = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)
    photo = models.ImageField(default='default.jpg', upload_to='', blank=True)
    public = models.BooleanField(default=True)
    phonenumber = models.CharField(max_length=20)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='OTHER')
    location = models.CharField(max_length=100, blank=True, null=True)
    post_type = models.CharField(max_length=10, choices=POST_TYPE_CHOICES, default='OFFER')

    def __str__(self):
        return self.title

class DonationRequest(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    recipient = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='donation_requests')
    donor = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='donation_offers')
    status = models.CharField(max_length=20, choices=[
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled')
    ], default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Donation Request for {self.post.title}"

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    donation_request = models.ForeignKey(DonationRequest, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message[:20]}..."