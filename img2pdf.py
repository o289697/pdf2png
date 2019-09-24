#coding=utf-8
import sys
sys.path.insert(0, '.')
sys.path.insert(0, './pypackages')
import os
import fitz
import shutil

def custom_sort(x,y):
        if x>y:
                return 1
        if x<y:
                return -1
        return 0
        
def ToPdf():
        print("ToPdf")
        t=sys.argv[1].split(".")
        t.pop()
        dir='.'.join(t)        
        path_list = os.listdir(dir)
        path_name=[]
        path_name_dict={}
        for i in path_list:
                l=int(i.split(".")[0])
                path_name.append(l)
                path_name_dict[l]=i

        path_name=sorted(path_name, custom_sort)

        doc = fitz.open()  
        for file_name in path_name:
                img=dir+"/"+path_name_dict[file_name]
                print path_name_dict[file_name]
                imgdoc = fitz.open(img)                 
                pdfbytes = imgdoc.convertToPDF()        
                imgpdf = fitz.open("pdf", pdfbytes)
                doc.insertPDF(imgpdf)   
        #os.remove(dir+".pdf")               
        doc.save(dir+".pdf")
        doc.close()
        shutil.rmtree(dir)

if __name__ == "__main__":
    ToPdf()