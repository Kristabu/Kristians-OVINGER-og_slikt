#program start
#input a0 (positivt heltall A)
#output a0 og a1

#initialiser verdier
li a0 16 #input, a0 og a1 er outputs
li a3 0 #sammenligner 
li s2 2 #divider
li s3 2 #startverdi loop
add a4 a4 a0 #mellomlagring av A
div a5 a4 s2 #teller a5 (A/2)

#for loop der i er a5

Loop:
    #Deler
    #a5 er høyeste resultat
    div a0 a4 s3
    mul a3 a0 a5
    beq a0 a5 Kvadrattall
    beq a3 a4 Slutt
    
    #negativ loop fra A/2 -> 0
    addi s3 s3 1
    blt s3 a5 Loop
    beq s3 a5 Primtall

         
Kvadrattall:
    mul a3 a0 a5
    beq a3 a4 Slutt
    bne a3 a4 Loop

Primtall:
    li a0 0
    li a1 0
Slutt:
    nop