from .models import Guest

class GuestDAO:
  def addUser(new_id, data):
    new_guest = Guest(userid=new_id, name=data['name'], password=data['password'], email=data['email'], phone_number=data['phone'], profile_image=data['profile'])
    new_guest.save()
    