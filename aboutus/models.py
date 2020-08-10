from django.db import models


# Create your models here.
class AboutUs(models.Model):
    PENDING, CONFIRMED, REJECTED = ('PE', 'CF', 'CL')
    ORDER_STATUSES = (
        (PENDING, 'Pending'),
        (CONFIRMED, 'Confirmed'),
        (REJECTED, 'Rejected'),
    )

    source = models.CharField(max_length=100, blank=True)
    pickUpFrom = models.CharField(max_length=100, blank=True)
    deliveryTo = models.CharField(max_length=100, blank=True)
    yourName = models.CharField(max_length=100, blank=True)
    emailId = models.EmailField(max_length=120, blank=True)
    phoneNo = models.CharField(max_length=25, blank=True)
    truckType = models.CharField(max_length=100, blank=True)
    dateTime = models.DateTimeField(auto_now_add=True)
    ord_status = models.CharField(max_length = 50, choices=ORDER_STATUSES, default=PENDING)
    

    def __str__(self):
        return self.yourName

    class Meta:
        #db_table = 'aboutus'
        verbose_name = 'View Order'
        verbose_name_plural = 'View Orders'
