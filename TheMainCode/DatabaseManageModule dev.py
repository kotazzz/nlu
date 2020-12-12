from NewLifeUtils import *
class DatabaseManageModule(object):
    def __init__(self, Logger = None, File = None, Except = None):
        self.connection_state = 'setup'
        
        if type(Logger) == LoggerModule:
            self.Logger = Logger
        else:
            self.Logger = LoggerModule()
            
        if type(File) == FileModule:
            self.File = File
        else:
            self.File = FileModule()
            
        if type(Except) == ExceptModule:
            self.Except = Except
        else:
            self.Except = ExceptModule()
        
        self.db_path = self.File.get_path("+database")
    def connect(self, db_name = 'default_db.db'):
        self.db_name = db_name
        try:
            self.Logger.log(f'Connecting to {self.db_name}')
            self.Logger.log(f'Path: {self.db_path}')
            self.connection = sqlite3.connect(self.db_path + self.db_name)
            self.Logger.log(f'Getting cursor for {self.db_name}...')
            self.cursor = self.connection.cursor()
        except Exception as e:
            self.Except.except_print(e)
            self.Logger.err('Failed to connect to the database')
            self.connection_state = 'fault'
        else:
            self.Logger.log('Successfully connected to the database')
            self.connection_state = 'connected'
    
if __name__ == "__main__":
    # cm = ColorModule()
    # sm = StringUtilModule()
    # lm = LoggerModule(cm)
    # em = ExceptModule(lm, sm)
    # tbm = TableBuildModule(sm, cm)
    # csm = CustomShellModule(None, em, sm, cm)
    # um = UtilsModule()
    # fm = FileModule()
    # flm = FilelogModule()
    dmm = DatabaseManageModule()
    dmm.connect()