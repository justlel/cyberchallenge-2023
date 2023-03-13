import hashlib
import string


def get_hashes():
    with open('ct.txt', 'r') as f:
        return [l.strip() for l in f.readlines()]


def bruteforce_hash():
    final = ""
    for hash_calculate in get_hashes():
        char_append = ""
        for char in string.ascii_letters + string.digits + string.punctuation:
            for mode in ['sha256', 'sha512', 'md5']:
                hash_function = hashlib.new(mode)
                hash_function.update(char.encode())
                if hash_function.hexdigest() == hash_calculate:
                    char_append += char
                    break
            if char_append != "":
                final += char_append
                break
    return final


if __name__ == '__main__':
    print(get_hashes())
    print(bruteforce_hash())
