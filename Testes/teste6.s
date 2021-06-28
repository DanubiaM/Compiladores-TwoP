.global main
main:
push {ip, lr}       @empilhamento endereco de retorno
MOV R0, #4      @load addres for variable
push {R0}
pop {R1}          @pops in R1
LDR R0, =n1      @load address
STR R1, [R0]      @store  result

MOV R0, #6      @load addres for variable
push {R0}
pop {R1}          @pops in R1

LDR R0, =n2      @load address
STR R1, [R0]      @store  result

MOV R0, #7      @load addres for variable
push {R0}
pop {R1}          @pops in R1

LDR R0, =n3      @load address
STR R1, [R0]      @store  result

MOV R0, #8      @load addres for variable
push {R0}
pop {R1}          @pops in R1

LDR R0, =n4      @load address
STR R1, [R0]      @store  result

LDR R0, =n1      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack variable content

LDR R0, =n2      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack variable content

pop {R1}          @pops in R1
pop {R0}          @pops in R0
ADD R0, R0, R1    @sum operation
push {R0}         @stack result content
LDR R0, =n3      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack variable content

pop {R1}          @pops in R1
pop {R0}          @pops in R0
ADD R0, R0, R1    @sum operation

push {R0}         @stack result content
LDR R0, =n4      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack variable content
pop {R1}          @pops in R1
pop {R0}          @pops in R0

ADD R0, R0, R1    @sum operation
push {R0}         @stack result content
pop {R1}          @pops in R1
LDR R0, =media      @load address

STR R1, [R0]      @store  result
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
.balign 8
n3: .word 0
.balign 8
n4: .word 0
.balign 8
media: .word 0

.global scanf
.global printf
