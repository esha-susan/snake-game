# snake.py

import random

# --- CONSTANTS (Must match snakecontroller.py) ---
ROWS = 25
COLS = 25
TILE = 25 # Size of one game tile in pixels

WINDOW_WIDTH = TILE * COLS
WINDOW_HEIGHT = TILE * ROWS

# --- DATA STRUCTURES ---
class Tile:
    """Represents one segment of the snake or the food item."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

# --- GAME STATE ---
class SnakeGame:
    def __init__(self):
        self.snake = Tile(5 * TILE, 5 * TILE)
        self.snake_body = []
        self.food = None 
        
        # Start with a safe, non-zero velocity to move immediately
        self.velocityX = TILE   # Snake starts moving right (1 TILE distance)
        self.velocityY = 0
        
        self.gameover = False
        self.score = 0
        
        # Place food after initializing everything else
        self.food = self.place_food()

    def place_food(self):
        """Places food in a random location not occupied by the snake."""
        while True:
            food_x = random.randint(0, COLS - 1) * TILE
            food_y = random.randint(0, ROWS - 1) * TILE

            # Check if food is on the snake's head or body
            if not ((food_x == self.snake.x and food_y == self.snake.y) or any(t.x == food_x and t.y == food_y for t in self.snake_body)):
                return Tile(food_x, food_y)
    # snake.py (CORRECTED move method)

    def move(self):
        """Updates the snake's position and checks for collisions."""
        if self.gameover:
            return

        # 1. Calculate the *next* head position
        new_head_x = self.snake.x + self.velocityX
        new_head_y = self.snake.y + self.velocityY

        # 2. Collision Checks (Based on the new position)
        
        # Wall collision
        if new_head_x < 0 or new_head_x >= WINDOW_WIDTH or \
           new_head_y < 0 or new_head_y >= WINDOW_HEIGHT:
            self.gameover = True
            return

        # Self collision: Check the *next* head position against the current body
        # This is the most crucial part. We check if the NEW head position
        # is the same as the position of ANY existing body segment.
        for tile in self.snake_body:
            if new_head_x == tile.x and new_head_y == tile.y:
                self.gameover = True
                return

        # 3. Eating Food Check
        # We must decide here if we grow the snake or just move the body
        is_eating_food = (new_head_x == self.food.x and new_head_y == self.food.y)

        # 4. Update Body Segments (Append new head and chop tail if not eating)
        
        # The segment the head is currently on (the neck) becomes the first body segment
        new_segment = Tile(self.snake.x, self.snake.y)
        self.snake_body.insert(0, new_segment)
        
        # If not eating, remove the tail segment to simulate forward motion
        if not is_eating_food and len(self.snake_body) > 0:
            self.snake_body.pop()

        # 5. Move the Head
        self.snake.x = new_head_x
        self.snake.y = new_head_y
        
        # 6. Food Replacement and Score Update
        if is_eating_food:
            self.food = self.place_food()
            self.score += 1
    
            
    def reset(self):
        """Resets the game state."""
        self.snake = Tile(5 * TILE, 5 * TILE)
        self.snake_body = []
        self.velocityX = TILE
        self.velocityY = 0
        self.score = 0
        self.gameover = False
        self.food = self.place_food()