import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
from time import sleep
from datetime import datetime

# Set up display
i2c = board.I2C()
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)
small_font = ImageFont.truetype('FreeSans.ttf', 12)
large_font = ImageFont.truetype('FreeSans.ttf', 33)
disp.fill(0)
disp.show()

# Make an image to draw on in 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)

# Display a message on 3 lines, first line big font        
def display_message(top_line, line_2):
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    draw.text((0, 0),  top_line, font=large_font, fill=255)
    draw.text((0, 50),  line_2, font=small_font, fill=255)
    disp.image(image)
    disp.show()

while True:
    now = datetime.now()
    date_message = '{:%d %B %Y}'.format(now)
    time_message = '{:%H:%M:%S}'.format(now)
    display_message(time_message, date_message)
    sleep(0.1)
