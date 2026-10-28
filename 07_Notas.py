#lee la nota de un alumno y dependiendo del numero ( 0 - 10)
#le indica si es suspenso ( menos de 5), aprobado (5 o 6)
#notable (7 o 8) o sobresaliente (9 o 10)
nota = int(input("Introduce una nota: "))

match nota:
    case _ if nota < 5:
        print("Estás suspenso")
    case _ if nota <= 6:
        print("Estás aprobado")
    case _ if nota < 9:
        print("Notable")
    case _ if nota >= 9:
        print("Sobresaliente")





        