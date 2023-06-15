from django.contrib import admin
from information.models import Banner,AboutMe,Experience,Certification,MainSkill,Awards,Educations,Service,ServiceContainer,Project,ProjectInfo,HireMe,HireMeForm,Footer
# Register your models here.

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['main_Titel','sub_titel','banner_image']
    list_per_page = 10

@admin.register(AboutMe)
class AboutmeAdmin(admin.ModelAdmin):
    list_display = ['aboutme_titel','aboutme_description']
    list_per_page = 10

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['company_name','position','responsibility','job_timeline']
    list_per_page = 10

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['certificate_name','inssued_By']
    list_per_page = 10

@admin.register(MainSkill)
class MainSkillAdmin(admin.ModelAdmin):
    list_display = ['skill_name','skill_subtitel']
    list_per_page = 10

@admin.register(Awards)
class AwardAdmin(admin.ModelAdmin):
    list_display = ['award_titel','time']
    list_per_page = 10

@admin.register(Educations)
class EducationsAdmin(admin.ModelAdmin):
    list_display = ['institute_name','degree_name','time_line']
    list_per_page = 10

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['titel','sub_titel']
    list_per_page = 10

@admin.register(ServiceContainer)
class ServiceContainerAdmin(admin.ModelAdmin):
    list_display = ['logo','titel','sub_titel']
    list_editable = ['titel','sub_titel']
    list_per_page = 10

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['titel','sub_titel']
    list_per_page = 10

@admin.register(ProjectInfo)
class ProjectInfoAdmin(admin.ModelAdmin):
    list_display = ['image','titel','sub_titel']
    list_editable=['titel','sub_titel']
    list_per_page = 10

@admin.register(HireMe)
class HireMeAdmin(admin.ModelAdmin):
    list_display = ['titel','sub_titel','hireme_bigimage']
    list_per_page = 10

@admin.register(HireMeForm)
class HireMeFormAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','subject']
    list_per_page = 10

@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ['footer']
    list_per_page = 10




