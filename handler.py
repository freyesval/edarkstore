import json
# from secrets import access_key, secret_access_key
import boto3
import os
from indicador import Mindicador
from pdf import PDF

client = boto3.client('s3',
        endpoint_url='http://localhost:4569',
        aws_access_key_id='S3RVER',
        aws_secret_access_key='S3RVER',
        region_name='us-west-2')

dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')





def s3local(event, context):

    try:
        uf = Mindicador('uf')
        texto = uf.InfoApi()
        pdf = PDF()
        pdf.add_page()
        pdf.logo('logo.png', 0, 0, 45, 25)
        pdf.titles('Valor de la UF del último mes')
        pdf.texts(texto)
        pdf.set_author('Fernando Reyes, Desarrollador de Software')
        pdf.output('valor_uf.pdf','F')

        for file in os.listdir():
            #print('Ingreso a los archivos ', str(file))
            if '.pdf' in file:
                print('pdf encontrado, procediendo a subir...')
                upload_file_bucket = 'local-bucket'
                upload_file_key = 'pdf/' + str(file)
                client.upload_file(file, upload_file_bucket, upload_file_key)

                print(f'Se subio correctamente {file}')
        return {"statusCode": 200, "body": 'El PDF se ha subido correctamente'}
    
    except Exception as e:
        print(e)
        return {
            "statusCode": 400, 
            "body": f'Error!!!! \n {e}'
        }


#s3local()

def dollarValue(event, context):
    try:
        usd = Mindicador('dolar')
        fecha, valor = usd.InfoApi()
        print(fecha,valor)


        table = dynamodb.Table('dollar-value')

        table.put_item(
            Item={
                'fecha': fecha,
                'valor': str(valor),
            }
        )
        print('asdf')
        print()
        print(table.creation_date_time)
        
        return {
            "statusCode": 200,
            "body": 'Se ha agregado el valor diario del dollar correctamente!!!'
        }
    except Exception as e:
        print(e)
        return {
            "statusCode": 400,
            "body": f'Error!!!! \n {e}'
        }