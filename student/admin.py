from django.contrib import admin
from .models import StudentDetailModel, StudentContactDetailModel, AddressDetailModel, StundetPrevEducationModel
# Register your models here.

admin.site.register(StudentDetailModel)
admin.site.register(StudentContactDetailModel)
admin.site.register(AddressDetailModel)
admin.site.register(StundetPrevEducationModel)