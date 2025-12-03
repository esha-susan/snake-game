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
        self.snake_body=[]
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

            if not ((food_x==self.snake.x and food_y==self.snake.y)or any(t.x==food_x and t.y==food_y for t in self.snake_body)):
                return Tile(food_x,food_y)
    
    def move(self):
        if self.gameover:
            return

        new_head_x = self.snake.x + self.velocityX
        new_head_y = self.snake.y + self.velocityY

        # Check collisions with walls
        if new_head_x < 0 or new_head_x >= WINDOW_WIDTH or new_head_y < 0 or new_head_y >= WINDOW_HEIGHT:
            self.gameover = True
            return

        # Check collisions with body
        for tile in self.snake_body:
            if new_head_x == tile.x and new_head_y == tile.y:
                self.gameover = True
                return

        # Check if eating food
        is_eating_food = (new_head_x == self.food.x and new_head_y == self.food.y)

        # Add current head as new body segment
        new_segment = Tile(self.snake.x, self.snake.y)
        self.snake_body.insert(0, new_segment)

        # Remove tail if not eating
        if not is_eating_food and len(self.snake_body) > 0:
            self.snake_body.pop()

        # Update head position
        self.snake.x = new_head_x
        self.snake.y = new_head_y

        # If eating, place new food and increase score
        if is_eating_food:
            self.food = self.place_food()
            self.score += 1



    def reset(self):
        self.snake=Tile(5*TILE,5*TILE)
        self.snake_body=[]
        self.velocityX=TILE
        self.velocityY=0
        self.score=0
        self.gameover=False
        self.food=self.place_food()
        