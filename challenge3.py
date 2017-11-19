def __init__(self,configfile):
    with open('./test.cfg') as configfile:
        for x in configfile:
        #print(x,end='')
            y=x.strip()
        #print(y,end='')
        #print(y.split('='))
            z=y.split('=')
            print(z[1])
            self._config={z[0]:z[1]}
            print(self._config)

with open('./user.csv') as information:
    for x in information:
        #print(x,end='')
        y=x.strip()
        z=y.split(',')
        print(z[1])
        _config={z[0]:z[1]}
        print(_config)

if __name__=="main":
    print(__init__.z1)
