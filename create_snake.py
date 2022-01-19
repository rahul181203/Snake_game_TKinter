import turtle as t
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20 
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake():
    def __init__(self) -> None:
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake(position)
    
    def reset(self):
        for seg in self.snake:
            seg.goto(1000,1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
    
    def add_snake(self,position):
        nithin = t.Turtle(shape="square")
        nithin.color("white")
        nithin.penup()
        nithin.goto(position)
        self.snake.append(nithin)
    
    def extend(self):
        self.add_snake(self.snake[-1].position())
    
    def move(self):
        for seg_num in range(len(self.snake)-1,0,-1):
            new_x = self.snake[seg_num-1].xcor()
            new_y = self.snake[seg_num-1].ycor()
            self.snake[seg_num].goto(new_x,new_y)
        self.head.fd(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)