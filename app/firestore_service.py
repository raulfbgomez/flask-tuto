import firebase_admin
from firebase_admin import credentials
from firebase_admin import  firestore

# if (not len(firebase_admin._apps)):
#   credential = credentials.ApplicationDefault()
#   firebase_admin.initialize_app(credential)
  # firebase_admin.initialize_app(cred, {
  #     'projectId': '',
  #   })

# db = firestore.client()

# Use the application default credentials
if (not len(firebase_admin._apps)):
  cred = credentials.ApplicationDefault()
  firebase_admin.initialize_app(cred)

db = firestore.client()


# Metodos
def get_users():
  return db.collection('users').get()

def get_todos(user_id):
  return db.collection('users').document(user_id).collection('todos').get()