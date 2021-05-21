import firebase_admin
from firebase_admin import credentials

from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('helloworldfirebase-14d36-firebase-adminsdk-etrvs-7fb7dd0b7c.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
  'databaseURL': 'https://helloworldfirebase-14d36-default-rtdb.asia-southeast1.firebasedatabase.app/'
})
ref = db.reference()

users_ref = ref.child('User')
users_ref.set({  #ทัับ Data เก่าไปเลย
    'alanisawesome': {
        'date_of_birth': 'June 23, 1912',
        'full_name': 'Alan Turing'
    },
    'gracehop': {
        'date_of_birth': 'December 9, 1906',
        'full_name': 'Grace Hopper'
    }
})
posts_ref = ref.child('posts')

new_post_ref = posts_ref.push()
new_post_ref.set({  #สร้างใหม่
    'author': 'gracehop',
    'title': 'Announcing COBOL, a New Programming Language'
})

# We can also chain the two calls together
posts_ref.push().set({ #สร้างใหม่(ไม่ทับ)
    'author': 'alanisawesome',
    'title': 'The Turing Machine'
})

hopper_ref = users_ref.child('gracehop')
hopper_ref.update({ #update Data เพิ่ม
    'nickname': 'Amazing Grace'
})
hopper_ref = ref.child('posts/-M_-O5dlcOBnqg_Nhyve')    #ลบ Data
hopper_ref.delete()
print(ref.get())