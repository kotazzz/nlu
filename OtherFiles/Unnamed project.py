# -*- coding: utf-8 -*-
# new project
from NewLifeUtils import *
import pymorphy2
import csv
def get_gender(name):
    gender = pymorphy2.MorphAnalyzer().parse(name)[0].tag.gender
    if gender == 'masc':
        return 'm'
    if gender == 'femn':
        return 'f'
        
def generate_school():
    tbm = TableBuildModule()
    data = []
    with open("Unnamed project - HSD.csv", newline="", encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=";", quotechar="|")
        for row in spamreader:
            for el in row:
                data.append(str(el))
    morph = pymorphy2.MorphAnalyzer()
    city_t_r = tbm.get_column(
        tbm.get_record(9, data, random.randrange(1, tbm.get_record_count(9, data))), 9, 3
    )
    city_t = morph.parse(city_t_r[0])[0].inflect({"loct"}).word
    city_r = tbm.get_column(
        tbm.get_record(9, data, random.randrange(1, tbm.get_record_count(9, data))), 9, 2
    )
    city = city_r[0]
    school_id = random.randrange(1, 150)
    school_name = f"Школа в {city_t} {city} #{school_id}"
    return [school_name, school_id]

        
class DataSector(object):
    data_storage = {}
    def create_section(self, name, *args):
            try:
                self.data_storage[name]
            except:
                self.data_storage[name] = []
            for item in args:
                self.data_storage[name].append(item)
    def get_storage(self):
        return(self.data_storage)
    def get_section(self, section_name):
        return(self.data_storage[section_name])

class DefSector:
    class School(object):
        def __init__(self):
            schooldata = generate_school()
            self.school_name = schooldata[0]
            self.school_number = schooldata[1]
            self.school_id = '123'
    class Cabinet(object):
        room_type = 'general'
    class ClassCabinet(Cabinet):
        specification = 'chemistry'
        
    class Person(object):
        name = 'Аркадий'
        surname = 'Котазов'
        patronymic = 'Михаилович'
        
    class Staff(Person):
        staff_type = 'director'
    class Teacher(Person):
        school_subjects = ['Математика', 'Физика']
    class Student(Person):
        goal = {"type":"stud"}
        
    class Subject:
        pass
        
class CommandsSector:
    class Info(CustomShellModule.Command):
        command = "инфо"
        aliases = [command, "информация"]
        description = "Вся информация о коммандах"
        required = []
        optional = []
        skipcheck = False
        def run(console):
            info = '\n---------------------------------------------\n'
            info += 'Это мой новый проект основанный на NLU5\n'
            info += 'Больше нет доступной информации\n'
            info += '---------------------------------------------\n'
            console.Logger.log(info)
def other():
    class Task:
        def execute(console):
            logger = LoggerModule()
            PersonInfo = DataSector()
            datafile =open('Unnamed project - data.json', 'r', encoding='utf8')
            data = json.loads(datafile.read())
            PersonInfo.create_section('names',data['names'])
            PersonInfo.create_section('surnames',data['surnames'])
            PersonInfo.create_section('patronymics',data['patronymics'])
            
    #Init CustomShellModule
    cmd = CustomShellModule()
    
    #Register commands
    cmd.registerCommand(CommandsSector.Info)
    
    #Register tasks
    cmd.registerInitTask(Task)
    
    #start main cycle
    cmd.main()
if __name__ == "__main__":
    myschool = DefSector.School()