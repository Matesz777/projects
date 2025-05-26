import os
import tkinter as tk

#CEL stworz graficzny interfejs, nastepnie dodaj mozliwość zapisywania w konkretnej dacie
#Dodaj mozliwosc Pokazywania dostepnych plikow, aby nie musiec za kazdym razem wpisywac i wybierac plik

def createFile(task_file):
    with open(task_file, "w") as f:
        f.write("Twoja lista zadań na dziś! Powodzenia!")
            

TaskList = []
fileName = None
while True:
    print("To do List!")
    print("Posibilities: " \
        " 1. Create file or choice file" \
        " 2. Add task" \
        " 3. Edit Task" \
        " 4. Delete Task" \
        " 5. Priority" \
        " 6. Show list" \
        " 7. Exit")
    UserChoice = int(input("Give your choice: "))

    if UserChoice == 1:
        fileName = input("Jak chcesz nazwac swoj plik (bez .txt wystarczy sama nazwa) : ")
        fileName = f"{fileName}.txt"
        fileExists = fileName
        if not os.path.exists(fileExists):
            print("Tworzę PLik...")
            createFile(fileName)
        elif os.path.exists(fileExists):
            print("Plik juz istnieje chesz go otworzyć i pracować dalej ? (tak/nie)")
            decision = input(">> ").lower()
            if decision == "tak":
                print("Pracujemy z istniejacym plikiem :D")
                with open(fileExists, "r") as f:
                    loadfile = f.read()
                    print(loadfile)
            elif decision == "nie":
                fileName = input("Jak chcesz nazwac swoj plik (bez .txt wystarczy sama nazwa) : ")
                createFile(fileName)
    if UserChoice == 2:
        addingTask = input("Jaki plan na dzis ?")
        with open(fileName or fileExists, "a") as f:
            f.write("\n" + addingTask)
        print("dodano do listy zadanie", addingTask)

    elif UserChoice == 3:
        try:
            UserEdit = int(input("Podaj pozcyje do edycji: "))
            UserEditText = input("Wpisz treść: ")

            with open(fileName or fileExists, "r") as f:
                lines = f.readlines()

            if UserEdit <= 0 or UserEdit > len(lines):
                print("Nie ma takiego zadania")
            else:
                lines[UserEdit] = UserEditText.strip() + "\n"
                with open(fileName or fileExists, "w") as f:
                    f.writelines(lines)

        except ValueError:
            print("Wprowadz prawidlowa pozycje")

    elif UserChoice == 4:
        deleteTask = int(input("Podaj pozycje którą chcesz usunąć: "))

        with open(fileName or fileExists, "r") as f:
            lines = f.readlines()
        del lines[deleteTask]

        with open(fileName or fileExists, "w") as f:
            f.writelines(lines)

        with open(fileName or fileExists, "r") as f:
            f.read()

    elif UserChoice == 5:
        with open(fileName or fileExists,"r") as f:
            lines = f.readlines()
        tasks = lines[1:]

        UserPriority = int(input("podaj pozycje jaka ma miec priorytet: "))

        if 0 < UserPriority <= len(tasks):
            tasks[0], tasks[UserPriority - 1] = tasks[UserPriority - 1], tasks[0]
            new_lines = [lines[0]] + tasks

            with open(fileName or fileExists, "w") as file:
                file.writelines(new_lines)

            print("Zadanie ustawione jako priorytet!")
        else:
            print("Nie ma takiej pozycji")
    elif UserChoice == 6:
        with open(fileName or fileExists, "r") as f:
            lines = f.readlines()
        if len(lines) <= 1:
            print("Brak zadań do wyświetlenia")
        else:
            print(lines[0].strip())
            tasks = lines[1:]
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
    elif UserChoice == 7: 
        print("Do zobaczenia!")
        break
