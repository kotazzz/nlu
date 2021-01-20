
import os

from NewLifeUtils.ExceptModule import except_print
from NewLifeUtils.LoggerModule import log, err,wrn,tip,rea
from NewLifeUtils.TableBuildModule import createTable
from NewLifeUtils.UtilsModule import select_rand_list
from NewLifeUtils_old.OneCode import CustomShellModule

if __name__ == '__main__':
    mytab = createTable(3, [], [
        "Заголовок1", "Заголовок2", "Заголовок3--------------------",
        "Тут пусто --->", "", "тут капелька",
        "Данные тут", "Привет", "Кто прочитал тот молодец",

    ], "Заголовок")
    bprint()
    log("Что то случилось!")
    log("Записиваю информацию...")
    log("Взламываю пентагон")
    wrn("Обрати внимание, что то опасное!")
    err("Что то сломалось, иди чини, даун!")
    tip("Подсказка: выкини комп в помойку, он лагает")
    res = rea("Введите что нибудь")
    tip(f"Перменаая res - {res}")
    tip(f"Я создал табличку: {mytab}")
    log(f"Список данных: 1 2 3 4 5 6 7 8")
    tip(f"Выбор: {select_rand_list([1,2,3,4,5,6,7,8])}")
    log("Сейчас произайдет ошибка")
    try:
        0/0
    except Exception as e:
        except_print(e)
    shell = CustomShellModule()
    shell.main()



    os.system("pause")