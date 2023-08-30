from django.db import models

# Create your models here.

# state choices
STATE_CHOICES =(
    ('1', 'Uttar Pradesh'),
    ('2', 'Madhya Pradesh'),
    ('3', 'Maharashtra'),
    ('4', 'Rajasthan'),
    ('5', 'Bihar'),
    ('6', 'West Bengal'),
    ('7', 'Andhra Pradesh'),
    ('8', 'Tamil Nadu'),
    ('9', 'Karnataka'),
    ('10', 'Gujarat'),
    ('11', 'Odisha'),
    ('12', 'Telangana'),
    ('13', 'Kerala'),
    ('14', 'Jharkhand'),
    ('15', 'Assam'),
    ('16', 'Punjab'),
    ('17', 'Chhattisgarh'),
    ('18', 'Haryana'),
    ('19', 'Uttarakhand'),
    ('20', 'Himachal Pradesh'),
    ('21', 'Tripura'),
    ('22', 'Meghalaya'),
    ('23', 'Manipur'),
    ('24', 'Nagaland'),
    ('25', 'Goa'),
    ('26', 'Arunachal Pradesh'),
    ('27', 'Mizoram'),
    ('28', 'Sikkim')
)

def get_state_name(state_id):
    for state in STATE_CHOICES:
        if state[0] == state_id:
            return state[1]
    return None

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=10, choices = STATE_CHOICES, default='1')
    gender = models.CharField(max_length=1, choices = GENDER_CHOICES, default='M')