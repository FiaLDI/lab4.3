#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать класс Triad (тройка чисел); определить методы увеличения полей на 1 Определить
# класс-наследник Time с полями: час, минута, секунда. Переопределить методы увеличения
# полей на 1 и определить методы увеличения на n секунд и минут.


class Triad:
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c

    def increment(self):
        self.a += 1
        self.b += 1
        self.c += 1

    def __str__(self):
        return f"Triad({self.a}, {self.b}, {self.c})"


class Time(Triad):
    def __init__(self, hour=0, minute=0, second=0):
        super().__init__(hour, minute, second)
        self.second = second  # Добавляем поле для секунд

    def increment(self):
        self.second += 1
        if self.second >= 60:
            self.second = 0
            self.b += 1  # Увеличиваем минуты
            if self.b >= 60:
                self.b = 0
                self.a += 1  # Увеличиваем часы

    def increment_seconds(self, n):
        for _ in range(n):
            self.increment()

    def increment_minutes(self, n):
        self.b += n
        while self.b >= 60:
            self.b -= 60
            self.a += 1  # Увеличиваем часы

    def __str__(self):
        return f"Time({self.a}h, {self.b}m, {self.second}s)"


if __name__ == "__main__":
    # Пример использования
    triad = Triad(1, 2, 3)
    print(triad)  # Triad(1, 2, 3)
    triad.increment()
    print(triad)  # Triad(2, 3, 4)

    time = Time(12, 30, 45)
    print(time)  # Time(12h, 30m, 45s)
    time.increment()
    print(time)  # Time(12h, 30m, 46s)
    time.increment_seconds(15)
    print(time)  # Time(12h, 31m, 1s)
    time.increment_minutes(30)
    print(time)  # Time(13h, 1m, 1s)
