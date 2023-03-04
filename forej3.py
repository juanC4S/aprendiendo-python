text="Hola, me llamo Juan Carlos. ¿Tu como te llamas?"
signos=[" ", ".", ","]
canti=0
contespa=0
contpuntos=0
contcomas=0
for cha_r in text:
    
    if cha_r in signos: 
        canti+=1
        print("signo: [ {} ] encontrado ".format(cha_r))
        if cha_r ==" ":
            contespa+=1
        if cha_r ==".":
            contpuntos+=1
        if cha_r ==",":
            contcomas+=1
print("cantidad de signos encontrados: ",canti)
print("cantidad de signos [espacios] encontrados: ",contespa)
print("cantidad de signos [ . ] encontrados: ",contpuntos)    
print("cantidad de signos [ , ]encontrados: ",contcomas)        
        
    # elif cha_r ==".":
        
    #     contpuntos+=1
        
    # elif cha_r==",":
        
    #     contcomas+=1
            
    # print ("hay {} espacios en esa frase".format(contespa))
    # print ("hay {} puntos en esa frase".format(contpuntos))
    # print ("hay {} comas en esa frase".format(contcomas))

