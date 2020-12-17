# load data
def LoadList(fname):
    f = open(fname,'r')
    data = f.read()
    f.close()
    return eval(data)
# save data
def SaveList(fname,item):
    f = open(fname,'w')
    f.write(str(item))
    f.close()