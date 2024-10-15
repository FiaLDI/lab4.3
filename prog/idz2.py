#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать абстрактный базовый класс Container с виртуальными методами sort( ) и
# поэлементной обработки контейнера foreach( ). Разработать производные классы Bubble
# (пузырек) и Choice (выбор). В первом классе сортировка реализуется методом пузырька, а
# поэлементная обработка состоит в извлечении квадратного корня. Во втором классе
# сортировка реализуется методом выбора, а поэлементная обработка — вычисление
# логарифма.

from abc import ABC, abstractmethod
import math


class Container(ABC):
    @abstractmethod
    def sort(self):
        pass

    @abstractmethod
    def foreach(self):
        pass


class Bubble(Container):
    def __init__(self, data):
        self.data = data

    def sort(self):
        n = len(self.data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]

    def foreach(self):
        for value in self.data:
            print(f"Квадратный корень из {value} = {math.sqrt(value)}")


class Choice(Container):
    def __init__(self, data):
        self.data = data

    def sort(self):
        n = len(self.data)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.data[j] < self.data[min_index]:
                    min_index = j
            self.data[i], self.data[min_index] = self.data[min_index], self.data[i]

    def foreach(self):
        for value in self.data:
            print(f"Логарифм из {value} = {math.log(value)}")


if __name__ == "__main__":
    numbers = [4, 9, 8, 1, 25]

    bubble_container = Bubble(numbers.copy())
    bubble_container.sort()
    print(bubble_container.data)
    bubble_container.foreach()

    choice_container = Choice(numbers.copy())
    choice_container.sort()
    print(choice_container.data)
    choice_container.foreach()
