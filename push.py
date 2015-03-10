#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import servKey as servKey
import requests
import httplib

url = "https://android.googleapis.com/gcm/send"
header = {"Authorization": str("key=" + servKey.autho), 
	"Content-Type" : "application/json", 
	"Accept-Encoding" : "application/json" }

fich = open("ids.txt","r")
moviles = fich.readlines()
fich.close()

fich = open("frases.txt","r")
frases = fich.readlines()
fich.close()

for movil in moviles :
	data = { 
		"registration_ids" : str(movil["id"]),
		"data" : {
			"mensaje" : {
				"tipo" : str("frase"),
				"mensaje" : str(frases[int(movil["frase"])])
			}
		}
	}
	movil["frase"] = (int(movil["frase"]) + 1) % len(frases)
	r = requests.post(url, json.dumps(data), header)

fich = open ("ids.txt","w")
for movil in moviles :
	linea = json.dumps(movil) + "\n"
	fich.write(linea)

fich.close()
