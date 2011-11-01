# -*- coding:utf-8 -*-
"""
Script para geolocalizar endereços
requer o modulo geopy para funcionar:
easy_install geopy
"""
from geopy import geocoders

def carrega_csv(filename)
	"""
	Abre Arquivo csv com endereços para geo-referenciamento
	primeira linha deve ser cabeçalho com nomes de variaveis
	"""
	with open(filename,'r') as f:
		ends = f.readlines()
	return ends
	

def georeferencia(enderecos,arqsaida,campo,geoserv='google'):
	
	if geoserv == 'google':
		# Usando o Google
		g = geocoders.Google('ABQIAAAA_gnHK6RUKt_B9h1XlCw2fRRSj27_XPuJ4H5ID33wYOhGVNZE9hSv8VlUSRnLRlA9aUnXiquLb89oJw')
	elif geoserv == 'geonames':
		#Usando o geonames que não requer API Key
		gn = geocoders.GeoNames()
	j=1
	varnames = enderecos.pop(0)
	try:
		for i,e in enumerate(enderecos):
			if i == 0:
				fs.write('lat,lng,ATIVIDADE,DDD,T1,NOME,CNPJ,LOGR,NR,COMPL ,CEP,BAIRRO ,CIDADE  ,UF,RA,GRUPO,QTD_FUNC\n')
				continue
			# lat lng perto do RJ ---> agua!
			lat = -23.40
			lng = -43.10
			l = e.split(',')
			#por endereco
			query_string = '%s, %s, %s, rio de janeiro, RJ, Brazil'%(l[5], l[6], l[9])
			#por CEP
			#query_string = 'rio de janeiro, RJ, %s, Brazil'%(l[8][:5]+'-'+l[8][5:])
			#print query_string#place, lat, lng
			try:
				place, (lat, lng) = g.geocode(query_string)
				print i#place, lat, lng
			except:
				print '==> Não encontrei no Google: %s'%query_string, j
				j += 1
			l = [str(lat),str(lng)]+l
			fs.write(','.join(l))
	finally:
		fs.close()
if __name__=="__main__":
	fs = open('NovaAmostra-loc-endereco.csv','w')
	ends = carrega_csv('Dados nova amostra.csv')

