import os

weekdays = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]
schedule = []

try:
    os.remove('env.py')
    print("Configurações antigas removidas com sucesso")
except:
    print("Nenhuma configuração prévia encontrada")

for day in weekdays:
    daySchedule = []
    if input("Tem alguma aula de "+day+"? (y/n)\n").lower() == "y":
        while True:
            startTime = input('Insira o horário de início da aula "HH:MM": \n')
            endTime = input('Insira o horário de termino da aula "HH:MM": \n')
            classID = input("Insira o ID de acesso da aula: \n")
            daySchedule.append([classID, startTime.split(":"), endTime.split(":")])
            if input("Mais alguma aula de "+day+"? (y/n)\n").lower() != "y":
                break
    schedule.append(daySchedule)

envFile = open("env.py", "w+")
envFile.write("schedule = "+str(schedule))
envFile.close()