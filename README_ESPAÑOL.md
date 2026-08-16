# twilio-python

[![Tests](https://github.com/twilio/twilio-python/actions/workflows/test-and-deploy.yml/badge.svg)](https://github.com/twilio/twilio-python/actions/workflows/test-and-deploy.yml)
[![PyPI](https://img.shields.io/pypi/v/twilio.svg)](https://pypi.python.org/pypi/twilio)
[![PyPI](https://img.shields.io/pypi/pyversions/twilio.svg)](https://pypi.python.org/pypi/twilio)
[![Learn OSS Contribution in TwilioQuest](https://img.shields.io/static/v1?label=TwilioQuest&message=Learn%20to%20contribute%21&color=F22F46&labelColor=1f243c&style=flat-square&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAMAAAD04JH5AAAASFBMVEUAAAAZGRkcHBwjIyMoKCgAAABgYGBoaGiAgICMjIyzs7PJycnMzMzNzc3UoBfd3d3m5ubqrhfrMEDu7u739/f4vSb/3AD///9tbdyEAAAABXRSTlMAAAAAAMJrBrEAAAKoSURBVHgB7ZrRcuI6EESdyxXGYoNFvMD//+l2bSszRgyUYpFAsXOeiJGmj4NkuWx1Qeh+Ekl9DgEXOBwOx+Px5xyQhDykfgq4wG63MxxaR4ddIkg6Ul3g84vCIcjPBA5gmUMeXESrlukuoK33+33uID8TWeLAdOWsKpJYzwVMB7bOzYSGOciyUlXSn0/ABXTosJ1M1SbypZ4O4MbZuIDMU02PMbauhhHMHXbmebmALIiEbbbbbUrpF1gwE9kFfRNAJaP+FQEXCCTGyJ4ngDrjOFo3jEL5JdqjF/pueR4cCeCGgAtwmuRS6gDwaRiGvu+DMFwSBLTE3+jF8JyuV1okPZ+AC4hDFhCHyHQjdjPHUKFDlHSJkHQXMB3KpSwXNGJPcwwTdZiXlRN0gSp0zpWxNtM0beYE0nRH6QIbO7rawwXaBYz0j78gxjokDuv12gVeUuBD0MDi0OQCLvDaAho4juP1Q/jkAncXqIcCfd+7gAu4QLMACCLxpRsSuQh0igu0C9Svhi7weAGZg50L3IE3cai4IfkNZAC8dfdhsUD3CgKBVC9JE5ABAFzg4QL/taYPAAWrHdYcgfLaIgAXWJ7OV38n1LEF8tt2TH29E+QAoDoO5Ve/LtCQDmKM9kPbvCEBApK+IXzbcSJ0cIGF6e8gpcRhUDogWZ8JnaWjPXc/fNnBBUKRngiHgTUSivSzDRDgHZQOLvBQgf8rRt+VdBUUhwkU6VpJ+xcOwQUqZr+mR0kvBUgv6cB4+37hQAkXqE8PwGisGhJtN4xAHMzrsgvI7rccXqSvKh6jltGlrOHA3Xk1At3LC4QiPdX9/0ndHpGVvTjR4bZA1ypAKgVcwE5vx74ulwIugDt8e/X7JgfkucBMIAr26ndnB4UCLnDOqvteQsHlgX9N4A+c4cW3DXSPbwAAAABJRU5ErkJggg==)](https://twil.io/learn-open-source)

## Documentación

La documentación para la API Twilio puede ser encontrada [aquí][apidocs].


La documentacion para la libreria de pyhton puede ser encontrada [aquí][libdocs].

## Versiones

`twilio-python` usa una versión modificada de [Semantic Versioning](https://semver.org) para todos los cambios. [Revise este documento](VERSIONS.md) para más detalles.

### Versiones de Python con Soporte

Esta librería puede ser utilizada en las siguientes versiones de Python:

- Python 3.7
- Python 3.8
- Python 3.9
- Python 3.10
- Python 3.11

## Instalación

Instada PyPi usando [pip](https://pip.pypa.io/en/latest/), un
administrador de paquetes para Python.

```shell
pip3 install twilio
```

Si la instalación de pip falla en windows, compruebe la longitud de la ruta del directorio. Si supera los 260 caracteres, active [Long Paths](https://docs.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation) o elija una ruta más corta.

¿No tiene pip instalado? Instálelo ejecutando el siguiente comando:

```shell
curl https://bootstrap.pypa.io/get-pip.py | python
```

O puede [descargar el código fuente
(ZIP)](https://github.com/twilio/twilio-python/zipball/main 'twilio-python
source code') para `twilio-python`, y ejecutar:

```shell
python3 setup.py install
```

> **Info**
> Si la línea de comando le da un mensaje que diga "Permission Denied", intente ejecutar el comando anterior usando `sudo` (ejemplo: `sudo pip3 install twilio`).

### Compruebe la instalación

Intente mandarse un mensaje SMS. Guarde el siguiente código de prueba en un editor de texto. Asegúrese de actualizar `account_sid`, `auth_token`, y `from_` número de teléfono con los datos de su [cuenta de Twilio](https://console.twilio.com). El `to` número de teléfono será el de su teléfono móbil.

```python
from twilio.rest import Client

# Your Account SID and Auth Token from console.twilio.com
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token  = "your_auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15558675309",
    from_="+15017250604",
    body="Hello from Python!")

print(message.sid)
```

Guarde el archivo como `send_sms.py`. En la terminal, `cd` al directorio donde acaba de guardar el archivo, entonces ejecute:

```shell
python3 send_sms.py
```

Tras una breve espera, recibirá el mensaje en su teléfono.

> **Advertencia**
> Es correcto escribir en tu código directamente las credenciales cuando estas haciendo pruebas localmente, pero deberias usar variables de entorno para mantener sus credenciales en secreto antes de commitear cualquier codigo o desplegarlo a producción. Echale un ojo a  [Como establecer variables de entorno](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html) para mas informacion.

## Use la Librería de Ayuda

### Las Credenciales de la API 

El cliente `Twilio` necesita sus credenciales Twilio. Puedo o pasarlas directamentes al constructor(revise el código de abajo) o mediante variables del entorno.

Autenticación con Account SID y Auth Token:

```python
from twilio.rest import Client

account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token  = "your_auth_token"
client = Client(account_sid, auth_token)
```

Autenticación con API Key y API Secret:

```python
from twilio.rest import Client

api_key = "XXXXXXXXXXXXXXXXX"
api_secret = "YYYYYYYYYYYYYYYYYY"
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client = Client(api_key, api_secret, account_sid)
```

Alternativamente, un constructor `Client` sin estos parametros buscará las variables `TWILIO_ACCOUNT_SID` y `TWILIO_AUTH_TOKEN`  dentro del entorno actual.

Sugerimos guardar sus credenciales como variables del entorno. ¿Por qué? Nunca tendrá que preocuparse de que al subir sus credenciales, estas accidentalmente se publiquen de forma pública.

```python
from twilio.rest import Client
client = Client()
```

### Especifica la Región y/o Edge

Para sacar provecho de la [Infrastructura Global](https://www.twilio.com/docs/global-infrastructure) de Twilio, specifica la Región y/o Edge (locación en la cual el contenido es almacenado en el cache) para el cliente:

```python
from twilio.rest import Client

client = Client(region='au1', edge='sydney')
```

Un constructor `Client` sin estos parámetros buscará la `TWILIO_REGION` y `TWILIO_EDGE` que son variables dentro del entorno actual.

Alternativamente, puede especificar el edge y/o región tras la construcción del cliente Twilio:

```python
from twilio.rest import Client

client = Client()
client.region = 'au1'
client.edge = 'sydney'
```

Esto resultará en que el `hostname` se transforme del `api.twilio.com` al `api.sydney.au1.twilio.com`.

### Realice una Llamada

```python
from twilio.rest import Client

account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token  = "your_auth_token"
client = Client(account_sid, auth_token)

call = client.calls.create(to="9991231234",
                           from_="9991231234",
                           url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
print(call.sid)
```

### Consiga los Datos de una Llamada Existente

```python
from twilio.rest import Client

account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token  = "your_auth_token"
client = Client(account_sid, auth_token)

call = client.calls.get("CA42ed11f93dc08b952027ffbc406d0868")
print(call.to)
```

### Itera a Traves de Records

La libreria automaticamente se encarga de la paginación por tí. Colecciones, como `calls` y `messages`, usan los métodos `list` y `stream`. Con ambas `list` y `stream`, puede especificar el numero de records que desee recibir (`limit`) y el máximo tamaño de cada busqueda de pagina que quiera  (`page_size`). 

`list` busca rápidamente todos los records y los devuelve como una lista, mientras que `stream` devuelve un iterador y lentamente recupera páginas de records mientras itera por la colección. Tambien puede paginar manualmente usando el metodo `page`.

#### Uso del Método `list`

```python
from twilio.rest import Client

account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "your_auth_token"
client = Client(account_sid, auth_token)

for sms in client.messages.list():
  print(sms.to)
```

### Peticiones Asíncronas a la API 

Por defecto, el cliente Twilio hace peticiones síncronas a la API de Twilio. Para permitir peticiones asíncronas y no bloqueantes, hemos incluido un cliente HTTP opcional asíncrono. Cuando se usen con el cliente y los métodos de acompañamiento `*_async`, la peticiones hechas a la API Twilio seran realizadas asíncronamente.

```python
from twilio.http.async_http_client import AsyncTwilioHttpClient
from twilio.rest import Client

async def main():
    account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    auth_token  = "your_auth_token"
    http_client = AsyncTwilioHttpClient()
    client = Client(account_sid, auth_token, http_client=http_client)

    message = await client.messages.create_async(to="+12316851234", from_="+15555555555",
                                                 body="Hello there!")

asyncio.run(main())
```

### Habilitar el registro de depuración


Registre la solicitud de la API y los datos de respuesta en la consola:

```python
import logging

client = Client(account_sid, auth_token)
logging.basicConfig()
client.http_client.logger.setLevel(logging.INFO)
```

Registre la solicitud a la API y los datos de respuesta en un archivo:

```python
import logging

client = Client(account_sid, auth_token)
logging.basicConfig(filename='./log.txt')
client.http_client.logger.setLevel(logging.INFO)
```

### Manejar las Excepciones
La versión 8.x de `twilio-python` exporta una clase excepción que le ayudará a manejar las excepciones específicas a los métodos de Twilio. Para usarla, importe `TwilioRestException` y capture las siguientes excepciones:

```python
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token  = "your_auth_token"
client = Client(account_sid, auth_token)

try:
  message = client.messages.create(to="+12316851234", from_="+15555555555",
                                   body="Hello there!")
except TwilioRestException as e:
  print(e)
```

### Generar TwiML

Para controlar las llamadas de teléfono, su aplicación necesitará [TwiML][twiml].

Use `twilio.twiml.Response` para crear facilmente esas respuestas.

```python
from twilio.twiml.voice_response import VoiceResponse

r = VoiceResponse()
r.say("Welcome to twilio!")
print(str(r))
```

```xml
<?xml version="1.0" encoding="utf-8"?>
<Response><Say>Welcome to twilio!</Say></Response>
```

### Otros ejemplos avanzados

- [Learn how to create your own custom HTTP client](./advanced-examples/custom-http-client.md)

### Imagen de Docker

La `Dockerfile` presente en este repositorio y su respectiva `twilio/twilio-python` imagen de Docker están siendo usadas actualmente por Twilio solo para realizar pruebas.

### Ayuda

Si necesita alguna ayuda instalando or usando la librería, por favor visite primero [Twilio Support Help Center](https://support.twilio.com), y [archive un ticket de soporte](https://twilio.com/help/contact) si no encuentra respuesta a su problema.

Si ha encontrado algún bug en la librería o le gustaría que se añadan alguna nueva funcionalidad, adelante  abra 'issues' o 'pull requests' en este repositorio!

[apidocs]: https://www.twilio.com/docs/api
[twiml]: https://www.twilio.com/docs/api/twiml
[libdocs]: https://twilio.github.io/twilio-python
