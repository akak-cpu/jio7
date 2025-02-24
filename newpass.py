from django.contrib.auth.models import User
user=User.object.get(username="jio")
user.set_password("jio")
user.save()