#Programado por v4char

import socket
import time

servidor = "servidor_irc"
canal = "#canal"
nombre = "nombre_del_bot"
puerto = 6667

def respuesta_ping(ircmsg, canal):
      if ircmsg.find("PING :") != -1:
            respuesta_ping = ircmsg
            respuesta_ping = respuesta_ping[respuesta_ping.find("PING :"):]
            respuesta_ping = respuesta_ping.split("\n", 1 )
            respuesta_ping = respuesta_ping[0].replace("I", "O", 1)
            irc.send(respuesta_ping)
            unirse_a_canal(canal)
            print respuesta_ping
            print "\n\r"
        
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
time.sleep(4)
unirse_a_canal(canal)

while 1:
      ircmsg = irc.recv(512)
      
      if ((ircmsg.find("PRIVMSG") != -1) != 1):
            respuesta_ping(ircmsg,canal)
            
      ircmsg = ircmsg.strip('\n\r')
      
      if ircmsg.find("PRIVMSG "+canal) != -1:
            mostrar_chat(ircmsg, canal)
      
      if ircmsg.find("palabra clave") != -1:
            enviar_mensaje(canal, "No digas la palabra clave")
