#addi a0, x0, 10
#addi a1, x0, -110
#addi a2, x0, -2
#addi a3, x0, -2
#addi a4, x0, -7
#addi a5, x0, 5

add s2, a0, a1
add s3, a2, a3
add s4, a4, a5

bge s2, s3, a0a1 #a>b hopp
bge s3, s4, a2a3
bge s4, s2, a4a5

a0a1:
    blt s2, s4, a4a5
    addi a0, s2, 0
    jal x0, Slutt
a2a3:
    addi a0, s3, 0
    jal x0, Slutt
a4a5:
    addi a0, s4, 0
    jal x0, Slutt

Slutt:
    nop



    