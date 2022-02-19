from django.apps import AppConfig
from django.conf import settings
import myfitnesspal

client = None

class MfpConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MFP'

    global client
    client = myfitnesspal.Client('keiranbatten1998@gmail.com', password=settings.MFP_PASSWORD)
