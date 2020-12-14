##############################################################
# _   _ _____ _____ _____________   __   _____  _____ _   _  #
#| | | |_   _/  ___|_   _| ___ \ \ / /  |  __ \|  ___| \ | | #
#| |_| | | | \ `--.  | | | |_/ /\ V /   | |  \/| |__ |  \| | #
#|  _  | | |  `--. \ | | |    /  \ /    | | __ |  __|| . ` | #
#| | | |_| |_/\__/ / | | | |\ \  | |    | |_\ \| |___| |\  | #
#\_| |_/\___/\____/  \_/ \_| \_| \_/     \____/\____/\_| \_/ #                                                                                           
##############################################################

#################### INPORTS   ###############################
from enum import Enum
import random
import time
#################### FUNCTIONS ###############################
def select_from (source):
    random_key = random.randrange(1, len(source))
    return source[random.randrange(1, len(source))]

def search(source, key):
    i = 0
    while i < len(source):
        text = source[i]
        if text == key:
            return i
    return 0

#################### LIST VAR  ###############################
L_HISTORY_TYPE =            ['NONE','HAPPY','SAD','UNFINISHED']

L_DATE =                    ['NONE', 'Когда то давно была такая вот история.', 'Эта история произошла недавно, а все было вот как.',
                             'Разговор пойдет об истории с {HERO}']
L_HERO =                    ['NONE', 'Макс', 'Даня', 'Дарья', 'Лиза', 'Настя', 'Сэм', 'Давил', 'Маша', 'Вася',
                             'Гена', 'Валера', 'Миша', 'Сэмуель', 'Виктор', 'Диана']
L_HERO_LIFE_STAGE =         ['NONE', '{HERO} являлся учеником', '{HERO} был старшеклассником', '{HERO} был студентлм']
L_HERO_PROBLEMS =           ['NONE', '{HERO} очень часто гнобили за его ориентацию.', 'у {HERO} не было друзей.',
                             '{HERO} скучал по лучшей подруге, которая переехала.', '{HERO} переезжал, но он этого не хотел.',
                             '{HERO} был худшим учеником в классе', '{HERO} ненавидели родители', '{HERO} был из детдома', '{HERO} бросила девушка']
L_HERO_PROBLEMS_STUDIENT =  ['NONE', '{HERO} был худшим учеником в классе', '{HERO} гнобили в классе', '{HERO} не хотел учиться','{HERO} часто задирали другие']
L_HERO_PERSONALITY =        ['NONE', 'Забывчивый', 'Умный', 'Несдержанный', 'Странный', 'Скрытный',
                             'Стеснительный','Самоуверенный','Прямолинейный','Чистолюбивый','Агрессивный','ЧСВшный','Вечно осуждающий','Вежливый']
L_HERO_PER_DESCRIBE =       ['NONE', '{HERO} по характеру был {PER1} и {PER2}. Он никому не говорил что он еще и {PER3}',
                             '{PER1}, {PER2} и {PER3} - это про {HERO}']
L_BEGIN_HAPPY =             ['NONE', 'Это был обычный день для {HERO}.', 'Казалось что это очередной скучный день.']
L_BEGIN_SAD =               ['NONE', 'У {HERO} прошел день. Очень плохо.', '{HERO} было грустно']
L_BEGIN_UNFINISHED =        ['NONE'] + L_BEGIN_HAPPY[1:len(L_BEGIN_HAPPY)] + L_BEGIN_SAD[1:len(L_BEGIN_SAD)]

L_EVENT_1 =                 ['NONE', 'Казалсь что на сегодня все, но нет, он узнал о том, что его бабушка залетела.', '{HERO} пролил чай',
                             'Кто то пощвонил {HERO} и послал']

