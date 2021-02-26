from NewLifeUtils.CustomShellModule import *
import uuid


class DataSector():
    def __init__(self):
        self.uuid = str(uuid.uuid4())

    def __call__(self):
        return dict((key, getattr(self, key)) for key in self.__dict__.keys()
                    if not callable(getattr(self, key)) and not key.startswith('__')) | {'type': type(self).__name__}


########################################################################

class Subject(DataSector):
    def __init__(self, name, begin, end):
        super(Subject, self).__init__()
        self.name = name
        self.beginclass = begin
        self.endclass = end


class Student(DataSector):
    def __init__(self, name, classnumber):
        super(Student, self).__init__()
        self.name = name
        self.classnumber = classnumber


shell = Shell()


@shell.register_command("userlist", description="userlist")
def userlist(console):
    data = [
        Student('Kotaz', 9)(),
        Subject('Math', 3, 9)()
    ]

    import yaml
    log('\n' + yaml.dump(data, default_flow_style=False))
    log(data)


shell.run()
