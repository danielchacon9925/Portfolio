// Laboratorio 2-Daniel Chacón Mora(B72018)|Erick Sancho
// Programa realiza control automático de lavadora con 4 etapas de funcionamiento.

// Librerías utilizadas
// Brinda acceso a entradas y salidas de microcontrolador
#include <avr/io.h>
// Permite usar función _delay_ms()
#include <util/delay.h>
// Utilizada para habilitar interrupciones globales
#include <avr/interrupt.h>
#include <stdio.h>

//Definicion de pines

// Carga
#define HIGH (1<<PA0)
#define MEDIUM (1<<PD6)
#define LOW (1<<PB0)
// START/PAUSE/RESET
#define START_PAUSE (1<<PD3)
#define RESET (1<<PD2)
#define START_PAUSE_LED (1<<PB1)
// LEDs de ciclo
#define FILL_LED (1<<PA2)
#define WASH_LED (1<<PD4)
#define RINSE_LED (1<<PD5)
#define SPIN_LED (1<<PB7)
// LEDS load
#define HIGH_LED (1<<PA1)
#define MEDIUM_LED (1<<PD1)
#define LOW_LED (1<<PD0)



//Definicion de estados
typedef enum {
	STATE_IDE,
	STATE_FILL,
	STATE_WASH,
	STATE_RINSE,
	STATE_SPIN,
	STATE_FINAL
} state_t;


// Varibles globales
// Se define IDE como estado inicial
volatile state_t state = STATE_IDE;
volatile state_t next_state = STATE_IDE;
// Tipo de carga
volatile uint8_t load = 0;
// Tiempo
volatile uint8_t diferential_time_value = 0;
volatile uint8_t time = 0, time_left = 0;

//Declaracion de funciones
// Configuraciones iniciales
void setup();
void SET_TIMER(uint8_t diferential_time_value);
// Configuraciones de 7seg display
void COUNTDOWN_TIMER(int timer);
void LED_7s_display(int valor, int display);
// Máquina de estados
void FSM();
// Estados
uint8_t FILL(uint8_t load);
uint8_t WASH(uint8_t load);
uint8_t RINSE(uint8_t load);
uint8_t SPIN(uint8_t load);
void FINAL(uint8_t load);


// Funcionamiento principal de lavadora
int main(void)
{
	// Se inicia configurando entradas, salidas e interrupciones
    setup();
	// Se pone TIMER en 0
	SET_TIMER(diferential_time_value);
	// Bucle con máquina de estados
	while(1){
		FSM();
	}
	return 0;
}
//______________________________________________________________

////____Configuración de interrupciones y de TIMER____////
// Interrupciones
void setup()
{
	//Configuras los pines como entrada
	DDRB &= ~LOW;
	DDRA &= ~HIGH;
	DDRD &= ~(MEDIUM | RESET | START_PAUSE);
	//Configuras los pines como salida
	DDRD |= (MEDIUM_LED | LOW_LED | WASH_LED | RINSE_LED);
	DDRB |= (START_PAUSE_LED | SPIN_LED);
	DDRA |=	(HIGH_LED | FILL_LED); 

	// Botones habilitados
    PORTD |= (START_PAUSE | RESET | MEDIUM);
	PORTB |= LOW; 
	PORTA |= HIGH;

	//Configucion registro PCMSK para activar interupciones
	PCMSK |= (1<<PCINT0); // Interrupcion LOW

	PCMSK1 |= (1<<PCINT8); // Interrupcion HIGH
    
	PCMSK2 |= (1<<PCINT17); //Interrupcion MEDIUM

	//Configuracion GIMSK para activar interupciones
	GIMSK |= ((1<<PCIE0) | (1<<PCIE1) | (1<<PCIE2)); // LOAD
	GIMSK |= ((1 << INT0) | (1 << INT1)); // START/PAUSE-RESET
	
}
// TIMER
void SET_TIMER(uint8_t diferential_time_value)
{
	// Configurar el prescaler a 64
	TCCR0B |= (1 << CS01) | (1 << CS00);

	// Valor de comparación
	OCR0A = diferential_time_value; 

	// Configuracion del modo de operacion operación CTC (Clear Timer on Compare Match) 
	TCCR0A |= (1 << WGM01);

	// // Habilitar una interrupción de comparación en la salida A del temporizador.
  	TIMSK |= (1 << OCIE0A);

	// Se habilitan interrupciones globales
	sei();
}
//______________________________________________________________

