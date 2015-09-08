#Programado por v4char
import socket
import time

servidor = "servidor irc"
canal = "#canal"
nombre = "v4charbot"
puerto = 6667

def entre(texto, inicio, final):
      pos_a = texto.find(inicio)
      if pos_a == -1: return ""
      pos_b = texto.rfind(final,1)
      if pos_b == -1: return ""
      pos_a = pos_a + len(inicio)
      if pos_a >= pos_b: return ""
      return texto[pos_a:pos_b]

def respuesta_ping(ircmsg, canal):
      if ircmsg.find("PING :") != -1:
            respuesta_ping = ircmsg
            respuesta_ping = entre(respuesta_ping, "PING :","\r\n:")
            respuesta_ping = "PONG :"+respuesta_ping+"\r\n"
            irc.send(respuesta_ping)
            unirse_a_canal(canal)
        
def enviar_mensaje(canal , msg):
      irc.send("PRIVMSG "+ canal +" :"+ msg +"\n\r") 
    
def unirse_a_canal(canal):
      irc.send("JOIN "+ canal +"\n\r")

def  obtener_nick(canal, ircmsg):
      if ircmsg.find("PRIVMSG "+canal) != -1:
            nick = ircmsg.split('!', 1 )
            nick = nick[0].replace(":", "",1)
            return nick

def obtener_mensaje(canal, ircmsg):
      if ircmsg.find("PRIVMSG "+canal) != -1:
            mensaje = ircmsg.split(canal+' ', 1 )
            mensaje = mensaje[1].replace(":", "",1)
            return mensaje

def mostrar_chat(ircmsg, canal):
      print (obtener_nick(canal, ircmsg)+": "+obtener_mensaje(canal, ircmsg))

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((servidor, puerto))
irc.send("USER "+ nombre +" "+ nombre +" "+ nombre +" :Bot by v4char\n\r")
irc.send("NICK "+ nombre +"\n\r")

print("Conectando... Se paciente.")
unirse_a_canal(canal)
time.sleep(6)
unirse_a_canal(canal)

while 1:
      ircmsg = irc.recv(512)
      ircmsg = ircmsg.strip('\n\r')
      
      if ircmsg.find("PRIVMSG "+canal) != -1:
            mostrar_chat(ircmsg, canal)
            
      respuesta_ping(ircmsg,canal)
      
      if ircmsg.find("palabra clave") != -1:
            enviar_mensaje(canal, "No digas la palabra clave")
