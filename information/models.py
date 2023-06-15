from django.db import models

# Create your models here.

class Banner(models.Model):
     main_Titel = models.CharField(max_length=255)
     sub_titel = models.CharField(max_length=255)
     banner_image = models.ImageField()


#about me section start here 

class AboutMe(models.Model):
     aboutme_titel = models.CharField(max_length=100)
     aboutme_description = models.CharField(max_length=1000)

class Experience(models.Model):
     company_name = models.CharField(max_length=255)
     position = models.CharField(max_length=255)
     responsibility = models.CharField(max_length=1000)
     job_timeline = models.CharField(max_length=100)

class Certification(models.Model):
     certificate_name = models.CharField(max_length=255)
     inssued_By = models.CharField(max_length=255)

class MainSkill(models.Model):
     skill_name = models.CharField(max_length=255)
     skill_subtitel = models.CharField(max_length=255)

class Awards(models.Model):
     award_titel = models.CharField(max_length=255)
     time = models.CharField(max_length=100)

class Educations(models.Model):
     institute_name = models.CharField(max_length=255)
     degree_name = models.CharField(max_length=255)
     time_line = models.CharField(max_length=100)



#service section start here 

class Service(models.Model):
     titel = models.CharField(max_length=100)
     sub_titel = models.CharField(max_length=255)


class ServiceContainer(models.Model):
     logo = models.ImageField()
     titel = models.CharField(max_length=100)
     sub_titel = models.CharField(max_length=255)




#project section start here 

class Project(models.Model):
     titel = models.CharField(max_length=100)
     sub_titel = models.CharField(max_length=255)


class ProjectInfo(models.Model):
     image = models.ImageField()
     titel = models.CharField(max_length=100)
     sub_titel = models.CharField(max_length=255)



#Hire me section start here 

class HireMe(models.Model):
     titel = models.CharField(max_length=100)
     sub_titel = models.CharField(max_length=255)
     hireme_bigimage = models.ImageField()

class HireMeForm(models.Model):
      name = models.CharField(max_length=100)
      email = models.EmailField()
      subject = models.CharField(max_length=100)
      message =models.CharField(max_length=1000)

class Footer(models.Model):   
      footer = models.CharField(max_length=100)