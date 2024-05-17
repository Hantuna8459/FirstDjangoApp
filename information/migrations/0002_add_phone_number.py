from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ("information","0001_initial"),
    ]
    operations = [
         migrations.AddField(
            model_name='Users',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
    ]