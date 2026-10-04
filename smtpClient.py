from socket import *




msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
mailserver = '127.0.0.1'
port = 1025

# Create socket called clientSocket and establish a TCP connection with mailserver and port
# Fill in start
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((mailserver, port))
# Fill in end

recv = clientSocket.recv(1024).decode()
#print(recv) #You can use these print statement to validate return codes from the server.
#if recv[:3] != '220':
#    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
#print(recv1)
#if recv1[:3] != '250':
#    print('250 reply not received from server.')

# Send MAIL FROM command and handle server response.
# Fill in start
mailFromCommand = 'MAIL FROM:<alice@example.com>\r\n'
clientSocket.send(mailFromCommand.encode())
recv2 = clientSocket.recv(1024).decode()
# Fill in end

# Send RCPT TO command and handle server response.
# Fill in start
rcptToCommand = 'RCPT TO:<bob@example.com>\r\n'
clientSocket.send(rcptToCommand.encode())
recv3 = clientSocket.recv(1024).decode()
# Fill in end

# Send DATA command and handle server response.
# Fill in start
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024).decode()
# Fill in end

# Send message data.
# Fill in start
clientSocket.send(msg.encode())
# Fill in end

# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024).decode()
# Fill in end

# Send QUIT command and get server response.
# Fill in start
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recv6 = clientSocket.recv(1024).decode()
# Fill in end
