#pragma once

#include <iostream>

#include <GL/glew.h>
#include <GLM/gtc/matrix_transform.hpp>
#include <GLFW/glfw3.h>

class Snake{
public:
	Snake(int ix);

	void move(bool* keys);

	int getX() { return x; }
	int getY() { return y; }
	int getScore() { return score; }
	void upScore();

	~Snake();
private:
	int x, y, score;
};

