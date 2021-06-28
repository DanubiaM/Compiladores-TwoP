.global main
main:
push {ip, lr}       @empilhamento endereco de retorno
LDR R0, =string_1           @load addres of pattern number
BL printf      @call function for write
LDR R0, =format       @load addres of pattern number
LDR R1, =n       @load addres of variable
BL scanf  @call function for read
MOV R0, #1      @load addres for variable
push {R0}         @stack result content
pop {R1}          @pops in R1
LDR R0, =fatorial      @load address
STR R1, [R0]      @store  result
LDR R0, =n      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack variable content
MOV R0, #1      @load number
push {R0}         @stack variable content
pop {R1}          @pops in R1
pop {R0}          @pops in R0
ADD R0, R0, R1    @sum operation
push {R0}         @stack result content
pop {R1}          @pops in R1
LDR R0, =parada      @load address
STR R1, [R0]      @store  result
MOV R0, #0      @load addres for variable
push {R0}         @stack result content
pop {R1}          @pops in R1
LDR R0, =cont      @load address
STR R1, [R0]      @store  result
LDR R0, =n      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack result content
pop {R1}         @pops in R1
LDR R0, =format           @load addres of pattern number
BL printf      @call function for write
LDR R0, =parada      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack variable content
pop {R1}         @pops in R1
LDR R0, =format           @load addres of pattern number
BL printf      @call function for write
LDR R0, =fatorial      @load addres for variable
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
n: .word 0
.balign 8
fatorial: .word 0
.balign 8
cont: .word 0
.balign 8
parada: .word 0
.balign 8
string_1: .asciz "Digite um numero"
.global printf
.global scanf
