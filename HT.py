import hashlib
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


clear_screen()


# Custom function to check if a file exists in the current directory
def check_file(filename):
    if os.path.exists(filename):
        return True
    else:
        print(
            f"Error: File '{filename}' not found in the current directory. Please include it or modify the code to put yours.")
        return False


# Check if the 'common-pass.txt' file exists before proceeding
if not check_file('common-pass.txt'):
    exit()


class TextColor:
    ORANGE = '\033[38;5;208m'  # ANSI escape code for orange
    CYAN = '\033[36m'  # ANSI escape code for cyan
    YELLOW = '\033[38;5;226m'  # ANSI escape code for yellow
    PURPLE = '\033[38;5;165m'  # ANSI escape code for purple
    MINT = '\033[38;5;121m'  # ANSI escape code for mint
    RED = '\033[31m'  # ANSI escape code for red
    RED_TOMATO = '\033[38;5;202m'  # ANSI escape code for Tomato Red
    RED_BG = "\x1b[41m"
    BLUE = "\u001b[34m"
    RESET = '\033[0m'


def colored_text(text, color):
    return color + text + TextColor.RESET


def display_known_algorithms():
    print("Known Hash Algorithms:")
    known_algorithms = {
        "md5": "MD5 (Message-Digest Algorithm 5)",
        "sha1": "SHA-1 (Secure Hash Algorithm 1)",
        "sha256": "SHA-256 (Secure Hash Algorithm 256-bit)",
        "sha512": "SHA-512 (Secure Hash Algorithm 512-bit)",
        "sha3_256": "SHA-3 (Secure Hash Algorithm 3)",
        "blake2b": "BLAKE2 (a cryptographic hash function)",
        "whirlpool": "Whirlpool",
        "ripemd160": "RIPEMD-160 (RACE Integrity Primitives Evaluation Message Digest 160)",
        "tiger": "Tiger",
        "crc32": "CRC32 (Cyclic Redundancy Check 32-bit)",
        "adler32": "Adler-32",
        "murmurhash": "MurmurHash",
        "fnv1": "FNV-1 (Fowler-Noll-Vo hash function 1)",
        "cityhash": "CityHash",
        "xxhash": "xxHash",
        "siphash": "SipHash",
        "jenkins": "Jenkins Hash",
        "farmhash": "FarmHash",
        "poly1305": "Poly1305 (a MAC and cryptographic hash function)",
        "gost34_11": "GOST R 34.11-94 (Russian cryptographic hash function)"
    }

    for algorithm, description in known_algorithms.items():
        print(f"{colored_text(algorithm, TextColor.CYAN)}: {description}")

    print("\n")


def find_password(hash_to_find, password_list, hash_function):
    for password in password_list:
        hashed_password = hash_function(password.encode()).hexdigest()
        if hashed_password == hash_to_find:
            return password
    return None


def create_hash(password, hash_function):
    hashed_password = hash_function(password.encode()).hexdigest()
    return hashed_password


def detect_hash_algorithm(hash_value):
    for algorithm in hashlib.algorithms_guaranteed:
        try:
            hash_function = getattr(hashlib, algorithm)
            hash_function()
            if len(hash_value) == hash_function().digest_size * 2:
                return algorithm
        except (AttributeError, ValueError):
            pass
    return None


def translate_hash(hash_value, target_algorithm):
    source_algorithm = detect_hash_algorithm(hash_value)
    if source_algorithm:
        try:
            source_hash_function = getattr(hashlib, source_algorithm)
            target_hash_function = getattr(hashlib, target_algorithm)
            decoded_hash = bytes.fromhex(hash_value)
            hashed_password = target_hash_function(decoded_hash).hexdigest()
            return hashed_password
        except AttributeError:
            pass
    return None


