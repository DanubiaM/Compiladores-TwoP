.global main
main:
push {ip, lr}       @empilhamento endereco de retorno
LDR R0, =string_1           @load addres of pattern number
BL printf      @call function for write
LDR R0, =format       @load addres of pattern number
LDR R1, =idade       @load addres of variable
BL scanf  @call function for read
LDR R0, =idade      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack variable content
pop {R0}          @pops R0
MOV R1, R0        @mov content for R1
MOV R0, #18      @load number
push {R0}         @stack variable content
pop {R0}      @pops R0
MOV R2, R0        @mov content for r2
CMP R1, R2        @compar contents
@AND OPERATION
BLE L2      @case Val1<Val2
LDR R0, =idade      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack variable content
pop {R0}          @pops R0
MOV R1, R0        @mov content for R1
MOV R0, #60      @load number
push {R0}         @stack variable content
pop {R0}      @pops R0
MOV R2, R0        @mov content for r2
CMP R1, R2        @compar contents
@AND OPERATION
BGE L2       @case Va1>Val2
@AND OPERATION
L1:      @label content if
LDR R0, =string_2           @load addres of pattern number
BL printf      @call function for write
B L3      @jump for endif
L2:      @label for else
LDR R0, =idade      @load addres for variable
LDR R0, [R0]      @load data of variable
push {R0}         @stack variable content
pop {R0}          @pops R0
MOV R1, R0        @mov content for R1
MOV R0, #18      @load number
push {R0}         @stack variable content
pop {R0}      @pops R0
MOV R2, R0        @mov content for r2
CMP R1, R2        @compar contents
@AND OPERATION
BGE L5       @case Va1>Val2
@AND OPERATION
L4:      @label content if
LDR R0, =string_3           @load addres of pattern number
BL printf      @call function for write
B L6      @jump for endif
L5:      @label for else
LDR R0, =string_4           @load addres of pattern number
BL printf      @call function for write
L6:      @label for endif
L3:      @label for endif
pop {ip, pc}
.data
.balign 8
format: .asciz "%d"
.balign 8
idade: .word 0
.balign 8
string_1: .asciz "Digite sua idade" 
.balign 8
string_2: .asciz "Voce e adulto" 
.balign 8
string_3: .asciz "Voce e adolecente ou crianca" 
.balign 8
string_4: .asciz "Você e idoso" 
.global printf
.global scanf

