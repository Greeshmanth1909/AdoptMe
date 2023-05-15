"""access user upload from database"""

from upload.models import upload_img

db_objects = upload_img.objects.all()
