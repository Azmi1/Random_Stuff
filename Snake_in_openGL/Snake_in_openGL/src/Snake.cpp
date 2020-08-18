#include "Snake.h"

Snake::Snake(int ix){
	x = ix;
	y = ix;
	score = 2;
}

void Snake::move(bool* keys){
	if (keys['W'] == true) {
		y--;
	}
	else if (keys['S'] == true) {
		y++;
	}

	if (keys['A'] == true) {
		x--;
	}
	else if (keys['D'] == true) {
		x++;
	}
}

void Snake::upScore(){
	score++;
}

Snake::~Snake()
{
}