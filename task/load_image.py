from .firebase import storage
from typing import BinaryIO
import datetime
import pyrebase

def load( file: BinaryIO ):
    file_save = file.read()
    file_name = f'{datetime.datetime.now().timestamp()}.{file.name.split(".")[-1]}' 
    try:
        response = storage.child("Tasks/" + file_name).put(file= file_save)
        url = storage.get_url( response['downloadTokens'] )
        print(url)
        return url
    except Exception as error:
        return error
    
   