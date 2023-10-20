from django.db import models


class Person(models.Model):
    class Meta:
        abstract = True

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Student(Person):
    class Meta:
        db_table = 'Student'


class Teacher(Person):
    class Meta:
        db_table = 'Teacher'


class Homework(models.Model):
    class Meta:
        db_table = 'Homework'

    text = models.TextField()
    created = models.DateTimeField()
    deadline = models.DateTimeField()

    def __str__(self):
        return '{} {} {}'.format(self.text, self.created, self.deadline)


class HomeworkResult(models.Model):
    class Meta:
        db_table = 'HomeworkResult'

    author = models.ForeignKey('Student', on_delete=models.CASCADE)
    homework = models.ForeignKey('Homework', on_delete=models.CASCADE)
    solution = models.TextField()
    created = models.DateTimeField()

    def __str__(self):
        return '{} {} {}'.format(self.author, self.homework, self.solution)
