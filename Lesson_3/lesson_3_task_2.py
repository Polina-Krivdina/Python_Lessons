from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 13", "+79234566890"))
catalog.append(Smartphone("Apple", "iPhone 15", "+79238966890"))
catalog.append(Smartphone("Samsung", "Galaxy S21", "+79234566000"))
catalog.append(Smartphone("Xiaomi", "Mi 11", "+79735566890"))
catalog.append(Smartphone("Samsung", "Galaxy Z Flip", "+79767896890"))

for telefon in catalog:
    print(f"{telefon.marka} - {telefon.model}. {telefon.number}")