while True:
    print(colored_text("HashTweaks", TextColor.RED_BG))
    print(colored_text("1: Find an existing password (HASH2PASS)", TextColor.ORANGE))
    print(colored_text("2: Create a password hash (PASS2HASH)", TextColor.CYAN))
    print(colored_text("3: Detect hash algorithm", TextColor.YELLOW))
    print(colored_text("4: Translate hash to another algorithm", TextColor.MINT))
    print(colored_text("5: View known hash algorithms", TextColor.RED))
    print(colored_text("6: File Hashing", TextColor.BLUE))
    print(colored_text("7: Compare two Hash", TextColor.BLUE))
    print(colored_text("8: Exit", TextColor.YELLOW))

    choice = input(colored_text("Please select an option (1, 2, 3, 4, 5, or 6): ", TextColor.RED_TOMATO))

    if choice == '1':
        with open('common-pass.txt', 'r') as file:
            password_list = [line.strip() for line in file]

        hash_algorithm = input("Select a hash algorithm (md5, sha256, sha3_256): ")
        if hash_algorithm in hashlib.algorithms_available:
            hash_function = getattr(hashlib, hash_algorithm)
            hash_to_find = input("Please enter a hash to find the corresponding password: ")
            found_password = find_password(hash_to_find, password_list, hash_function)

            if found_password:
                print(colored_text(f"Original Password: {found_password}", TextColor.ORANGE))
            else:
                print("Password not found for the given hash.")
        else:
            print("Invalid hash algorithm.")

        input("Press Enter to continue...")
        clear_screen()

    elif choice == '2':
        hash_algorithm = input("Select a hash algorithm (md5, sha256, sha3_256): ")
        if hash_algorithm in hashlib.algorithms_available:
            hash_function = getattr(hashlib, hash_algorithm)
            new_password = input("Please enter a password to create a hash: ")
            hashed_password = create_hash(new_password, hash_function)
            print(colored_text(f"Hashed Password: {hashed_password}", TextColor.CYAN))
        else:
            print("Invalid hash algorithm.")

        input("Press Enter to continue...")
        clear_screen()

    elif choice == '3':
        hash_value = input("Please enter a hash value: ")
        detected_algorithm = detect_hash_algorithm(hash_value)
        if detected_algorithm:
            print(colored_text(f"The detected hash algorithm is: {detected_algorithm}", TextColor.YELLOW))
        else:
            print("Could not detect a supported hash algorithm.")

        input("Press Enter to continue...")
        clear_screen()

    elif choice == '4':
        source_hash_value = input("Please enter the source hash value: ")
        target_algorithm = input("Select a target hash algorithm (md5, sha256, sha3_256): ")
        if target_algorithm in hashlib.algorithms_available:
            translated_hash = translate_hash(source_hash_value, target_algorithm)
            if translated_hash:
                print(f"Translated Hash: {translated_hash}")
            else:
                print("Translation failed.")
        else:
            print("Invalid target hash algorithm.")

        input("Press Enter to continue...")
        clear_screen()

    elif choice == '5':
        display_known_algorithms()
        input("Press Enter to continue...")
        clear_screen()

    elif choice == '6':  # New option for getting hash from a file
        file_path = input("Enter the path of the file to calculate hash: ")
        hash_algorithm = input("Select a hash algorithm (md5, sha256, sha3_256): ")

        if hash_algorithm in hashlib.algorithms_available:
            hash_function = getattr(hashlib, hash_algorithm)
            try:
                with open(file_path, 'rb') as file:
                    file_contents = file.read()
                    file_hash = hash_function(file_contents).hexdigest()
                    print(colored_text(f"Hash of '{file_path}': {file_hash}", TextColor.MINT))
            except FileNotFoundError:
                print("File not found.")
        else:
            print("Invalid hash algorithm.")

        input("Press Enter to continue...")
        clear_screen()


    elif choice == '7':  # New option for comparing two hashes
        hash1 = input("Enter the first hash: ")
        hash2 = input("Enter the second hash: ")

        if hash1 == hash2:
            print("The hashes are equal.")
        else:
            print("The hashes are not equal.")

        input("Press Enter to continue...")
        clear_screen()


    elif choice == '8':
        break

    else:
        print("Invalid choice. Please select 1, 2, 3, 4, 5, 6, 7 or 8.")
        input("Press Enter to continue...")
        clear_screen()
