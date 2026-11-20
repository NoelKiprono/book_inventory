from django.db import models

# Create your models here.

CATEGORIES = [
    ('politics', 'political category'),
    ('fiction', 'fiction category'),
    ('personal growth', 'personal growth category'),
    ('education', 'education category')
]


class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORIES)
    year = models.IntegerField()
    cost = models.IntegerField()
    isbn = models.CharField(unique=True, max_length=15, null=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'books'


# updates database after creating/updating/editing models
# python manage.py makemigrations
# python manage.py migrate


# .\.venv\Scripts\Activate.ps1   ---- venv activation
    



