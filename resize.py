#coding=utf-8
import sys
sys.path.insert(0, '.')
sys.path.insert(0, './pypackages')
import os
import math
from PIL import Image
import re

def Zoom(w):
        z = min(math.floor( 800 / float(w) * 10) / 10, 1)
        if(z==1):
                z=1
        if(z==0):
                z=0.1
	return z

def Resize():
        print("Resize")
        t=sys.argv[1].split(".")
        t.pop()
        dir='.'.join(t)
        filter=[".jpg",".png"]
        for s in os.listdir(dir):
                print(s)
                ext = os.path.splitext(s)[1]
                if ext in [".png"]:
                        im = Image.open(dir+"/"+s)
                        w, h = im.size
                        rgb_im = im.convert('RGB')
                        zoom = Zoom(w)
                        rgb_im.thumbnail((int(w * zoom), int(h * zoom)),Image.ANTIALIAS)
                        #rgb_im.save(dir+"/"+re.compile(ext).sub('.jpg',s),"jpeg")
                        rgb_im.save(dir+"/"+re.compile(ext).sub('.jpg',s), dpi=[72,72],  quality=72, optimize=True, progressive=True)
                if ext in [".jpg",".jpeg"]:
                        im = Image.open(dir+"/"+s)
                        w, h = im.size
                        zoom = Zoom(w)
                        im.thumbnail((int(w * zoom), int(h * zoom)),Image.ANTIALIAS)
                        #im.save(dir+"/"+s.replace(ext,'.jpg'),"jpeg")
                        im.save(dir+"/"+s.replace(ext,'.jpg'), dpi=[72,72], quality=72, optimize=True, progressive=True)
                os.remove(dir+"/"+s)

if __name__ == "__main__":
    Resize()