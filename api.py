#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import json

moviles = []

try :
	fich = open("ids.txt","r")
	moviles = fich.readlines()
	fich.close()
except :
	fich = open("ids.txt","w")
	fich.close()
	moviles = []

urls = (
	'/guardarId/', 'guardarId',
)
	
app = web.application(urls, globals())

class guardarId:
	def POST(self):
		jobj = json.loads(web.data())
		existe = False
		for movil in moviles :
			if movil["id"] == jobj["id"] :
				existe = True
				break;

		aux = []
		for movil in moviles :
			if not movil["id"] == jobj["id"] :
				aux.append(movil)

		if not existe :
			aux.append({"id":jobj["id"], "frase": 0})

		fich = open("ids.txt","w")
		for movil in aux :
			linea = json.dumps(movil) + "\n"
			fich.write(linea)

		fich.close()
		

if __name__ == "__main__":
	app.run()
