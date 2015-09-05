#Programado por v4char

import socket  
      
servidor = "servidor irc" 
canal = "#canal"
nombre = "v4charbot"
puerto = 6667

def respuesta_ping(ircmsg,canal):
    if ircmsg.find("PING :") != -1:
        respuesta_ping = ircmsg
        respuesta_ping = respuesta_ping.replace("I", "O")
        respuesta_ping = respuesta_ping+"\n\r"
        irc.send(respuesta_ping)
        unirse_a_canal(canal)
        

def enviar_mensaje(canal , msg):
    irc.send("PRIVMSG "+ canal +" :"+ msg +"\n\r") 

def unirse_a_canal(canal):
    irc.send("JOIN "+ canal +"\n\r")
        
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((servidor, puerto))
irc.send("USER "+ nombre +" "+ nombre +" "+ nombre +" :Bot by v4char\n\r")
irc.send("NICK "+ nombre +"\n\r")



while 1:
    ircmsg = irc.recv(1024)
    ircmsg = ircmsg.strip('\n\r')
    print(ircmsg)
    
    respuesta_ping(ircmsg,canal)
    
    if ircmsg.find("palabra clave") != -1:
        enviar_mensaje(canal, "No digas la palabra clave")
 
  
  
    
