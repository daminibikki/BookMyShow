import os
import django

# ✅ Tell Django where your settings are
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookmyseat.settings')

# ✅ Setup Django manually
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = "admin"
email = "admin@example.com"
password = "admin123"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("✅ Superuser created!")
else:
    print("⚠️ Superuser already exists.")