////____Máquina de Estados____////
void FSM()
{	
	if (PORTB & START_PAUSE_LED) // todo
	{
		state = next_state;
		switch (state)
		{
		case STATE_IDE:
			_delay_ms(10000);
			next_state = STATE_FILL; 
			break;	
		case STATE_FILL:
			diferential_time_value = FILL(load);
			next_state = STATE_WASH;
			break;
		case STATE_WASH:
			diferential_time_value = WASH(load);
			next_state = STATE_RINSE;
			break;
		case STATE_RINSE:
			diferential_time_value = RINSE(load);
			next_state = STATE_SPIN;
			break;
		case STATE_SPIN:
			diferential_time_value = SPIN(load);
			next_state = STATE_FINAL;
			break;
		case STATE_FINAL:
			FINAL(load);
			break;
		default:
			next_state = STATE_IDE;
		}
	}
}
// Primer estado: Se llena de agua el tanque de la lavadora
uint8_t FILL(uint8_t load)
{	
	PORTA |= FILL_LED;
	PORTD &= ~(WASH_LED | RINSE_LED );
	PORTB &= ~SPIN_LED;

	if (load == 1){
		diferential_time_value = 1;
		COUNTDOWN_TIMER(diferential_time_value);
	}
	else if (load == 2){
		diferential_time_value = 2;
		COUNTDOWN_TIMER(diferential_time_value);
	}
	else if (load == 3){
		diferential_time_value = 3;
		COUNTDOWN_TIMER(diferential_time_value);
	}

	return diferential_time_value;
}
// Segundo estado
uint8_t WASH(uint8_t load)
{	
	PORTD |= WASH_LED;
	PORTD &= ~RINSE_LED ;
	PORTA &= ~FILL_LED;
	PORTB &= ~SPIN_LED;

	if (load == 1){
		diferential_time_value = 3;
		COUNTDOWN_TIMER(diferential_time_value);
	}
	else if (load == 2){
		diferential_time_value = 5;
		COUNTDOWN_TIMER(diferential_time_value);
	}
	else if (load == 3){
		diferential_time_value = 7; // TODO: No se pudo usar los dos displays al mismo tiempo
		COUNTDOWN_TIMER(diferential_time_value);
	}

	return diferential_time_value;
}
// Tercer estado
uint8_t RINSE(uint8_t load)
{	
	PORTD |= RINSE_LED;
	PORTA &= ~FILL_LED;
	PORTD &= ~WASH_LED;
	PORTB &= ~SPIN_LED;
	
	if (load == 1){
		diferential_time_value = 2;
		COUNTDOWN_TIMER(diferential_time_value);
	}
	else if (load == 2){
		diferential_time_value = 4;
		COUNTDOWN_TIMER(diferential_time_value);
	}
	else if (load == 3){
		diferential_time_value = 5;
		COUNTDOWN_TIMER(diferential_time_value);
	}

	return diferential_time_value;
}
// Cuarto estado
uint8_t SPIN(uint8_t load)
{	
	PORTB |= SPIN_LED;
	PORTD &= ~(WASH_LED | RINSE_LED);
	PORTA &= ~FILL_LED;
	
	if (load == 1){
		diferential_time_value = 3;
		COUNTDOWN_TIMER(diferential_time_value);
	}
	else if (load == 2){
		diferential_time_value = 5;
		COUNTDOWN_TIMER(diferential_time_value);
	}
	else if (load == 3){
		diferential_time_value = 6;
		COUNTDOWN_TIMER(diferential_time_value);
	}
	// Se apaga motor
	PORTB &= ~SPIN_LED;


	return diferential_time_value;
}
// Se termina rutina de lavado
void FINAL(uint8_t load)
{	
	/// Primer blink
	// Enciende
	PORTD |= LOW_LED;
	_delay_ms(1000);
	PORTD |= MEDIUM_LED;
	_delay_ms(1000);
	PORTA |= HIGH_LED;
	_delay_ms(1000);
	// Apaga
	PORTD &= ~LOW_LED;
	_delay_ms(1000);
	PORTD &= ~MEDIUM_LED;
	_delay_ms(1000);
	PORTA &= ~HIGH_LED;
	_delay_ms(1000);
	/// Segundo blink
	// Enciende
	PORTD |= LOW_LED;
	_delay_ms(1000);
	PORTD |= MEDIUM_LED;
	_delay_ms(1000);
	PORTA |= HIGH_LED;
	_delay_ms(1000);
	// Apaga
	PORTD &= ~LOW_LED;
	_delay_ms(1000);
	PORTD &= ~MEDIUM_LED;
	_delay_ms(1000);
	PORTA &= ~HIGH_LED;
	_delay_ms(1000);
	/// Terrcer blink
	// Enciende
	PORTD |= LOW_LED;
	_delay_ms(1000);
	PORTD |= MEDIUM_LED;
	_delay_ms(1000);
	PORTA |= HIGH_LED;
	_delay_ms(1000);
	// Apaga
	PORTD &= ~LOW_LED;
	_delay_ms(1000);
	PORTD &= ~MEDIUM_LED;
	_delay_ms(1000);
	PORTA &= ~HIGH_LED;
	_delay_ms(1000);

		
	// Deja encendido LEDS que indica que finalizó estado
	PORTD |= LOW_LED;
	PORTD |= MEDIUM_LED;
	PORTA |= HIGH_LED;

}
//______________________________________________________________

