#include "Snake.h"

Snake::Snake(int ix, int ivel_tabele){
	x = ix;
	y = ix;
	score = 2;
	vel_tabele = ivel_tabele;
}

void Snake::changeDir(bool* keys){
	if (keys['W'] == true)
		direct = UP;

	else if (keys['S'] == true)
		direct = DOWN;

	else if (keys['A'] == true)
		direct = LEFT;

	else if (keys['D'] == true)
		direct = RIGHT;
}

void Snake::move(){
	switch (direct) {
		case UP:
			y--;
			break;
		case DOWN:
			y++;
			break;
		case LEFT:
			x--;
			break;
		case RIGHT:
			x++;
			break;
	}
}

void Snake::upScore(){
	score++;
}

Snake::~Snake()
{
}