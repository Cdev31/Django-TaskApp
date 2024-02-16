from .firebase import storage
from typing import BinaryIO
import datetime


def load( file: BinaryIO ):
    file_save = file.read()
    file_name = f'{datetime.datetime.now().timestamp()}.{file.name.split(".")[-1]}' 
    response = storage.child("Tasks/" + file_name).put(file=file_save)
    name = response['name'].split("/")[1]
    url = f'https://firebasestorage.googleapis.com/v0/b/{response["bucket"]}/o/Tasks%2F{name}?alt=media&token={response["downloadTokens"]}'
    return url
    
    
def delete( file_name: str ):
    try:
        storage.delete(file_name)
        return True
    except Exception as error:
        print(error)
        return False