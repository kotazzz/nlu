from NewLifeUtils.CustomShellModule import *


class DataSector():
    def __init__(self, value):
        self.val = value

    def __call__(self, *args, **kwargs):
        return self.val

    def __repr__(self):
        return f'DataSector({self.val} - {type(self.val).__name__})'

    def __str__(self):
        return str(self.val)


class User():
    def __init__(self, id, name):
        self.id = DataSector(id)
        self.name = DataSector(name)

    def __call__(self):
        return dict((key, getattr(self, key)()) for key in self.__dict__.keys()
            if type(getattr(self, key) is DataSector))

    def __str__(self):
        return f'User<#{self.id} {self.name}>'


shell = Shell()


@shell.register_command("userlist", description="userlist")
def userlist(console):

    data =[
            User(1, 'Volmur')(),
            User(2, 'NewLife')(),
            User(3, 'Kotaz')(),
            ]
    import yaml
    log('\n'+yaml.dump(data, default_flow_style=False))


shell.run()
