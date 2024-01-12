from django.db import models

# Create your models here.

STATUS = (
  ('Pending', 'Pending'),
  ('Approved', 'Approved'),
  ('Rejected', 'Rejected'),
)

class Bids(models.Model):
  user = models.ForeignKey('users.NewUser', on_delete=models.CASCADE)
  quantity = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
  price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
  start_time = models.DateTimeField(default=None, blank=True)
  close_time = models.DateTimeField(default=None, blank=True)
  status = models.CharField(choices=STATUS, max_length=10, default='Pending')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  reason = models.TextField(blank=True, null=True)

  def __str__(self):
      return f"{self.user} - {self.quantity}"
  
  class Meta:
    ordering = ['-created_at']
    verbose_name_plural = "Bids"

class BidsHistory(models.Model):
  user = models.ForeignKey('users.NewUser', on_delete=models.CASCADE)
  bid = models.ForeignKey('Bids', on_delete=models.CASCADE)
  name = models.CharField(max_length=100, blank=True)
  quantity = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
  price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
  start_time = models.DateTimeField(default=None, blank=True)
  close_time = models.DateTimeField(default=None, blank=True)
  status = models.CharField(choices=STATUS, max_length=10, default='Pending')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  reason = models.TextField(blank=True, null=True)

  def __str__(self):
      return f"{self.user} - {self.quantity}"
  
  # class Meta:
  #   ordering = ['-created_at']