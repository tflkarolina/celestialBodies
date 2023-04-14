from tkinter import messagebox

class CiałoNiebieskie:
    def __init__(self, nazwa, masa, odleglosc_od_slonca, okres_obiegu):

        self.nazwa = nazwa
        self.masa = float(masa)
        self.odleglosc_od_slonca = float(odleglosc_od_slonca)
        self.okres_obiegu = float(okres_obiegu)

    def __str__(self):
        return f"Nazwa: {self.nazwa}, Masa: {self.masa}, Odległość od Słońca: {self.odleglosc_od_slonca}, Okres obiegu: {self.okres_obiegu}"

    def get_odleglosc(self):
        return self.odleglosc_od_slonca

    def get_masa(self):
        return self.masa

    def get_okres(self):
        return self.okres_obiegu

    @staticmethod
    def convert_to_cialo(obj):
        return CiałoNiebieskie(obj.nazwa, obj.masa, obj.odleglosc_od_slonca, obj.okres_obiegu)

global ciala_niebieskie

ciala_niebieskie = [
    CiałoNiebieskie("Merkury", 0.33, 0.39, 0.24),
    CiałoNiebieskie("Wenus", 4.87, 0.72, 0.62),
    CiałoNiebieskie("Ziemia", 5.97, 1.00, 1.00),
    CiałoNiebieskie("Mars", 0.642, 1.52, 1.88),
    CiałoNiebieskie("Jowisz", 1898, 5.20, 11.86),
    CiałoNiebieskie("Saturn", 568, 9.58, 29.46),
    CiałoNiebieskie("Uran", 86.8, 19.18, 84.01),
    CiałoNiebieskie("Neptun", 102, 30.07, 164.79)
]

#pomocnicza funkcja do sortowania kubełkowego
def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        var = bucket[i]
        j = i - 1
        while j >= 0 and var < bucket[j]:
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = var

#ODLEGLOSC OD SLONCA
def bucket_sort_odl():
    input_list = [(CiałoNiebieskie.convert_to_cialo(item)).get_odleglosc() for item in ciala_niebieskie]

    max_value = max(input_list)
    size = max_value / len(input_list)

    buckets_list = []
    for x in range(len(input_list)):
        buckets_list.append([])

    for i in range(len(input_list)):
        j = int(input_list[i] / size)
        if j != len(input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])


    for z in range(len(input_list)):
        insertion_sort(buckets_list[z])


    final_output = []
    for x in range(len(input_list)):
        final_output = final_output + buckets_list[x]

    for i in range(len(final_output)):
        for planet in ciala_niebieskie:
            if final_output[i] == planet.get_odleglosc():
                final_output[i] = None
                final_output[i] = planet
                break
    return final_output


def bucket_sort_odl_mal():
    input_list = [(CiałoNiebieskie.convert_to_cialo(item)).get_odleglosc() for item in ciala_niebieskie]

    max_value = max(input_list)
    size = max_value / len(input_list)


    buckets_list = []
    for x in range(len(input_list)):
        buckets_list.append([])


    for i in range(len(input_list)):
        j = int(input_list[i] / size)
        if j != len(input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])

    for z in range(len(input_list)):
        insertion_sort(buckets_list[z])

    final_output = []
    for x in range(len(input_list)):
        final_output = final_output + buckets_list[x]

    for i in range(len(final_output)):
        for planet in ciala_niebieskie:
            if final_output[i] == planet.get_odleglosc():
                final_output[i] = None
                final_output[i] = planet
                break
    return final_output[::-1]

#MASA
def bucket_sort_masa():
    input_list = [(CiałoNiebieskie.convert_to_cialo(item)).get_masa() for item in ciala_niebieskie]

    max_value = max(input_list)
    size = max_value / len(input_list)

    buckets_list = []
    for x in range(len(input_list)):
        buckets_list.append([])

    for i in range(len(input_list)):
        j = int(input_list[i] / size)
        if j != len(input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])


    for z in range(len(input_list)):
        insertion_sort(buckets_list[z])

    final_output = []
    for x in range(len(input_list)):
        final_output = final_output + buckets_list[x]

    for i in range(len(final_output)):
        for planet in ciala_niebieskie:
            if final_output[i] == planet.get_masa():
                final_output[i] = None
                final_output[i] = planet
                break
    return final_output

def bucket_sort_masa_mal():
    input_list = [(CiałoNiebieskie.convert_to_cialo(item)).get_masa() for item in ciala_niebieskie]

    max_value = max(input_list)
    size = max_value / len(input_list)

    buckets_list = []
    for x in range(len(input_list)):
        buckets_list.append([])

    for i in range(len(input_list)):
        j = int(input_list[i] / size)
        if j != len(input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])

    for z in range(len(input_list)):
        insertion_sort(buckets_list[z])

    final_output = []
    for x in range(len(input_list)):
        final_output = final_output + buckets_list[x]

    for i in range(len(final_output)):
        for planet in ciala_niebieskie:
            if final_output[i] == planet.get_masa():
                final_output[i] = None
                final_output[i] = planet
                break
    return final_output[::-1]

#OKRES
def bucket_sort_okres():
    input_list = [(CiałoNiebieskie.convert_to_cialo(item)).get_okres() for item in ciala_niebieskie]

    max_value = max(input_list)
    size = max_value / len(input_list)

    buckets_list = []
    for x in range(len(input_list)):
        buckets_list.append([])

    for i in range(len(input_list)):
        j = int(input_list[i] / size)
        if j != len(input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])

    for z in range(len(input_list)):
        insertion_sort(buckets_list[z])


    final_output = []
    for x in range(len(input_list)):
        final_output = final_output + buckets_list[x]

    for i in range(len(final_output)):
        for planet in ciala_niebieskie:
            if final_output[i] == planet.get_okres():
                final_output[i] = None
                final_output[i] = planet
                break
    return final_output

def bucket_sort_okres_mal():
    input_list = [(CiałoNiebieskie.convert_to_cialo(item)).get_okres() for item in ciala_niebieskie]

    max_value = max(input_list)
    size = max_value / len(input_list)


    buckets_list = []
    for x in range(len(input_list)):
        buckets_list.append([])


    for i in range(len(input_list)):
        j = int(input_list[i] / size)
        if j != len(input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])


    for z in range(len(input_list)):
        insertion_sort(buckets_list[z])


    final_output = []
    for x in range(len(input_list)):
        final_output = final_output + buckets_list[x]

    for i in range(len(final_output)):
        for planet in ciala_niebieskie:
            if final_output[i] == planet.get_okres():
                final_output[i] = None
                final_output[i] = planet
                break
    return final_output[::-1]

print("Ciała niebieskie w Układzie Słonecznym:")
for cialo in ciala_niebieskie:
    print(cialo.__str__())