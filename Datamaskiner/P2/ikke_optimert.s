#program start
#input a0 (positivt heltall A)
#output a0 og a1

#initialiser verdier
#li a0 21 #input
li s2 2
li s3 1 #steg i loop
div a1 a0 s2 #teller a2

#for loop der i er a2

Loop:
    #Deler
    #a2 er høyeste resultat
    div a2 a0 a1
    mul a3 a2 a1
    beq a3 a0 Slutt
    
    #negativ loop fra A/2 -> 0
    sub a1 a1 s3
    beq a1 x0 Slutt
    bgt a1 x0 Loop
    
    #loop funksjonen
    #addi a3 a3 1 
    #blt a2 a3 Slutt #i når range
    #bgt a2 a3 Loop

Slutt:
    nop