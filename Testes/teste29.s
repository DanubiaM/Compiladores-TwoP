.global main
main:
push {ip, lr}       @empilhamento endereco de retorno
MOV R0, #1      @load addres for variable
push {R0}         @stack result content
pop {R1}          @pops in R1
LDR R0, =n1      @load address
STR R1, [R0]      @store  result
MOV R0, #3      @load addres for variable
push {R0}         @stack result content
pop {R1}          @pops in R1
LDR R0, =n2      @load address
STR R1, [R0]      @store  result
L3:      @label for while
LDR R0, =n1      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack variable content
pop {R0}
MOV R1, R0
LDR R0, =n2      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack variable content
pop {R0}
MOV R2, R0
CMP R1, R2
@AND OPERATION
BGT L2       @case Va1>Val2
@AND OPERATION
L1:      @label content while
LDR R0, =n1      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack variable content
MOV R0, #1      @load number
push {R0}         @stack variable content
pop {R1}          @pops in R1
pop {R0}          @pops in R0
ADD R0, R0, R1    @sum operation
push {R0}         @stack result content
pop {R1}          @pops in R1
LDR R0, =n1      @load address
STR R1, [R0]      @store  result
B L3      @jump loop while
L2:      @label for endwhile
LDR R0, =n1      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack variable content
pop {R1}         @pops in R1
LDR R0, =format           @load addres of pattern number
BL printf      @call function for write
pop {ip, pc}
.data
.balign 8
format: .asciz "%d"
.balign 8
n1: .word 0
.balign 8
n2: .word 0
.global printf
.global scanf