////////______INTERRUPCIONES______////////
// RESET
ISR(INT0_vect) 
{
	if(PIND & RESET){
		state = STATE_IDE;
		PORTD &= ~RINSE_LED;
		PORTA &= ~FILL_LED;
		PORTD &= ~WASH_LED;
		PORTB &= ~SPIN_LED;
	}
	else{
		/// Primer blink
		// Enciende
		PORTD |= LOW_LED;
		_delay_ms(1000);
		// Apaga
		PORTD &= ~LOW_LED;
		_delay_ms(1000);
		// Enciende
		PORTD |= MEDIUM_LED;
		_delay_ms(1000);
		// Apaga
		PORTD &= ~MEDIUM_LED;
		_delay_ms(1000);
		// Enciende
		PORTA |= HIGH_LED;
		_delay_ms(1000);
		// Apaga
		PORTA &= ~HIGH_LED;
		_delay_ms(1000);
		/// Segundo blink
		// Enciende
		PORTD |= LOW_LED;
		_delay_ms(1000);
		// Apaga
		PORTD &= ~LOW_LED;
		_delay_ms(1000);
		// Enciende
		PORTD |= MEDIUM_LED;
		_delay_ms(1000);
		// Apaga
		PORTD &= ~MEDIUM_LED;
		_delay_ms(1000);
		// Enciende
		PORTA |= HIGH_LED;
		_delay_ms(1000);
		// Apaga
		PORTA &= ~HIGH_LED;
		_delay_ms(1000);
		/// Tercer blink
		// Enciende
		PORTD |= LOW_LED;
		_delay_ms(1000);
		// Apaga
		PORTD &= ~LOW_LED;
		_delay_ms(1000);
		// Enciende
		PORTD |= MEDIUM_LED;
		_delay_ms(1000);
		// Apaga
		PORTD &= ~MEDIUM_LED;
		_delay_ms(1000);
		// Enciende
		PORTA |= HIGH_LED;
		_delay_ms(1000);
		// Apaga
		PORTA &= ~HIGH_LED;
		_delay_ms(1000);

		// Reinicio de máquina de estados
		state = STATE_IDE;
		next_state = STATE_IDE;
		// Reinicio de TIMER
		diferential_time_value = 0; 
		COUNTDOWN_TIMER( diferential_time_value);
		SET_TIMER(diferential_time_value);		
	}
}
// START/PAUSE
ISR(INT1_vect) 
{
	if(PIND & START_PAUSE){
		//Cuando el timer esta activado se detiene
		if (TIMSK & (1<<TOIE0)){
			TIMSK &= ~(1<<TOIE0);
			PORTB &= ~START_PAUSE_LED;
		}
		//Si esta detenido lo iniciamos
		else{
			TIMSK |= (1<<TOIE0);
			PORTB |= START_PAUSE_LED;
		}
	}
}
// LOW 
ISR(PCINT0_vect)
{
	if(PINB & LOW){
		load = 1;
		PORTD |= LOW_LED;
	}
	else {
		PORTD &= ~LOW_LED;
	}

}
// MEDIUM
ISR(PCINT2_vect) 
{
	if(PIND & MEDIUM){
		load = 2;
		PORTD |= MEDIUM_LED;
	}
	else {
		PORTD &= ~MEDIUM_LED;
	}

}
//HIGH
ISR(PCINT1_vect) 
{
	if(PINA & HIGH){
		load = 3;
		PORTA |= HIGH_LED;
	}
	else {
		PORTA &= ~HIGH_LED;
	}
}

