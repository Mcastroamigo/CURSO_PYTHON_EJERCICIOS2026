num = int(input("Introduce un numero"))

if num<0:
    print("Hace frio")
    
elif num>=0 and num<10 :
    print("Hace fresco")
    
elif num>10 and num<40 :
    print("Hace calor")
    
else: print("No se sabe")