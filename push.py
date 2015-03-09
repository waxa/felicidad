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

aux = []
for movil in moviles :
	aux.append(str(movil["id"]))


# TODO completar datos a mandar
data = { 
	"registration_ids" : aux,
	"data" : {
		"mensaje" : {
			"tipo" : str("XXXXX"),
			"mensaje" : str("XXXXX")
		}
	}
}

r = requests.post(url, json.dumps(data), header)
