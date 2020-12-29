import os

wd_name = "NLU Config"
cwd = os.path.join(os.getcwd(), wd_name)

configs = {}
def create_dirs(path):
    if not os.path.exists(path):
        os.makedirs(path)

def create_config(configname, file, path = ""):
    fullpath = os.path.join(os.path.join(cwd, path), '')
    create_dirs(fullpath)
    try:
        f = open(fullpath+f'\\{file}', 'a')
    except:
        f = open(fullpath+f'\\{file}', 'w')
    configs[configname] = os.path.join(cwd, path)+f'\\{file}'
    f.close()
    
def config_get_configs():
    return configs

def config_rewrite(configname, data):
    f = open(configs[configname], 'w')
    f.write(data)
    f.close()
    
def config_apwrite(configname, data):
    f = open(configs[configname], 'a')
    f.write(data)
    f.close()

def config_readall(configname):
    f = open(configs[configname], 'r')
    r = f.read()
    f.close()
    return r

if __name__ == "__main__":
    create_config("cfg","mycfg.txt")
    create_config("cfg2","mycfg2.txt")
    print(config_get_configs())
    print(config_readall("cfg2"))
    
    