import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('helloworldfirebase-14d36-firebase-adminsdk-etrvs-7fb7dd0b7c.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
  'databaseURL': 'https://helloworldfirebase-14d36-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref1 = db.reference('User')
ref2 = db.reference('User/Peam/age')


print(ref1.get())
print(ref2.get())