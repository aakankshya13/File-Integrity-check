import hashlib
import os

def get_file_hash(filename):
    hasher = hashlib.sha256()
    with open(filename, 'rb') as file:
        content = file.read()
        hasher.update(content)
    return hasher.hexdigest()

file_name = 'adsh.txt'  # Change this to your file
hash_file = 'saved_hash.txt'  # This will store the original hash

# Check if hash file exists
if not os.path.exists(hash_file):
    # First time: calculate and save the hash
    hash_value = get_file_hash(file_name)
    with open(hash_file, 'w') as f:
        f.write(hash_value)
    print(f"Hash saved. File is considered safe.")
else:
    # Later runs: compare with saved hash
    current_hash = get_file_hash(file_name)
    
    with open(hash_file, 'r') as f:
        saved_hash = f.read()
    
    if current_hash == saved_hash:
        print("File is SAFE. No changes detected.")
    else:
        print("File is TAMPERED! Hash does not match.")
