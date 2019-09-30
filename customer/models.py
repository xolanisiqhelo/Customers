from django.db import models


class Customer(models.Model):
    taskID = models.AutoField(primary_key=True, help_text="Linear record counter")
    customerCode = models.CharField(max_length=50, null=True,
                                    help_text="Primary key uniquely identifying each customer")
    # custFirstName = models.CharField(max_length=100, blank=True, null=True, help_text="customer firstname")
    # custLastname = models.CharField(max_length=100, blank=True, null=True, help_text="customer lastname")
    # deliveryaddress = models.CharField(max_length=100, blank=True, null=True,
    #                                    help_text="Delivery address on the customerApp")
    # statusCode = models.CharField(max_length=100, blank=True, null=True,
    #                               help_text="Reference code to status of  order/delivery")
    # statusDescription = models.CharField(max_length=100, blank=True, null=True,
    #                                      help_text="A verbose description of the status referenced "
    #                                                "from the Table/field: "
    #                                                "CodeReference/Description.")

    def __str__(self):
        return self.customerCode


class CodeReference(models.Model):
    statusCode = models.IntegerField(primary_key=True, help_text="Primary key Unique identifier")
    description = models.CharField(max_length=100, help_text="Verbose description related to the StatusCode",
                                   unique=False)

    def __str__(self):
        return self.description
