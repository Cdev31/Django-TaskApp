from .firebase import storage
from typing import BinaryIO


def load( file: BinaryIO ):
    file_save = file.read()
    response = storage.child("Tasks/" + file.name).put(file= file_save)
    url = 'https://firebasestorage.googleapis.com/v0/b/rooms-8a116.appspot.com/o/'
    return f"{url}/{response['name']}"
    
   