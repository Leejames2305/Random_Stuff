#include P18F4520.INC

    CONFIG OSC = INTIO67 ; Internal oscillator, I/O function on RA6/OSC2/CLKO, RA7/OSC1/CLKI
    
    CONFIG WDT=OFF
    CONFIG LVP=OFF
    CONFIG PBADEN=OFF
    LIST P=18F4520
    LIST F=INHX8M

TEMP            EQU 0x20  ; Temporary storage for ADRESH
SCALED_VALUE    EQU 0x21  ; Storage for scaled ADC result

	ORG 0x00
	GOTO MAIN
	
MAIN	
	MOVLW 0x30
	MOVWF OSCCON
	CALL INIT_ADC
	CALL INIT_PWM
	
MAIN_LOOP  
	CALL READ_ADC
	CALL SET_PWM_DUTY
	GOTO MAIN_LOOP
	
INIT_ADC
	MOVLW 0x00
	MOVWF ADCON1
	MOVLW 0x81
	MOVWF ADCON0
	RETURN
	
READ_ADC
	BSF ADCON0, GO
WAIT_ADC
	BTFSC ADCON0, GO
	GOTO WAIT_ADC
	MOVF ADRESH, W
	
	; Scale ADRESH to range 0x08 to 0x10
	; Formula: Scaled_Value = (ADRESH / 32) + 0x08

	RRCF WREG, 0, 0           ; Result is divided using approximation

	MOVWF SCALED_VALUE    ; Store the result in SCALED_VALUE

	; Add the minimum value of the target range (0x08)
	MOVLW 0x08            ; WREG = 0x08 (lower bound of the range)
	ADDWF SCALED_VALUE, F ; Add 0x08 to SCALED_VALUE
	MOVF SCALED_VALUE, W
	RETURN
	
INIT_PWM
	CLRF PORTC  ;Clear data latches at port C bit 2 (ccp1)
	BCF TRISC, 2
	
	MOVLW 0x0C
	MOVWF CCP1CON
	MOVLW 0x9C
	MOVWF PR2
	MOVLW 0x07
	MOVWF T2CON
	
	BCF PIR1, TMR2IF
	BSF T2CON, TMR2ON
	
	RETURN
	
SET_PWM_DUTY
	; Range is 0x08 to 0x10
	MOVWF CCPR1L
	RETURN
	
	END