from NewLifeUtils import *


class DatabaseManageModule(object):
    def __init__(self, Logger=None, File=None, Except=None, Table=None):
        self.connection_state = "setup"

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

        if type(Table) == TableBuildModule:
            self.Table = Table
        else:
            self.Table = TableBuildModule()

        self.db_path = self.File.get_path("+database")

    def connect(self, db_name="default_db.db"):
        self.db_name = db_name
        try:
            self.Logger.log(f"Connecting to {self.db_name}")
            self.Logger.log(f"Path: {self.db_path}")
            self.connection = sqlite3.connect(self.db_path + self.db_name)
            self.Logger.log(f"Getting cursor for {self.db_name}...")
            self.cursor = self.connection.cursor()
        except Exception as e:
            self.Except.except_print(e)
            self.Logger.err("Failed to connect to the database")
            self.connection_state = "fault"
        else:
            self.Logger.log("Successfully connected to the database")
            self.connection_state = "connected"

    def create_table(self, table_name, fields):
        table_name = self.check_name(table_name)
        self.execute(f'CREATE TABLE {table_name} ({", ".join(fields)})')

    def add_into_table(self, table_name, values):
        pass

    def print_table_description(self, table_name):
        description = list(self.get_table_description(table_name))
        data = []
        for t in description:
            for e in t:
                data.append(e)
        self.Logger.log(
            self.Table.createMultilineTable(
                6,
                [6, 40, 10, 7, 40, 2],
                ["cid", "name", "type", "notnull", "default", "pk"] + data,
            )
        )

    def print_results_mini(self, result, sizes, header=[]):
        if header == []:
            enable_header = False
        else:
            enable_header = True
        rowCount = 1
        if result != []:
            rowCount = len(result[0])
        data = []
        for t in result:
            for e in t:
                data.append(e)
        self.Logger.log(
            self.Table.createTable(rowCount, sizes, header + data, header=enable_header)
        )

    def print_results(self, result, sizes, header=[]):
        rowCount = 1
        if result != []:
            rowCount = len(result[0])
        data = []
        for t in result:
            for e in t:
                data.append(e)
        self.Logger.log(self.Table.createMultilineTable(rowCount, sizes, header + data))

    def get_table_description(self, table_name):
        self.execute(f"PRAGMA TABLE_INFO('{table_name}')")
        res = self.get_result()
        return res

    def execute(self, request):
        if self.connection_state == "connected":
            self.Logger.log(f"Executing: {request}")
            self.cursor.execute(request)
        else:
            self.Logger.err(
                f"Unable to execute, connection state is {connection_state}"
            )

    def check_name(self, text):
        if text.split() != 1:
            return f"'{text}'"
        else:
            return text

    def get_result(self):
        self.last_result = self.cursor.fetchall()
        return self.last_result

    def get_connection_state(self):
        return self.connection_state

    def get_connection(self):
        return self.connection

    def get_cursor(self):
        return self.cursor


if __name__ == "__main__":
    # cm = ColorModule()
    # sm = StringUtilModule()
    # lm = LoggerModule(cm)
    # em = ExceptModule(lm, sm)
    # tbm = TableBuildModule(sm, cm)
    # csm = CustomShellModule(None, em, sm, cm)
    # um = UtilsModule()
    # fm = FileModule()
    flm = FilelogModule()
    dmm = DatabaseManageModule()
    dmm.connect()

    dmm.get_cursor().execute(f"PRAGMA TABLE_INFO('my table')")
    r = dmm.get_result()
    dmm.print_results(r, [])

    dmm.get_cursor().execute("select * from sqlite_master where type = 'table'")
    r = dmm.get_result()
    dmm.print_results_mini(r, [])
# Traceback (most recent call last):
# File "E:\Документы\_Repo\NewLifeUtils\TheMainCode\DatabaseManageModule dev.py", line 118, in <module>
# dmm.print_results(r,[])
# File "E:\Документы\_Repo\NewLifeUtils\TheMainCode\DatabaseManageModule dev.py", line 76, in print_results
# self.Logger.log(self.Table.createMultilineTable(rowCount,sizes,header+data))
# File "E:\Документы\_Repo\NewLifeUtils\TheMainCode\NewLifeUtils.py", line 515, in createMultilineTable
# data[i] = self.String.sslice(data[i], sizes[i % len(sizes)])
# File "E:\Документы\_Repo\NewLifeUtils\TheMainCode\NewLifeUtils.py", line 158, in sslice
# return [text[i : i + chunkSize] for i in range(0, len(text), chunkSize)]
# ValueError: range() arg 3 must not be zero

# E:\Документы\_Repo\NewLifeUtils\TheMainCode>