L_FINAL_HAPPY =             ['NONE', '{HERO} выйграл миллион', '{HERO} просто выспался']
L_FINAL_SAD =               ['NONE', '{HERO} умер', '{HERO} не разослал 15 сообщений друзьям и умер']
L_FINAL_UNFINISHED =        ['NONE', '{HERO} так и просуществовал в таком состоянии', 'никто из друзей больше не видел {HERO}']
#################### VARIABLES ###############################
class History(object): 
    def load_variables(self):
        self.HISTORY_TYPE = select_from(L_HISTORY_TYPE)

        self.DATE = select_from(L_DATE)
        self.HERO = select_from(L_HERO)
        self.HERO_LIFE_STAGE = select_from(L_HERO_LIFE_STAGE)
        self.HERO_PROBLEMS = select_from(L_HERO_PROBLEMS)
        self.HERO_PERSONALITY_1 = select_from(L_HERO_PERSONALITY)
        self.HERO_PERSONALITY_2 = select_from(L_HERO_PERSONALITY)
        self.HERO_PERSONALITY_3 = select_from(L_HERO_PERSONALITY)
        self.HERO_PER_DESCRIBE = select_from(L_HERO_PER_DESCRIBE)

        self.EVENT_1 = select_from(L_EVENT_1)

        self.FINAL = ''
        self.BEGIN = ''
        if self.HISTORY_TYPE == 'NONE':
            exit(-1)
        if self.HISTORY_TYPE == 'HAPPY':
           self.FINAL = select_from(L_FINAL_HAPPY)
           self.BEGIN = select_from(L_BEGIN_HAPPY)
        if self.HISTORY_TYPE == 'SAD':
           self.FINAL = select_from(L_FINAL_SAD)
           self.BEGIN = select_from(L_BEGIN_SAD)
        if self.HISTORY_TYPE == 'UNFINISHED':
           self.FINAL = select_from(L_FINAL_UNFINISHED)
           self.BEGIN = select_from(L_BEGIN_UNFINISHED)
 
    def getHistory(self, seed, htype):
            self.description = ''
            if seed == True:
                self.description = self.description+f'\n    НОМЕР ИСТОРИИ: {self.seed}'
            if htype == True:
                self.description = self.description+f'\n    ТИП: {self.HISTORY_TYPE}'
                self.history = f'''
 {self.DATE.format(HERO=self.HERO)}. {self.HERO_LIFE_STAGE.format(HERO=self.HERO)}. {self.HERO_PROBLEMS.format(HERO=self.HERO)}
 {self.HERO_PER_DESCRIBE.format(HERO=self.HERO, PER1=self.HERO_PERSONALITY_1, PER2=self.HERO_PERSONALITY_2, PER3=self.HERO_PERSONALITY_3)}
 {self.BEGIN.format(HERO=self.HERO)}
 {self.EVENT_1.format(HERO=self.HERO)}
 {self.FINAL.format(HERO=self.HERO)}
{self.description}'''
            return self.history
    def __init__(self, seed):
        if seed == '0':
            seed_max = str(int(time.time()**20-time.time()))
            seed = f'{seed_max[len(seed_max)-16:len(seed_max)-12]} {seed_max[len(seed_max)-12:len(seed_max)-8]} {seed_max[len(seed_max)-8:len(seed_max)-4]} {seed_max[len(seed_max)-4:len(seed_max)]}'
            random.seed(seed)
            self.seed = seed
        else:
            random.seed(seed)
            self.seed = seed
        self.load_variables()
        
#################### PREPARE   ###############################


#################### MAIN      ###############################
def main():
    want_exit = False
    while not want_exit:        
        seed = input('Введите номер генератора или 0 что бы выбрать рандом:')
        count = 0
        while count < 1000:
            print('======================================================================')
            history = History(seed)
            print(history.getHistory(True, True))
            count +=1
            print(f'=================================================================={count}')

        
        if input('Введите "1" для выхода: ') == '1':
            want_exit = True
        else:
            print('Вы отказались о твыхода. Перезапуск генератора...')


#4140 6930 6372 6260 6838 5090 7648








if __name__ == '__main__':
    main()
