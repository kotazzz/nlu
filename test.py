from NewLifeUtils.CustomShellModule import *
import yaml
import time

settings_name = "config.yml"
default_settings = {"base_name": "base.yml"}

# print(yaml.dump(a, default_flow_style=False))

s = Shell()


@s.register_command("test", [], "my simple command", [], ["param"], False)
def _(console):
    log("123")


s.run()
time.sleep(1)
i = 1
while True:
    i -= 0.01
    st = pow(i, i)
    s.insert_print("log", str(st))
    time.sleep(1)
