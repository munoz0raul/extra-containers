from flask import Flask
from flask_mqtt import Mqtt

app = Flask(__name__)

app.config['SECRET'] = 'my secret key'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MQTT_BROKER_URL'] = 'host.docker.internal'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_USERNAME'] = ''
app.config['MQTT_PASSWORD'] = ''
app.config['MQTT_KEEPALIVE'] = 5
app.config['MQTT_TLS_ENABLED'] = False

access = 0

mqtt = Mqtt(app)

@app.route('/')
def hello_world():
  global access
  return ('Numbem of Access on shellhttpd Container ' + str(access))

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('containers/requests')

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
  if message.payload.decode().startswith('ACCESS='):
    value = message.payload.decode().split('=')
    if value[1].isnumeric():
      global access
      access = int(value[1])
