# branch1
import hashlib

def hash_password(password):

    hash_object = hashlib.sha256(password.encode())
    hashed_password = hash_object.hexdigest()
    return hashed_password

def check_password(file_path, hashed_password_to_check):
    with open(file_path, 'r') as file:
        stored_hashed_password = file.read().strip()

    if hashed_password_to_check == stored_hashed_password:
        print("A senha está correta.")
    else:
        print("A senha está incorreta.")

if __name__ == "__main__":
    with open('senha.txt', 'r') as file:
        password = file.read().strip()

    hashed_password = hash_password(password)

    print(f"A senha é: {password}")

    check_password('hashed_password.txt', hashed_password)
