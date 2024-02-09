from .firebase import storage
from typing import BinaryIO


def load( file: BinaryIO ):
    file_save = file.read()
    return storage.child("Tasks/" + file.name).put(file= file_save)
    
    
   