#coding=utf-8
import sys
sys.path.insert(0, '.')
sys.path.insert(0, './pypackages')
import os
import fitz

def ToPng():
        print("ToPng")
#============== 
        t=sys.argv[1].split(".")
        t.pop()
        dir='.'.join(t)
        #==============
        if not os.path.exists(dir):
                os.mkdir(dir)
        #==============        
        i=1
        p=0
        while i<len(sys.argv):
                doc = fitz.open(sys.argv[i])
                print("{}:{}".format(sys.argv[i], doc.pageCount) )
                for pg in range(doc.pageCount):
                        page = doc[pg]
                        rotate = int(0)
                        # 每个尺寸的缩放系数为1，这将为我们生成分辨率提高四倍的图像。
                        zoom_x = 2.0
                        zoom_y = 2.0
                        trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
                        pm = page.getPixmap(matrix=trans, alpha=False)
                        pm.writePNG("%s/%i.png" % (dir,p+pg))
                        print(pg)
                p+=doc.pageCount
                i+=1
        #==============
       

if __name__ == "__main__":
    ToPng()