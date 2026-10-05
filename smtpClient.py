from socket import *

def smtp_client():
    # Define mailserver and port appropriately inside your function
    mailserver = "localhost"
    port = 1025
    
    # Create socket and establish connection safely inside the function block
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    
    # Receive the greeting message from the server
    recv = clientSocket.recv(1024).decode()
    print(recv)
    if not recv.startswith('220'):
        print('220 reply not received from server.')

    # Send HELO command and print server response
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
    if not recv1.startswith('250'):
        print('250 reply not received from server.')
        
    # Close connection cleanly
    clientSocket.close()

if __name__ == "__main__":
    smtp_client()
