# This is a sample Python script.
import random


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def randomize_teams(names):
    anz = len(names)
    count = anz / 2
    for i in range(int(count)):
        sample = random.sample(names, 2)
        for e in sample:
            names.remove(e)
        print("Team", i + 1, ":", sample)


if __name__ == '__main__':
    names = ["Aldi", "Dinu", "Kapy", "Sati", "Osman", "Rashi", "Solem", "Vasee"]
    randomize_teams(names)

