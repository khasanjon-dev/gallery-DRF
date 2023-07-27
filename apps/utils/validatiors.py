import os
import re

from django.core.validators import RegexValidator
from django.utils import timezone

pattern = r'^(\+?998)?([. \-])?(\d[0-9])([. \-])?(\d){3}([. \-])?(\d){2}([. \-])?(\d){2}$'

phone_regex = RegexValidator(
    regex=r'^998[0-9]{9}$',
    message="Phone number must be entered in the format: '998 [XX] [XXX XX XX]'. Up to 12 digits allowed."
)


def is_phone_number_valid(phone):
    if not phone:
        return False, 'Please enter a phone number!'

    if not re.match(pattern, phone):
        return False, 'Please enter a valid phone number!'

    return True, phone


def generate_correct_phone_number(phone_num):
    if len(phone_num) <= 12:
        if len(phone_num.split()) == 1:
            return phone_num if len(phone_num) > 9 else '998' + phone_num
        else:
            c_ph_n = ''.join(c for c in phone_num if c.isdigit())
            return '998' + c_ph_n
    else:
        c_ph_n = ''.join(c for c in phone_num if c.isdigit())
        return c_ph_n


VIDEO_EXTENSIONS = ['.mp4', '.avi', '.mkv']
IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif']


def custom_upload_to(instance, filename):
    _, extension = os.path.splitext(filename.lower())
    if extension in VIDEO_EXTENSIONS:
        return f'videos/{timezone.now().strftime("%Y/%m/%d")}/{filename}'
    elif extension in IMAGE_EXTENSIONS:
        return f'images/{timezone.now().strftime("%Y/%m/%d")}/{filename}'
    else:
        return f'other/{timezone.now().strftime("%Y/%m/%d")}/{filename}'
