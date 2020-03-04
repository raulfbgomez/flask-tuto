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
  firebase_admin.initialize_app(cred, {
    'projectId': 'flask-tuto-269406'
  })

db = firestore.client()


# Metodos
def get_users():
  return db.collection('users').get()

def get_user(user_id):
  return db.collection('users').document(user_id).get()

def get_todos(user_id):
  return db.collection('users').document(user_id).collection('todos').get()

def user_put(user_data):
  user_ref = db.collection('users').document(user_data.username)
  user_ref.set({ 'password': user_data.password })