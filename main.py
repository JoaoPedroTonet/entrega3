import hashlib

def hash_password(password):
    hash_object = hashlib.sha256(password.encode())
    hashed_password = hash_object.hexdigest()
    return hashed_password

def save_to_file(data, filename):
    with open(filename, 'w') as file:
        file.write(data)

if __name__ == "__main__":
    with open('senha.txt', 'r') as file:
        password = file.read().strip()

    hashed_password = hash_password(password)

    save_to_file(hashed_password, 'hashed_password.txt')
