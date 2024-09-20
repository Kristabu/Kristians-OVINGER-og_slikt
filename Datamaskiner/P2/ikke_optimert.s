#program start
#input a0 (positivt heltall A)
#output a0 og a1

#initialiser verdier
li a0 17 #input, a0 og a1 er outputs
li a3 0 #sammenligner 
li s2 2 #divider
li s3 1 #startverdi loop
add a4 a4 a0 #mellomlagring av A
div a5 a4 s2 #teller a5 (A/2)
li a0 0
#for loop der i er a5

Div:
    #Deler
    #a5 er høyeste resultat
    div a7 a4 a5 #div produkt
    mul a3 a7 a5
    beq a3 a4 store_value
    bne a3 a4 Loop
    
store_value:
    bne a0 x0 Kvadrattall
    beq a5 s3 Kvadrattall
    add a0 a5 x0
    beq a3 a4 Kvadrattall
    
Loop:
    #negativ loop fra A/2 -> 0
    sub a5 a5 s3
    blt s2 a5 Div
    bgt s2 a5 Primtall
    beq a3 a4 Kvadrattall

         
Kvadrattall:
    div a6 a4 a5
    mul a3 a6 a5
    bne a6 a5 Loop
    li a1 1
    bne a1 x0 Primtall

Primtall: 
    bne a0 x0 Slutt
    li a0 0
    li a1 0
Slutt:
    nop