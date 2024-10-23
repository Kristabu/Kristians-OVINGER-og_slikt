#input output
#li x10 6
#li x11 5
#li x12 4
#li x13 5
#li x14 2
#li x15 1

#change made
li x22 0

#loop variables
li x8 0
li x9 1

j main

swap1: 
    mv x23, x10
    mv x10, x11
    mv x11, x23
    j swapp_happened
swap2: 
    mv x23, x11
    mv x11, x12
    mv x12, x23
    j swapp_happened
swap3:
    mv x23, x12
    mv x12, x13
    mv x13, x23
    j swapp_happened
swap4:
    mv x23, x13
    mv x13, x14
    mv x14, x23
    j swapp_happened
swap5:
    mv x23 x14
    mv x14 x15
    mv x15 x23
    j swapp_happened

swapp_happened:
    li x8 1
    j while_loop

no_swap:
    li x8 0
    j while_loop

main:

    

while_loop:
    #swap happened?
    bgt x10, x11, swap1
        beq x8 x9 no_swap
    bgt x11 x12 swap2
        beq x8 x9 no_swap
    bgt x12 x13 swap3
        beq x8 x9 no_swap
    bgt x13 x14 swap4
        beq x8 x9 no_swap
    bgt x14 x15 swap5

    beq x8 x0 Slutt


Slutt:
    nop