/**     @file capicua.c
 *      @brief El programa muestra un arreglo de dos dimensiones como laberinto 
 *      @author Delany Quiros-Daniel Chacon
 *      
 *      @details Buscar algoritmo de salida
 *      @bug Desconocido
 *
 */


#include<stdio.h>
#include<stdlib.h>

//Prototipo de funciones
void entrada(char maze[][ COL ]);//Encuentre inicio
void mazetraversal(char maze[ ROW ][ COL ], size_t xDir, size_t yDir, int dir);
void imprimirmaze( char maze[][ COL ]);//imprime el estado del lab
int movimientovalido( char maze[][ COL ], size_t r, size_t c);
int coordinadasborde( size_t x, size_t y);
//Declaracion de las coordinadas en el punto de inicio
int priXcoor, priYcoor;

//Funcion principal 
int main(){
	char maze[ROW][COL]={
		{"1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"},
		{"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"},
		{"1","E","1","0","0","1","1","0","0","1","1","1","1","1","1","1","1","0","1","0","1","0","0","0","0","0","0","1","0","0","0","0","1","1"},
		{"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"},
		{"1","0","1","0","0","1","0","0","0","0","0","0","0","0","1","0","1","0","0","0","0","1","0","0","0","0","0","1","0","0","0","0","1","1"},
		{"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"},
		{"1","0","0","0","1","0","1","1","1","1","1","0","1","1","0","0","0","0","0","1","0","1","0","1","0","0","0","0","1","1","1","1","0","1"},
		{"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"},
		{"1","0","0","0","1","0","0","0","0","1","0","0","1","1","1","1","1","1","1","0","0","0","1","1","1","0","0","1","0","0","0","1","S","1"},
		{"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"},
                {"1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"},

	entrada(maze);
	mazetraversal(maze,priXcoor,priYcoor, RIGHT);
	}

void entrada(char maze[][ COL ]){
	int x;
	priYcoor=0;
	for (x=0;x<ROW;x++){
		if(maze[x][priYcoor]=="0"){
			priXcoor=x;
			return;
		}
	}
}
//da posiciones y decide siguiente movimient
void mazetraversal(char maze[ROW][COL],size_t xDir, size_t yDir, int dir){
	int posicion=0;
	maze[xDir][yDir]="x";
	imprimirmaze(maze);
	
	//Revisa posicion de inicio
	if (xDir==priXcoor && yDir == priYcoor && posicion == 1){
		printf("\n***Posicion de inicio***\n");
		return;
	}

	else if((coordinadasborde(xDir,yDir) && xDir != priXcoor) && yDir != priYcoor)
		printf("\n***Hecho***\n);
		return;
	}

	else{
		int n,siguiente;
		posicion = 1;

			for(n=0, siguiente = dir; n < 4; n++, siguiente++, siguiente %= 4){
				//Switch para decidir siguiente movimiento
				switch( siguiente ){
					case RIGHT;
					//REvisa si tenemos 0 en posicion y+1
						if(movimientovalido( maze, xDir, yDir + 1)){
							mazetraversal( maze, xDir, yDir + 1, DOWN);
							return;
						}
						break;
					case LEFT:
						//Revisar 0 en posicion y-1
						if( movimientovalido( maze, xDir, yDir - 1)){
							mazetraversal(maze, xDir, yDir - 1, UP);
							return;
						}
						break;
					case UP:
						//revisar si tenemos un cero en la posicion x-1
						if(movimientovalido(maze, xDir - 1, yDir)){
							mazetraversal(maze, xDir -1, yDir, RIGHT);
							return;
						}
						break;
					default:
					//revisar cero en posicion x+1
						if(movimientovalido(maze,xDir + 1, yDir)){
							mazetraversal(maze, xDir + 1, yDir,LEFT);
							return;
						}
						break;
				}
			}
	}
}


//Imprimir estado del laberinto luego de cada movimiento
void imprimirmaze( char maze[][ COL ]){
	size_t x; size_t y;
	for(x=0;x < ROW; x++){
		for(y=0; y < COL; y++){	
			printf("%c", maze[ x ][ y ]);
		}
		puts("");
	}
	printf("\n\n")
}
//MOVIMIENTO VALIDO O NO
int movimientovalido(char maze[][ COL ], size_t r, size_t c){
	return (r >= 0 && r <= 33 && c >= 0 && c <= 11 && maze[r] != "1");
}

int coordenadasborde( size_t x, size_t y){
	int borde;
	if ((( x==0||x==33) && (y>=0 && y<=11))||((x>=0 && x<=33)&
	else borde=0;
	return borde;
}
