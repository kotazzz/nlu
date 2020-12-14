import random
import numpy as np

# частота дискретизации
SAMPLE_RATE = 44100
# 16-ти битный звук (2 ** 16 -- максимальное значение для int16)
S_16BIT = 2 ** 16


def generate_sample(freq, duration, volume):
    # амплитуда
    amplitude = np.round(S_16BIT * volume)
    # длительность генерируемого звука в сэмплах
    total_samples = np.round(SAMPLE_RATE * duration)
    # частоте дискретизации (пересчитанная)
    w = 2.0 * np.pi * freq / SAMPLE_RATE
    # массив сэмплов
    k = np.arange(0, total_samples)
    # массив значений функции (с округлением)
    return np.round(amplitude * np.sin(k * w))


#                      до      ре      ми     фа       соль    ля      си
freq_array = np.array([261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88])
random.seed()



def generate_tones(duration):
    tones = []
    for freq in freq_array:
        # np.array нужен для преобразования данных под формат 16 бит (dtype=np.int16)
        tone = np.array(generate_sample(freq, duration, 1.0), dtype=np.int16)
        tones.append(tone)
    return tones


import pyaudio as pa
import pygame

# ... место для предыдущего кода ...

# наши клавиши
key_names = ["a", "s", "d", "f", "g", "h", "j"]
# коды клавиш
key_list = list(map(lambda x: ord(x), key_names))
# состояние клавиш (нажато/не нажато)
key_dict = dict([(key, False) for key in key_list])


if __name__ == "__main__":
    # длительность звука
    duration_tone = 1 / 64.0
    # генерируем тона с заданной длительностью
    tones = generate_tones(duration_tone)
    # инициализируем
    p = pa.PyAudio()
    # создаём поток для вывода
    stream = p.open(
        format=p.get_format_from_width(width=2),
        channels=2,
        rate=SAMPLE_RATE,
        output=True,
    )
    # размер окна pygame
    window_size = 320, 240
    # настраиваем экран
    screen = pygame.display.set_mode(window_size)
    pygame.display.flip()
    running = True
    while running:
        # обрабатываем события
        for event in pygame.event.get():
            # событие закрытия окна
            if event.type == pygame.QUIT:
                running = False
            # нажатия клавиш
            if event.type == pygame.KEYDOWN:
                if event.key == ord("q"):
                    running = False
                # обрабатываем нажатые клавиши по списку key_list
                for (index, key) in enumerate(key_list):
                    if event.key == key:
                        # зажимаем клавишу
                        key_dict[key] = True
            # отпускание клавиш
            if event.type == pygame.KEYUP:
                for (index, key) in enumerate(key_list):
                    if event.key == key:
                        # отпускаем клавишу
                        key_dict[key] = False
        # обрабатываем нажатые клавиши 
        for (index, key) in enumerate(key_list):
            # если клавиша нажата
            if key_dict[key] == True:
                # то выводим звук на устройство
                stream.write(tones[index])
    # закрываем окно
    pygame.quit()
    # останавливаем устройство
    stream.stop_stream()
    # завершаем работу PyAudio
    stream.close()
    p.terminate()
