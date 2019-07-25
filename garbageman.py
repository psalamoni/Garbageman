import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-m", "--move", action="store_true")
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

    args.vars = list(filter(None, args.vars))

    path = args.vars[0]
    print(path)
    jpgs = pathmapping(path,'*.jpg',False)
    print(jpgs)

    pages = args.vars[1:]

    if batch:
        output_patt = savepath
    else:    
        output_patt = path[:path.rfind('/')+1]

    for jpg in jpgs:
        startnum = jpg.rfind('_')+1
        endnum = jpg.rfind('.')
        jpg_id = int(jpgs[startnum:endnum])

        if jpg_id not in pages:
            destfile = output_patt + jpg[jpg.rfind('/')+1:]
            shutil.copy2(jpg, destfile)
    print("PDF splitted successfully, please check the origin folder.")

if args.move:
    import os
    import csv

    pathcsv = args.vars[0]
    savepath = None
    if len(args.vars)>1:
        savepath = args.vars[1]
    os.path.normpath(pathcsv)

    with open(pathcsv, 'r') as f:
        reader = csv.reader(f, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        paths = list(reader)

    for newarg in paths:
        args.vars = newarg
        if savepath==None:
            move(False)
        else:
            move(True)