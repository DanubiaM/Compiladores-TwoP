.global main
main:
push {ip, lr}       @empilhamento endereco de retorno
MOV R0, #4      @load addres for variable
push {R0}         @stack result content
pop {R1}          @pops in R1
LDR R0, =n1      @load address
STR R1, [R0]      @store  result
MOV R0, #1       @load addres for variable
push {R0}         @stack result content
pop {R1}          @pops in R1
LDR R0, =n2      @load address
STR R1, [R0]      @store  result
MOV R0, #7      @load addres for variable
push {R0}         @stack result content
pop {R1}          @pops in R1
LDR R0, =n3      @load address
STR R1, [R0]      @store  result
MOV R0, #8      @load addres for variable
push {R0}         @stack result content
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
MOV R0, #4      @load number
push {R0}         @stack variable content
pop {R2}          @pops in R1
pop {R1}          @pops in R2
MOV R0, #0        @init variable for resultable
_division:        @create label
SUBS R1, R1, R2    @subtraction operation
ADD R0, R0,#1     @result division
BHI _division     @jump case R1>R2
push {R0}         @stack result content
pop {R1}          @pops in R1
LDR R0, =media      @load address
STR R1, [R0]      @store  result
LDR R0, =format           @load addres of pattern number
BL printf      @call function for write
LDR R0, =string_1           @load addres of pattern number
BL printf      @call function for write
LDR R0, =media      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack variable content
pop {R0}
MOV R1, R0
MOV R0, #7      @load addres for variable
push {R0}         @stack result content
pop {R0}
MOV R2, R0
CMP R1, R2
@AND OPERATION
BLT L2      @case Val1<Val2
L1:      @label content if
LDR R0, =string_2           @load addres of pattern number
BL printf      @call function for write
B L3      @jump for endif
L2:      @label for else
LDR R0, =string_3           @load addres of pattern number
BL printf      @call function for write
L3:      @label for endif
LDR R0, =string_4           @load addres of pattern number
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
.balign 8
string_1: .asciz ""
.balign 8
string_2: .asciz "Aprovado"
.balign 8
string_3: .asciz "Reprovado"
.balign 8
string_4: .asciz "SUCESSO!"
.global printf
.global scanf
