import socket
import rsa_maker
import os
import threading

SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
BUFFER = 4096

def main():
    clearPrompt()
    t = int(input('Give the size of the RSA communication module ?: '))
    RSAmodule = rsa_maker.makeModule(t)
    N = RSAmodule[0]
    e = RSAmodule[1]
    d = RSAmodule[2]
    clearPrompt()
    nickname = input('Give the Nickname to use: ')

    print('1: Wait to someone else connection')
    print('2: Connect to someone else')
    response = int(input('rp: '))
    clearPrompt()

    if response == 1:
        SOCKET.bind(("0.0.0.0", 6666))
        SOCKET.listen()

        #waiting for the client connection 
        response = None
        while response != 'y':
            clearPrompt()
            print('Waiting for new connection...')
            client, address = SOCKET.accept()
            clearPrompt()
            print('Connection receive from '+str(address)+', do you want to accept ?')
            response = input('(y/n): ')
        clearPrompt()

        #sending the public key to start communication
        print('Sending public key to client...')
        PublicKey = str(N)+";"+str(e)
        client.send(PublicKey.encode())
        clearPrompt()

        #getting the client public key
        print('Getting the client public key...')
        ClientPublicKey = client.recv(BUFFER).decode().split(';')
        Client_N = int(ClientPublicKey[0])
        Client_e = int(ClientPublicKey[1])
        clearPrompt()

        #the secure chat can now start with crypted message

        #sending server nickname
        print('Sending the server nickname...')
        client.send(rsa_maker.encrypt(nickname,Client_N,Client_e).encode())
        #getting the client nickname
        print('Getting the client nickname...')
        ClientNick = rsa_maker.decrypt(client.recv(BUFFER).decode(),N,d)
        clearPrompt()

        print("Communication start with " + ClientNick)

        recvThread = threading.Thread(target=recvMessage,args=(ClientNick,client,N,d,Client_N,Client_e,))
        recvThread.start()
        sendMessage(client,Client_N,Client_e,N,d)
        
    elif response == 2:
        host = input('Give the connection HOST: ')
        port = int(input('Give the connection PORT: '))
        SOCKET.connect((host, port))
        clearPrompt()

        #getting the server public key to start communication
        print('Getting the server public key...')
        ServerPublicKey = SOCKET.recv(BUFFER).decode().split(';')
        Server_N = int(ServerPublicKey[0])
        Server_e = int(ServerPublicKey[1])
        clearPrompt()

        #sending the client public key to the server
        print('Sending public key to server...')
        PublicKey = str(N)+";"+str(e)
        SOCKET.send(PublicKey.encode())
        clearPrompt()

        #the secure chat can now start with crypted message

        #getting the server nickname
        print('Getting the server nickname...')
        ServerNick = rsa_maker.decrypt(SOCKET.recv(BUFFER).decode(),N,d)
        #sending client nickname
        print('Sending nickname to server...')
        SOCKET.send(rsa_maker.encrypt(nickname,Server_N,Server_e).encode())
        clearPrompt()

        print("Communication start with " + ServerNick)

        recvThread = threading.Thread(target=recvMessage,args=(ServerNick,SOCKET,N,d,Server_N,Server_e,))
        recvThread.start()
        sendMessage(SOCKET,Server_N,Server_e,N,d)

def recvMessage(servNick,servM,NDecrypt,dDecrypt,NUnsign,eUnsign):
    while True:
        try:
            fullTrame = servM.recv(BUFFER).decode()
            fullTrame = fullTrame.split(";;;")
            DecryptedSign = rsa_maker.decrypt(fullTrame[1],NUnsign,eUnsign)
            if DecryptedSign == fullTrame[0]:
                decryptedMessage = rsa_maker.decrypt(fullTrame[0],NDecrypt,dDecrypt)
                print("#> " +servNick+ ": " +decryptedMessage)
            else:
                print('Unsigned message from wrong origin')
        except Exception:
            print('Error in message reception !')
            break

def sendMessage(ClientM,NEncrypt,eEncrypt,NSign,dSign):
    while True:
        try:
            msgToSend = input('')
            EncryptedMsg = rsa_maker.encrypt(msgToSend,NEncrypt,eEncrypt)
            signature = rsa_maker.encrypt(EncryptedMsg,NSign,dSign)
            trame = EncryptedMsg+";;;"+signature
            ClientM.send(trame.encode())
        except Exception:
            print('Error when sending a message !')
            break

def clearPrompt():
    os.system('cls' if os.name == 'nt' else 'clear')

def loadAnim(prompt):
    state = [" \ ", " - ", " / ", " | "]
    x = 0
    while True:
        global stop_anim
        clearPrompt()
        if stop_anim:
            break
        print(prompt + state[x])
        x+=1

if __name__ == '__main__':
    main()

exit()