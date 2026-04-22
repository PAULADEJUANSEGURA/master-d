from abc import ABC, abstractmethod
import json
import csv

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"nombre='{self.name}', email='{self.email}'"
    

class UserReader(ABC):
        
    @abstractmethod
    def read_users(self, file_path):
        pass

class JSONUserReader(UserReader):
    def read_users(self, file_path):
        with open(file_path, encoding='utf-8') as file:
            data = json.load(file)
            return [User(u['name'], u['email']) for u in data]
        
class CSVUserReader(UserReader):
    def read_users(self, file_path):
        users = []
        with open(file_path, encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                users.append(User(row['name'], row['email']))
        return users    
    
def load_users(reader, file_path):
    return reader.read_users(file_path)

def get_reader(file_path):
    ext = file_path.split('.')[-1].lower()
    if ext == 'json':
        return JSONUserReader()
    elif ext == 'csv':
        return CSVUserReader()
    else:
        raise ValueError("Unsupported file format")
    
file_path = input("¿Qué archivo quieres cargar? (ej: users.csv): ")
print("Cargando usuarios...")

try:
    reader = get_reader(file_path)
    users = load_users(reader, file_path)
    for user in users:
        print(user)
except Exception as e:
    print(f"Error: {e}")