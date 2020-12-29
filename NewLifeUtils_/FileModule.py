import os

wd_name = "NLU Config"
cwd = os.path.join(os.getcwd(), wd_name)

configs = {}

if not os.path.exists(cwd):
    os.makedirs(cwd)

def create_config(configname, file, path = ""):
    try:
        f = open(os.path.join(cwd, path)+f'{file}', 'a')
    except:
        f = open(os.path.join(cwd, path)+f'{file}', 'w')
    configs[configname] = os.path.join(cwd, path)+f'{file}'
    f.close()
    
def get_configs():
    return configs

def rewrite(configname, data):
    f = open(configs[configname], 'w')
    f.write(data)
    f.close()
    
def apwrite(configname, data):
    f = open(configs[configname], 'a')
    f.write(data)
    f.close()

def readall(configname):
    f = open(configs[configname], 'r')
    r = f.read()
    f.close()
    return r

if __name__ == "__main__":
    create_config("cfg","mycfg.txt")
    create_config("cfg2","mycfg2.txt")
    print(get_configs())
    print(readall("cfg2"))
    
    