#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import servKey as servKey
import requests
import httplib

url = "https://android.googleapis.com/gcm/send"
header = {"Authorization": "key=" + servKey.autho, "Content-Type" : "application/json", "Accept-Encoding" : "application/json" }

fich = open("/home/waxa/felicidad/ids.txt","r")
moviles = fich.readlines()
fich.close()

fich = open("/home/waxa/felicidad/frases.txt","r")
frases = fich.readlines()
fich.close()

aux = []
for movil in moviles :
	jobj = json.loads(movil)
	idMovil = []
	idMovil.append(str(jobj["id"]))
	data = { 
		"registration_ids" : idMovil,
		"data" : {
			"mensaje" : {
				"frase" : str(frases[int(jobj["frase"])])
			}
		}
	}
	print"frase : " + str(frases[int(jobj["frase"])])
	jobj["frase"] = (int(jobj["frase"]) + 1) % len(frases)
	r = requests.post(url, data = json.dumps(data), headers = header)
	print "-------------------------------"
	print "peticion enviada"
	print r.text
	print "-------------------------------"
	aux.append(jobj)

fich = open ("/home/waxa/felicidad/ids.txt","w")
for movil in aux :
	linea = json.dumps(movil) + "\n"
	fich.write(linea)

fich.close()

fich = open("/var/mail/waxa","w")
fich.write("")
fich.close()
