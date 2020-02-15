import turtle 
yak = turtle.Turtle()
yak.left(90)
yak.speed(90)

def tree(i):
	if i < 10:
		return

	else:
		yak.forward(i)
		yak.left(30)
		tree(3*i/4)
		yak.right(60)
		tree(3*i/4)
		yak.left(30)
		yak.backward(i)



tree(30)
turtle.done()

