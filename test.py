from NewLifeUtils.CustomShellModule import Shell
from NewLifeUtils.LoggerModule import log, err
from NewLifeUtils.StringUtilModule import screate


class Column(object):
    def __init__(self, data, size=-1):
        self.data = data
        if size == -1:
            self.size = max([len(str(d)) for d in data])
        else:
            self.size = size

    def add_data(self, data):
        self.data.append(data)

    def build_column(self, type, separator):
        build_line = lambda sep1, sep2: collumn.append(f'{sep1}{screate(data, self.size)}{sep2}')
        collumn = []
        if type == 1:
            for data in self.data:
                build_line(separator, separator)
        elif type == 2:
            for data in self.data:
                build_line('', separator)
        elif type == 3:
            for data in self.data:
                build_line('', separator)
        elif type == 4:
            for data in self.data:
                build_line(separator, separator)
        else:
            raise ValueError('Invalid type (1, 2, 3 or 4)')
        return collumn


class Table(object):
    def __init__(self, collumns, type=0, minify=True):
        self.separators = "╔╦╗║═╠╬╣╚╩╝"
        self.type = type
        self.collumns = collumns
        self.builded_collumns = []
        self.minify = minify

    def get_table(self):
        def add_separator(sizes, type):
            if type == 1:
                sep1 = self.separators[0]
                sep2 = self.separators[4]
                sep3 = self.separators[1]
                sep4 = self.separators[2]

            elif type == 2:
                sep1 = self.separators[5]
                sep2 = self.separators[4]
                sep3 = self.separators[6]
                sep4 = self.separators[7]

            else:
                sep1 = self.separators[8]
                sep2 = self.separators[4]
                sep3 = self.separators[9]
                sep4 = self.separators[10]

            if type == 2:
                sep = '\n' + sep1
            else:
                sep = sep1
            for i in sizes:
                sep += sep2 * i + sep3
            l = list(sep)
            l[-1] = sep4
            sep = ''.join(l)
            if type != 2:
                sep += '\n'
            return sep

        collumn_length = [len(collumn.data) for collumn in self.collumns]
        collumn_sizes = [collumn.size for collumn in self.collumns]
        for collumn in self.collumns:
            while len(collumn.data) < max(collumn_length):
                collumn.add_data('')
        sep = self.separators[3]
        builded_collumns = []
        if len(self.collumns) == 1:
            builded_collumns.append(self.collumns[0].build_column(4, sep))
        elif len(self.collumns) == 2:
            builded_collumns.append(self.collumns[0].build_column(1, sep))
            builded_collumns.append(self.collumns[1].build_column(3, sep))
        else:
            builded_collumns.append(self.collumns[0].build_column(1, sep))
            builded_collumns.append(self.collumns[-1].build_column(3, sep))
            for collumn in self.collumns[1:-1]:
                builded_collumns.append(collumn.build_column(2, sep))
        builded_table = add_separator(collumn_sizes, 1)
        f = False
        for i in range(len(self.collumns[0].data)):
            for collumn in builded_collumns:
                builded_table += collumn[i]
            if not self.minify or not f:
                builded_table += add_separator(collumn_sizes, 2)
                f = True
            builded_table += '\n'
        builded_table += add_separator(collumn_sizes, 3)
        return builded_table


if __name__ == '__main__':
    shell = Shell()
    shell.run()
else:

    data = ["мне",
            "наплевать",
            "еще",
            "раз",
            "между",
            "вами",
            "увижу",
            "оскорбления",
            "пизды",
            "дам",
            "огромных", ]
    c1 = Column(data, )
    c2 = Column(data[2:-3], )
    t1 = Table([c1,c2, ])
    log('\n' + t1.get_table())
