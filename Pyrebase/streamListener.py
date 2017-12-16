import pyrebase

def stream_handler(message):
    print(message["event"])
    print(message["path"])
    print(message["data"])

config = {
        "apiKey": "apiKey",
        "authDomain": "tmanager-175920.firebaseapp.com",
        "databaseURL": "https://tmanager-175920.firebaseio.com",
        "storageBucket": "projectId.appspot.com",
        "serviceAccount": "TManager-84bc0c2ff7da.json"
        }
firebase = pyrebase.initialize_app(config)

# grab username and passworfd
pwdFile = open(".password","r")
pwdLines = pwdFile.readlines()
email = pwdLines[0].strip()
pw = pwdLines[1].strip()
pwdFile.close()

auth = firebase.auth()
#authenticate a user
user = auth.sign_in_with_email_and_password(email,pw)

# open database
db = firebase.database()
my_stream = db.child("downloads").stream(stream_handler,user['idToken'],stream_id="new_posts")

