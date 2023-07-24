import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import json
import uuid

KEY_JSON_PATH = 'test-cpp-to-firebase-firebase-adminsdk-ruihs-39fe4e9ccc.json'
ADD_JSON_PATH = './add.json'

COLLECTION_NAME = "test_collection"

def configure_firebase():
    try:
        #認証情報を取得する
        cred = credentials.Certificate(KEY_JSON_PATH)
        app = firebase_admin.initialize_app(cred)
        db = firestore.client()
        return db 
    except Exception as e:
        print(e)
        return None
    
def load_json():
    try:
        with open('./add.json') as f:
            loaded_json = json.load(f)
        return loaded_json
    except Exception as e:
        print(e)
        return None
    
def add_firestore(db,json_to_add):
    try:
        document_name = str(uuid.uuid1())
        db.collection(COLLECTION_NAME).document(document_name).set(json_to_add)
    except Exception as e:
        print(e)
        exit(1)


def main():
    #fierebase情報の認証
    db = configure_firebase()
    if db ==None:
        return
    
    loaded_json = load_json()
    if loaded_json ==None:
        return
    
    add_firestore(db,loaded_json)

if __name__=="__main__":
    main()