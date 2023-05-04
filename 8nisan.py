# Boş bir To-Do listesi oluşturma
to_do_list = []

# Kullanıcıdan alınan girdileri listeye ekleyen fonksiyon
def add_task(to_do_list):
    task = input("Yapilacak görevi girin: ")
    to_do_list.append(task)
    print("Görev başariyla eklendi.")

# Listede bulunan görevleri gösteren fonksiyon
def show_tasks(to_do_list):
    print("Yapilacak Görevler: ")
    for task in to_do_list:
        print("- " + task)

# Listeden görev silen fonksiyon
def delete_task(to_do_list):
    task = input("Silmek istediğiniz görevi girin: ")
    if task in to_do_list:
        to_do_list.remove(task)
        print("Görev başariyla silindi.")
    else:
        print("Görev bulunamadi.")

# Ana döngü
while True:
    print("\nTo-Do List Uygulamasi")
    print("1. Görev Ekle")
    print("2. Görevleri Göster")
    print("3. Görev Sil")
    print("4. Çikiş")
    choice = input("Seçiminiz (1/2/3/4): ")
    
    if choice == "1":
        add_task(to_do_list)
    elif choice == "2":
        show_tasks(to_do_list)
    elif choice == "3":
        delete_task(to_do_list)
    elif choice == "4":
        print("Uygulamadan çikiliyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")