import paho.mqtt.client as mqtt

# import Adafruit_SSD1306
# from PIL import Image, ImageDraw, ImageFont

# disp = Adafruit_SSD1306.SSD1306_128_32(rst=0)
# disp.begin()
# FONT_PATH = '/usr/share/fonts/truetypr/piboto/PibotoCondensed-Regular.ttf'
# FONT = ImageFont.truetype(FONT_PATH, 22)

# def display_data(t, h):
#    image = Image.new('1', (disp.width, disp.heigth))
#    draw = ImageDraw.Draw(image)
# Draw temperature


def on_connect(client, userdata, flags, rc):
    print(f'Connected with result code {rc}')
    # Subscribe (or renew if reconnect).
    client.subscribe('temp_humidity')


def on_message(client, userdata, msg):
    # Decode temperature and humidity values from binary message payload.
    # t,h = [float(x) for x in msg.payload.decode('utf-8').split(',')]
    s, t, h = msg.payload.decode('utf-8').split(',')
    print(f'Device:{s}    Temp:{float(t):.1f}°C     Humi:{float(h):.1f}%')


client = mqtt.Client()
client.on_connect = on_connect   # Specify on_connect callback
client.on_message = on_message   # Specify on_message callback
client.connect('localhost', 1883, 60)

# Processes MQTT network traffic, callbacks and reconnections. (Blocking)
client.loop_forever()
