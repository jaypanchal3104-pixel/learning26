from django.contrib import admin

# Register your models here.
from .models import Student,Product,car,StudentProfile,Category,Service,intern,internDetails,teacher,subject
# Register your models here.

admin.site.register(Student)
admin.site.register(Product)
admin.site.register(car)
admin.site.register(StudentProfile)
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(intern)
admin.site.register(internDetails)
admin.site.register(teacher)
admin.site.register(subject)