
path = '/Users/mac/Desktop/Python_Homework/Mobile_Guide/file.txt'


def import_data(u:str):
    with open(path, 'r') as copy_file:
        new_data = copy_file.read()
    
    n_data = new_data.split()
    k = n_data[0]
    l = n_data[1]
    m = n_data[2]
    
    fin = ['k','l','m']
    u = print(",".join(map(str, fin)))
   
    return(u)

path1 = '/Users/mac/Desktop/Python_Homework/log.csv'

def rewrite(u: str):
    with open(path1, 'a') as lis:
        lis.write(u)





        