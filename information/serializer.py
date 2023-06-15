from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Banner,AboutMe,Experience,Certification,MainSkill,Awards,Educations,Service,ServiceContainer,Project,ProjectInfo,HireMe,HireMeForm,Footer

#Banner serializer section start here 

class BannerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Banner
        fields = ['main_Titel','sub_titel','banner_image']

#About me serializer section start here 

class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMe
        fields = ['aboutme_titel','aboutme_description']

class ExperienceSerializer(serializers.ModelSerializer):
     class Meta:
         model = Experience
         fields = ['company_name','position','responsibility','job_timeline']

class CertificationSerialize(serializers.ModelSerializer):
     class Meta:
         model = Certification
         fields = ['certificate_name','inssued_By']

class MainSkillSerializer(serializers.ModelSerializer):
     class Meta:
         model = MainSkill
         fields = ['skill_name','skill_subtitel']  

class AwardsSerializer(serializers.ModelSerializer):
     class Meta:
         model = Awards
         fields = ['award_titel','time']

class EducationsSerializer(serializers.ModelSerializer):
      class Meta:
          model = Educations
          fields = ['institute_name','degree_name','time_line']       
        
#Service serializer section start here 

class  ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['titel','sub_titel']

class  ServiceContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceContainer
        fields = ['logo','titel','sub_titel']       

#Project serializer section start here 

class ProjectSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['titel','sub_titel']

class  ProjectInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectInfo
        fields = ['image','titel','sub_titel']

#Hire me serializer start here 

class HireMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HireMe
        fields = ['titel','sub_titel','hireme_bigimage']

class HireMeFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = HireMeForm
        fields = ['name','email','subject','subject']

#Footer serializer start here 

class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = ['footer']