from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Banner,AboutMe,Experience,Certification,MainSkill,Awards,Educations,Service,ServiceContainer,Project,ProjectInfo,HireMe,HireMeForm,Footer
from .serializer import BannerSerializer, AboutMeSerializer, ExperienceSerializer,CertificationSerialize,MainSkillSerializer, AwardsSerializer,EducationsSerializer,ServiceSerializer,ServiceContainerSerializer,ProjectSerilizer,ProjectInfoSerializer,HireMeSerializer,HireMeFormSerializer,FooterSerializer

# Create your views here.

#Banner view start here

class BannerViewset(ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

#Aboutme view start here

class AboutMeViewset(ModelViewSet):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer


class ExperienceViewset(ModelViewSet):
    queryset= Experience.objects.all()
    serializer_class = ExperienceSerializer


class CertificationViewset(ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerialize

class MainSkillViewset(ModelViewSet):
    queryset = MainSkill.objects.all()
    serializer_class = MainSkillSerializer


class AwardsViewset(ModelViewSet):
    queryset = Awards.objects.all()
    serializer_class = AwardsSerializer


class EducationsViewset(ModelViewSet):
    queryset = Educations.objects.all()
    serializer_class = EducationsSerializer

#Service view start here

class ServiceViewset(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceContainerViewset(ModelViewSet):
    queryset = ServiceContainer.objects.all()
    serializer_class = ServiceContainerSerializer


#Project view start here

class ProjectViewset(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerilizer

class ProjectInfoViewset(ModelViewSet):
    queryset = ProjectInfo.objects.all()
    serializer_class = ProjectInfoSerializer

#Hier me view start here 

class HireMeViewset(ModelViewSet):
    queryset = HireMe.objects.all()
    serializer_class = HireMeSerializer

class HireMeFormViewset(ModelViewSet):
    queryset = HireMeForm.objects.all()
    serializer_class = HireMeFormSerializer

#footer view start here

class FooterViewset(ModelViewSet):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer
