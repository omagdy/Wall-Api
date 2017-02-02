from django.test import TestCase, Client
import requests

class WallTests(TestCase):

   #No longer usable as the user must verify the account when registering through a link sent by Email.
   def test_signup()self:
      data = {'username':'Omaru', 'password1':'meazyday', 'password2':'meazyday', 'email':'omagdy@gm.com'}
      c = Client() 
      response = c.post('/rest-auth/registration/',params=data)
      self.assertEqual(response.status_code, 200)


   def test_login(self):
      data = {'username':'Omar', 'email':'omagdy.222@gmail.com', 'password':'meazyday'}
      c = Client() 
      response = c.post('/rest-auth/login/',params=data)
      self.assertEqual(response.status_code, 200)


   def test_logout(self):
      c = Client() 
      response = c.post('/rest-auth/logout/')
      self.assertEqual(response.status_code, 200)

   def test_wall(self):

      c = Client() 
      response = c.get('/wall')
      self.assertEqual(response.status_code, 200)

   def test_postwall(self):

      c = Client()
      c.login(username='Omar', password='meazyday')
      data={'text':'A5eraaan!'}
      response = c.post('/wall',param=data)
      self.assertEqual(response.status_code, 200)







