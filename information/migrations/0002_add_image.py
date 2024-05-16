from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ("information","0001_initial"),
    ]
    operations = [
         migrations.AddField(
            model_name='Users',
            name='image',
            field=models.ImageField(upload_to='images/', null=True, blank=True),
        ),
    ]