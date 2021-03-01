from NewLifeUtils.CustomShellModule import *
from NewLifeUtils.TableBuildModule import *
from NewLifeUtils.ColorModule import *
import uuid

ACC.RESET
class DataSector():
    def __init__(self, customuuid = None):
        try:
            customuuid = uuid.UUID(customuuid)
        except TypeError:
            self.uuid = str(uuid.uuid4())
        else:
            self.uuid = customuuid

    def __call__(self):
        return dict((key, getattr(self, key)) for key in self.__dict__.keys()
                    if not callable(getattr(self, key))
                    and not key.startswith('__')
                    and not key.startswith('r_')) | {'type': type(self).__name__}


########################################################################

class Subject(DataSector):
    def __init__(self, name, begin, end, customuuid = None):
        super(Subject, self).__init__(customuuid)
        self.name = name
        self.beginclass = begin
        self.endclass = end


class Student(DataSector):
    def __init__(self, name, classnumber, customuuid = None):
        super(Student, self).__init__(customuuid)
        self.name = name
        self.classnumber = classnumber


class Mark(DataSector):
    def __init__(self, subject, mark, user, customuuid = None):
        super(Mark, self).__init__(customuuid)
        self.subject = subject()
        self.mark = mark
        self.user = user()
        self.date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        self.r_date = datetime.datetime.now()
        self.r_user = user
        self.r_subject = subject


shell = Shell()
users = []

@shell.register_exit_task()
def exit_task(console):
    save_data = {}
    save_users = []
    for user in users:
        save_users.append(
            {
                "name": user.name,
                "classnumber": user.classnumber,
                "uuid": str(user.uuid)
            }

        )
    log(f'Succesfull saved {len(users)} users')

    save_data['users'] = save_users
    storage = DataStorage('storage.yml', 'data')
    storage.data = save_data
    storage.save()
    log(f'Succesfull saved all data')

@shell.register_init_task()
def init_task(console):
    global users
    storage = DataStorage('storage.yml', 'data')
    try:
        storage['users']
    except KeyError:
        wrn('Storage is broken/empty')
    else:
        for rawuser in storage['users']:
            users.append(
                Student(rawuser['name'],rawuser['classnumber'], rawuser['uuid'])
            )
        log(f"Loaded {len(storage['users'])} users")



@shell.register_command("studadd", description="userlist", required=['name', 'class'], optional=[])
def useradd(console: Shell):
    stop = False
    if not (15 >= len(console.parametrs[0])):
        wrn('Name too long (Max: 15)')
        stop = True

    if not (len(console.parametrs[0]) >= 3):
        wrn('Name too short (Min: 3)')
        stop = True

    try:
        int(console.parametrs[1])
    except ValueError:
        wrn('Class must be int')
        stop = True
    else:
        if not (11 >= int(console.parametrs[1]) >= 1):
            wrn('Invalid class')
            stop = True
    if not stop:
        user = Student(console.parametrs[0], int(console.parametrs[1]))
        users.append(user)
        log(f'New student {user.name} ({user.classnumber})')

@shell.register_command("studdel", description="userlist", required=['uuid'], optional=[])
def userdel(console):
    try:
        srchuuid = uuid.UUID(console.parametrs[0])
    except ValueError:
        wrn('invalid uuid')
    else:

        for num, user in enumerate(users):
            if uuid.UUID(user.uuid) == srchuuid:
                users.pop(num)
                log('Succesfull')
                break
        else:
            wrn('Cannot find')

@shell.register_command("studlist", description="userlist", optional=[])
def userlist(console):
    table = ["id", "name", "class", "uuid"]
    for num, user in enumerate(users):
        table.append(num)
        table.append(user.name)
        table.append(user.classnumber)
        table.append(user.uuid)
    log(create_table(4, [], table))

@shell.register_command("studview", description="userlist", required=['uuid'], optional=[])
def studview(console):
    try:
        srchuuid = uuid.UUID(console.parametrs[0])
    except ValueError:
        wrn('invalid uuid')
    else:

        for num, user in enumerate(users):
            if uuid.UUID(str(user.uuid)) == srchuuid:
                log('Succesfull finded')
                log(f'Pos: {num}')
                log(f'Name: {user.name}')
                log(f'Class: {user.classnumber}')
                break

        else:
            wrn('Cannot find')



shell.unregister_by_name('hello')
shell.unregister_by_name('parse')
shell.unregister_by_name('info')
shell.run()
