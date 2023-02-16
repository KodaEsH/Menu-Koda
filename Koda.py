import socket
import time
import os


def you():
    print("""Menu:

    [+] - GETIP
    [+] - REDE
    [+] - GITHUB

          
          """)
    chamada = input("Digite o nome do comando :   ")
    os.mkdir("KodaEsh ")
    if chamada == "GETIP":
        getip()
    if chamada == "REDE":
        rede()
    if chamada == "GITHUB":
        print("KodaEsh :D")
    os.rmdir("KodaEsh ")



def getip():
    ip = " "
    try:
        in_put = input("Get you http link :  ")
        get = socket.gethostbyname(in_put)
        print(f"Host ip is : {get}")
        ip = get
    except KeyboardInterrupt:
        print("KeyboardInterrupt = true")



def rede():
    target = input("Input host :    ") # HOST TARGET

    for port in range(0, 65535):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conexão = client.connect_ex((target, port))
        if conexão == 0:
            print(f"Port = {port} : Target = {target}")


if __name__ == "__main__":
    you()