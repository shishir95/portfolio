from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

router.register('Banner', views.BannerViewset, basename="Banner")
router.register('AboutMe', views.AboutMeViewset, basename="AboutMe")
router.register('Experience', views.ExperienceViewset, basename="Experience")
router.register('Certification', views.CertificationViewset, basename="Certification")
router.register('MainSkill', views.MainSkillViewset, basename="MainSkill")
router.register('Award', views.AwardsViewset, basename="Award")
router.register('Education', views.EducationsViewset, basename="Education")
router.register('Service', views.ServiceViewset, basename="Service")
router.register('ServiceContainer', views.ServiceContainerViewset, basename="ServiceContainer")
router.register('Project', views.ProjectViewset, basename="Project")
router.register('Projectinfo', views.ProjectInfoViewset, basename="Projectinfo")
router.register('HireMe', views.HireMeViewset, basename="HireMe")
router.register('HireMeForm', views.HireMeFormViewset, basename="HireMeForm")
router.register('Footer', views.FooterViewset, basename="Footer")












urlpatterns = router.urls