ISR(TIMER0_COMPA_vect) {
  // Aqui va la rutina de interrupcion
  // Hacer LED display cada vez que se produzca la interrupción
	static uint8_t contador = 0;
	contador++;
	 
	// Se configuró el timer0 con un prescales de 64 y reloj de 1 MHz
	// Se ocupan 15625 ciclos del timer para que pase un segundo
	if(contador == 15625){
		time++;
		time_left--;
		//LED_7s_display()
	}
	else if(time == diferential_time_value){
		//LED_7s_display(0,0)
		TCNT0 = 0;
		TIMSK &= ~(1<<TOIE0);
	}
	contador = 0;
	time = 0;
	time_left = 0;
}
//______________________________________________________________

////____DISPLAYS____////
// Funciones encargadas de mostrar tiempo restante
// COUNTDOWN_TIMER hace llamado a impresion en 7segmentos
// LED_7s_display muestra número en display indicado.

void COUNTDOWN_TIMER(int timer)
{
	while(timer > 0)
	{
		LED_7s_display(timer, 1);
		_delay_ms(10000);
		timer--;
	}
	LED_7s_display(0, 0);
}
void LED_7s_display(int valor, int display)
{
	PORTB &= 0b10000111;
    if (display == 0)
	{
		if (valor == 0) PORTB |= 0b00000000;

		else if (valor == 1) PORTB |= 0b01000000; 

		else if (valor == 2) PORTB |= 0b00100000; 

		else if (valor == 3) PORTB |= 0b01100000;

		else if (valor == 4) PORTB |= 0b00010000;

		else if (valor == 5) PORTB |= 0b01010000;

		else if (valor == 6) PORTB |= 0b00110000;

		else if (valor == 7) PORTB |= 0b01110000;

		else if (valor == 8) PORTB |= 0b00001000;

		else PORTB |= 0b01001000;
	}
	else  // display == 1
	{
		if (valor == 0) PORTB |= 0b00100000;

		else if (valor == 1) PORTB |= 0b01000100; 

		else if (valor == 2) PORTB |= 0b00100100; 

		else if (valor == 3) PORTB |= 0b01100100;

		else if (valor == 4) PORTB |= 0b00010100;

		else if (valor == 5) PORTB |= 0b01010100;

		else if (valor == 6) PORTB |= 0b00110100;

		else if (valor == 7) PORTB |= 0b01110100;

		else if (valor == 8) PORTB |= 0b00001100;

		else PORTB |= 0b01001100;
	}
}
//______________________________________________________________
