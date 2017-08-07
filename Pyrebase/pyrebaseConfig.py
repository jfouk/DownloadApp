import pyrebase
config = {
        "apiKey": "AIzaSyBcrsiPbLP5KNpRcZpvVk2DEVjmhDvmhG4",
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
movie = {"name":"Star Wars 2", "link":"thelink2"}
db.child("downloads").child("next").update(movie, user['idToken'])
