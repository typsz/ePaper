#!/usr/bin/python
# -*- coding:utf-8 -*-

import epd2in9
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

try:
    epd = epd2in9.EPD()
    epd.init(epd.lut_full_update)
    epd.Clear(0xFF)
    
    # Drawing on the Horizontal image
    Himage = Image.new('1', (epd2in9.EPD_HEIGHT, epd2in9.EPD_WIDTH), 255)  # 255: clear the frame
    # Drawing on the Vertical image
    Limage = Image.new('1', (epd2in9.EPD_WIDTH, epd2in9.EPD_HEIGHT), 255)  # 255: clear the frame
    
    # Horizontal
    print "Drawing"
    draw = ImageDraw.Draw(Himage)
    font24 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 24)
    draw.text((10, 0), 'hello world', font = font24, fill = 0)
    draw.text((10, 20), '2.9inch e-Paper', font = font24, fill = 0)
    draw.text((150, 0), u'微雪电子', font = font24, fill = 0)    
    draw.line((20, 50, 70, 100), fill = 0)
    draw.line((70, 50, 20, 100), fill = 0)
    draw.rectangle((20, 50, 70, 100), outline = 0)
    draw.line((165, 50, 165, 100), fill = 0)
    draw.line((140, 75, 190, 75), fill = 0)
    draw.arc((140, 50, 190, 100), 0, 360, fill = 0)
    draw.rectangle((80, 50, 130, 100), fill = 0)
    draw.chord((200, 50, 250, 100), 0, 360, fill = 0)
    epd.display(epd.getbuffer(Himage))
    time.sleep(2)
    
    # Vertical
    draw = ImageDraw.Draw(Limage)
    font18 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 18)
    draw.text((2, 0), 'hello world', font = font18, fill = 0)
    draw.text((2, 20), '2.9inch epd', font = font18, fill = 0)
    draw.text((20, 50), u'微雪电子', font = font18, fill = 0)
    draw.line((10, 90, 60, 140), fill = 0)
    draw.line((60, 90, 10, 140), fill = 0)
    draw.rectangle((10, 90, 60, 140), outline = 0)
    draw.line((95, 90, 95, 140), fill = 0)
    draw.line((70, 115, 120, 115), fill = 0)
    draw.arc((70, 90, 120, 140), 0, 360, fill = 0)
    draw.rectangle((10, 150, 60, 200), fill = 0)
    draw.chord((70, 150, 120, 200), 0, 360, fill = 0)
    epd.display(epd.getbuffer(Limage))
    time.sleep(2)
    
    print "read bmp file"
    Himage = Image.open('2in9.bmp')
    epd.display(epd.getbuffer(Himage))
    time.sleep(2)
    
    print "read bmp file on window"
    Himage2 = Image.new('1', (epd2in9.EPD_HEIGHT, epd2in9.EPD_WIDTH), 255)  # 255: clear the frame
    bmp = Image.open('100x100.bmp')
    Himage2.paste(bmp, (50,10))
    epd.display(epd.getbuffer(Himage2))
    time.sleep(2)
    
    # partial update
    epd.init(epd.lut_partial_update)    
    epd.Clear(0xFF)
    time_image = Image.new('1', (epd2in9.EPD_HEIGHT, epd2in9.EPD_WIDTH), 255)
    time_draw = ImageDraw.Draw(time_image)
    while (True):
        time_draw.rectangle((10, 10, 120, 50), fill = 255)
        time_draw.text((10, 10), time.strftime('%H:%M:%S'), font = font24, fill = 0)
        newimage = time_image.crop([10, 10, 120, 50])
        time_image.paste(newimage, (10,10))  
        epd.display(epd.getbuffer(time_image))
        
    epd.sleep()
        
except Exception, e:
    print 'traceback.format_exc():\n%s' % traceback.format_exc()
    exit()

