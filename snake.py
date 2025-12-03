import random

#CONSTANTS
ROWS=25
COLS=25
TILE=25  #game tile size in pixels

WINDOW_WIDTH=TILE*COLS
WINDOW_HEIGHT=TILE*ROWS

class Tile:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
#GAME STATE
class SnakeGame:
    def __init__(self):
        self.snake=Tile(5*TILE,5*TILE)
        self.snake_bosy=[]
        self.food=None

        self.velocityX=TILE
        self.velocityY=0

        self.gameover=False
        self.score=0

        self.food=self.place_food()

#PLACE THE FOOD AT RANDOM POSITIONS
    def place_food(self):
        while True:
            food_x=random.randint(0,COLS-1)*TILE
            food_y=random.randint(0,ROWS-1)*TILE

            if not (food_x==self.snake.x and food_y==self.snake.y)or any(t.x==food_x and t.y==food_y for t in self.snake_body):
                return Tile(food_x,food_y)