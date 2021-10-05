import json
import requests
 
class Mindicador:
 
    def __init__(self, indicador):
        self.indicador = indicador
        #self.year = year
    
    def InfoApi(self):
        if self.indicador == 'dolar':
            # En este caso hacemos la solicitud para el caso de consulta de un indicador en un año determinado
            url = f'https://mindicador.cl/api/{self.indicador}'
            response = requests.get(url)
            data = json.loads(response.text.encode("utf-8"))
            # print(data["serie"])
            #print(data['serie'][0])
            return data['serie'][0]['fecha'][0:10], data['serie'][0]['valor']
            for dato in data["serie"]:
                print(f"El valor de {self.indicador} a la fecha ",dato["fecha"][0:10], " era de: $", str(dato["valor"]).strip())
            # Para que el json se vea ordenado, retornar pretty_json
            pretty_json = json.dumps(data, indent=2)

            return pretty_json
        elif self.indicador == 'uf':
            print('uf')
            url = f'https://mindicador.cl/api/{self.indicador}'
            response = requests.get(url)
            data = json.loads(response.text.encode("utf-8"))
            # print(data["serie"])
            #print(data['serie'][0])
            text = ''
            for dato in data['serie']:
                text += 'El valor de la uf a la fecha {} es de: ${}. \n'.format(dato['fecha'][0:10], dato['valor'])
            return text

#dolar = Mindicador('dolar')
#dolar.InfoApi()