#Programado por v4char
import socket
import time

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

print("Conectando")
time.sleep(6)
unirse_a_canal(canal)

while 1:
      ircmsg = irc.recv(1024)
      ircmsg = ircmsg.strip('\n\r')
    
      respuesta_ping(ircmsg,canal)
    
      if ircmsg.find("palabra clave") != -1:
            enviar_mensaje(canal, "No digas la palabra clave")
      
      if(ircmsg.find("PRIVMSG") != -1):
            nick = ircmsg.split('!', 1 )
            nick = nick[0].replace(":", "",1)
            mensaje = ircmsg.split(canal+' ', 1 )
            mensaje = mensaje[1].replace(":", "",1)
            print nick+": "+mensaje 
