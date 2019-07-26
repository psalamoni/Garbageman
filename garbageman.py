import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-m", "--move", action="store_true")
group.add_argument("-u", "--upper", action="store_true")
parser.add_argument("vars", nargs="*", type=str)
args = parser.parse_args()

def pathmapping(folder,parameter,recursive):
	import glob

	files = glob.glob(folder + parameter, recursive=recursive)
	return files

def move(batch):
    import os
    import shutil
    
    global args
    global i

    args.vars = list(filter(None, args.vars))

    path = args.vars[0]
    print(path)
    jpgs = pathmapping(path,'*.jpg',False)

    pages = args.vars[1:]

    if batch:
        output_patt = savepath
    else:    
        output_patt = path[:path.rfind('/')+1]

    for jpg in jpgs:
        startnum = jpg.rfind('_')+1
        endnum = jpg.rfind('.')
        jpg_id = str(int(jpg[startnum:endnum])+1)

        if jpg_id not in pages:
            destfile = output_patt + jpg[jpg.rfind('/')+1:]
            shutil.copy2(jpg, destfile)
            print('.', end ="")
            i += 1
    print('.')
    print("PDF splitted successfully, please check the origin folder.")

def upper(batch):
    import os
    import shutil
    
    global args
    global i

    args.vars = list(filter(None, args.vars))

    path = args.vars[0]
    print(path)
    jpgs = pathmapping(path,'**/*.jpg',True)
    print(jpgs)

    for jpg in jpgs:
        if batch:
            output_patt = savepath
        else:    
            output_patt = jpg[:jpg[:jpg.rfind('/')].rfind('/')+1]
        destfile = output_patt + jpg[jpg.rfind('/')+1:]
        shutil.move(jpg, destfile)
        print('.', end ="")
        i += 1
    print('.')
    print("PDF splitted successfully, please check the origin folder.")


import os
import csv

i=1

pathcsv = args.vars[0]
savepath_patt = None
if len(args.vars)>1:
    savepath_patt = args.vars[1]
os.path.normpath(pathcsv)

with open(pathcsv, 'r') as f:
    reader = csv.reader(f, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
    paths = list(reader)

for newarg in paths:
    args.vars = newarg

    if savepath_patt==None:
        if args.move:
            move(False)
        if args.upper:
            upper(False)

    else:
        savepath = savepath_patt + str(int(i/1000)+1)
        if os.path.exists(savepath)==False:
            os.mkdir(savepath)
        savepath += '/'
        if args.move:
            move(True)
        if args.upper:
            upper(True)