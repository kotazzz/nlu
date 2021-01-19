from NewLifeUtils.LoggerModule import *
import os
if __name__ == '__main__':
    log("Что то случилось!")
    log("Записиваю информацию...")
    log("Взламываю пентагон")
    wrn("Обрати внимание, что то опасное!")
    err("Что то сломалось, иди чини, даун!")
    tip("Подсказка: выкини комп в помойку, он лагает")
    res = rea("Введите что нибудь")
    tip(f"Перменаая res - {res}")
    os.system("pause")