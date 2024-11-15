'''
This is a pattern that i derived an equation(eq for length and breath of successive patterns)
i wrote a recursive script for implementing this pattern using py turtle


'''
import math 
import turtle as t 
import random 

class Pattern:
	def __init__(self, dim_l, dim_b):
		self.l= dim_l
		self.b= dim_b
    # level is number of recursive steps
    # set level in rectal()
		self.level= 0
		self.rand_tup= (random.randint(0,255),random.randint(0,255),random.randint(0,255))

	def _initial_sq(self):

		side= self.l
		t.colormode(255)
		t.fillcolor(self.rand_tup)
		t.begin_fill()

		t.teleport(0,side/2)
		t.forward(side/2)
		t.rt(90)
		t.forward(side)
		t.rt(90)
		t.forward(side)
		t.rt(90)
		t.forward(side)
		t.rt(90)
		t.forward(side/2)
		t.setheading(0)
		t.lt(180)
		t.end_fill()

	def _dim_calc(self, l, b): 
		self.l= b*b/(math.sqrt((b*b+ l*l/4)))
		self.b= l*b/(2*math.sqrt(l*b + l*l/4))
	
	def _theta(self, l, b):
		l= l/2
		h= math.sqrt((l*l  + b*b))
		theta= math.acos(l/h)
		return math.degrees(theta) 

	def _rectal(self):
		color_val= (random.randint(0,255),random.randint(0,255),random.randint(0,255))

		t.colormode(255)
		t.fillcolor(color_val)
		t.begin_fill()


		if self.level==8:
			t.hideturtle()
			t.exitonclick()
			t.end_fill()
		else: 
			self.level += 1
			t.lt(self._theta(self.l, self.b))
			self._dim_calc(self.l,self.b)
		
			t.forward(self.l)
			t.lt(90)
			t.forward(self.b)
			t.lt(90)
			t.forward(self.l)
			t.lt(90)
			t.forward(self.b)
			t.lt(90)
			t.forward(self.l/2)

			t.end_fill()
			self._rectal()


	def gen(self):
		screen = t.Screen()
		# Set the canvas size (width and height)
		screen.screensize(canvwidth=600, canvheight=600)  # Adjust as needed
		# Set the window size (can be independent of canvas size)
		screen.setup(width=700, height=700)


		self._initial_sq()
		self._rectal()

	
	
obj= Pattern(650, 650)
obj.gen()

