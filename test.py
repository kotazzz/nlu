#from NewLifeUtils.CustomShellModule import *
from NewLifeUtils.FileModule import *
import yaml
settings_name = "config.yml"
default_settings = {"base_name": "base.yml"}

# print(yaml.dump(a, default_flow_style=False))
#s = Shell()
#s.run()

create_config("test","test.yml","tests",
              {
                "main":"123",
                "main2":"1234",
              })



print(get_pointyaml("test", ""))

