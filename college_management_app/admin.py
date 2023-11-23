from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Notice,StudentResult,CustomUser, AdminHOD, Staffs, Courses, Subjects, Students, LeaveReportStudent, LeaveReportStaff,SessionYearModel
# Register your models here.
class UserModel(UserAdmin):
	pass


admin.site.register(CustomUser, UserModel)

admin.site.register(AdminHOD)
admin.site.register(Staffs)
admin.site.register(Courses)
admin.site.register(Subjects)
admin.site.register(SessionYearModel)
admin.site.register(Students)
admin.site.register(LeaveReportStudent)
admin.site.register(LeaveReportStaff)
admin.site.register(StudentResult)
admin.site.register(Notice)
