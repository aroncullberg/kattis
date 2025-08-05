import socket
from typing import Tuple
import time

def connect_to_server() -> Tuple[socket.socket, int, int, int]:
    """Connect to server and get RSA parameters"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('challs.crate.nu', 2456))

    full_response = ""

    while "Hämta [f]lagga eller [s]kylt?" not in full_response:
        data = s.recv(4096).decode('utf-8')
        if not data:
            raise ConnectionError("Server closed connection")
        full_response += data

    try:
        userid_line = [line for line in full_response.split('\n') if "kund nr." in line.lower()][0]
        userid = int(userid_line.split('nr. ')[1].split('!')[0])
    except (IndexError, ValueError) as e:
        raise ValueError(f"Failed to parse userid: {e}")

    try:
        n_line = [line for line in full_response.split('\n') if line.startswith('n = ')][0]
        e_line = [line for line in full_response.split('\n') if line.startswith('e = ')][0]

        n = int(n_line.split('n = ')[1])
        e = int(e_line.split('e = ')[1])
    except (IndexError, ValueError) as e:
        raise ValueError(f"Failed to parse RSA parameters: {e}")

    print(f"Parsed parameters:")
    print(f"UserID: {userid}")
    print(f"n: {n}")
    print(f"e: {e}")

    return s, userid, n, e

def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """Extended Euclidean Algorithm"""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def exploit_signature():
    print("Connecting to server...")
    s, userid, n, e = connect_to_server()

    target_msg = f"Kund nr. {userid} får hämta flaggan"
    target_bytes = target_msg.encode('utf-8')
    target_int = int.from_bytes(target_bytes, "little")

    print(f"\nTarget message: {target_msg}")

    m1 = 2  # Start with a small number
    m2 = (target_int * pow(m1, -1, n)) % n

    msg1 = m1.to_bytes((m1.bit_length() + 7) // 8, 'little')
    msg2 = m2.to_bytes((m2.bit_length() + 7) // 8, 'little')

    print("Getting signatures for message parts...")

    s.send(b's\n')
    time.sleep(0.1)
    s.recv(4096)
    s.send(msg1 + b'\n')
    sig1 = int(s.recv(4096).decode().strip())
    print(f"Got signature 1: {sig1}")

    time.sleep(0.1)
    s.send(b's\n')
    time.sleep(0.1)
    s.recv(4096)
    s.send(msg2 + b'\n')
    sig2 = int(s.recv(4096).decode().strip())
    print(f"Got signature 2: {sig2}")

    forged_sig = (sig1 * sig2) % n
    print("\nForging final signature...")

    s.send(b'f\n')
    time.sleep(0.1)
    s.recv(4096)
    s.send(target_bytes + b'\n')
    s.send(str(forged_sig).encode() + b'\n')

    time.sleep(0.1)
    result = s.recv(4096).decode()
    print(f"\nServer response: {result}")

    s.close()

if __name__ == "__main__":
    try:
        exploit_signature()
    except Exception as e:
        print(f"Error: {e}")
