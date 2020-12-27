# load data
def LoadList(fname):
    f = open('./data/' + fname,'r')
    data = f.read()
    f.close()
    return eval(data)
# save data
def SaveList(fname,item):
    f = open('./data/' + fname,'w')
    f.write(str(item))
    f.close()