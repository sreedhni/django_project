from django.db import models
from company.models import Company
from users.models import User
class Job (models.Model):
    user = models. ForeignKey (User, on_delete=models.CASCADE)
    company = models. ForeignKey (Company, on_delete=models.CASCADE)
    title = models. CharField(max_length=100)
    location = models. CharField(max_length=100)
    salary = models. PositiveIntegerField(default=35000)
    is_available=models.BooleanField(default=True)
    timestamb=models.DateTimeField(auto_now_add=True)
    job_description = models.TextField(null=True,blank=True)
    required_qualifications = models.CharField(max_length=50,null=True,blank=True)
    responsibilities = models.TextField(null=True,blank=True)
    application_Deadline = models.DateField(null=True,blank=True)
    salary_Range = models.CharField(max_length=50,null=True,blank=True)
    option = (('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Contract', 'Contract'), ('etc', 'etc'))
    Employment_Type = models.CharField(choices=option, max_length=20,null=True,blank=True)
    Company_Benefits = models.TextField(null=True,blank=True)
    How_to_Apply = models.TextField(null=True,blank=True)
    cover_letter=models.CharField(max_length=20,null=True,blank=True)
    status_choices = (('Accepted', 'Accepted'), 
                      ('Declined', 'Declined'), 
                      ('Pending', 'Pending'))
    status = models.CharField(max_length=20, choices=status_choices,null=True)


    def __str__(self):
        return self.title
class ApplyJob(models.Model):
    status_choices = (('Accepted', 'Accepted'), 
                      ('Declined', 'Declined'), 
                      ('Pending', 'Pending'))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job= models.ForeignKey(Job, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=status_choices,default="Pending")
    resume=models.FileField(upload_to="resumes",null=True,blank=True)


class Notification(models.Model):
    sender = models.ForeignKey(User, related_name='sent_notifications', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Company, related_name='received_notifications', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)