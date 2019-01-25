from __future__ import unicode_literals
from django.db import models


class Course(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=50)

    def __str__(self):
        return self.c_name


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_pic = models.CharField(max_length=3000)
    user_name = models.CharField(max_length=20)
    user_pass = models.CharField(max_length=30)
    user_fname = models.CharField(max_length=20)
    user_lname = models.CharField(max_length=20)
    user_email = models.EmailField()

    def __str__(self):
        return self.user_fname + " " + self.user_lname


class Tag(models.Model):
    t_id = models.AutoField(primary_key=True)
    t_name = models.CharField(max_length=20)

    def __str__(self):
        return self.t_name


class Department(models.Model):
    d_id = models.AutoField(primary_key=True)
    d_name = models.CharField(max_length=50)

    def __str__(self):
        return self.d_name


class University(models.Model):
    u_id = models.AutoField(primary_key=True)
    u_logo = models.CharField(max_length=3000)
    u_name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Universities"

    def __str__(self):
        return self.u_name


class Professor(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_pic = models.CharField(max_length=3000)
    p_fname = models.CharField(max_length=20)
    p_lname = models.CharField(max_length=20)
    u_id = models.ForeignKey(University, on_delete=models.CASCADE)
    d_id = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return "Prof. "+self.p_fname + " " + self.p_lname


class Note(models.Model):
    n_id = models.AutoField(primary_key=True)
    n_title = models.CharField(max_length=50)
    n_path = models.CharField(max_length=3000)
    n_year = models.IntegerField()
    n_upload_date_time = models.DateTimeField()
    n_average_rating = models.FloatField()
    u_id = models.ForeignKey(University, on_delete=models.CASCADE)
    d_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    p_id = models.ForeignKey(Professor, on_delete=models.CASCADE)
    c_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.n_title


class NoteTag(models.Model):
    t_id = models.ForeignKey(Tag, on_delete=models.CASCADE)
    n_id = models.ForeignKey(Note, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.t_id) + " " + str(self.n_id)


class Favourite(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    n_id = models.ForeignKey(Note, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user_id) + " " + str(self.n_id)


class Rating(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    n_id = models.ForeignKey(Note, on_delete=models.CASCADE)
    rating = models.FloatField(max_length=4)

    def __str__(self):
        return str(self.user_id) + " " + str(self.n_id) + " " + str(self.rating)


class Discussion(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    n_id = models.ForeignKey(Note, on_delete=models.CASCADE)
    comment = models.CharField(max_length=5000)

    def __str__(self):
        return str(self.user_id) + " commented on " + str(self.n_id) + ": \"" + self.comment +"\""



