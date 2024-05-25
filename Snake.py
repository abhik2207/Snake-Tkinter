from tkinter import *
import random


GAME_WIDTH = 1000
GAME_HEIGHT = 800
SPEED = 75
SPACE_SIZE = 25
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


class Snake:
    def __init__(self):
        self.bodySize = BODY_PARTS
        self.coordinates = []
        self.squares = []
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)


class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=FOOD_COLOR, tag="food")


def nextTurn(snake, food):
    x, y = snake.coordinates[0]
    if direction == 'up':
        y -= SPACE_SIZE
    elif direction == 'down':
        y += SPACE_SIZE
    elif direction == 'left':
        x -= SPACE_SIZE
    elif direction == 'right':
        x += SPACE_SIZE
    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        scoreLabel.config(text=f"SCORE:{score}")
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    if checkCollisions(snake):
        gameOver()
    else:
        abhik.after(SPEED, nextTurn, snake, food)


def changeDirection(newDirection):
    global direction
    if newDirection == 'left':
        if direction != 'right':
            direction = newDirection
    elif newDirection == 'right':
        if direction != 'left':
            direction = newDirection
    elif newDirection == 'up':
        if direction != 'down':
            direction = newDirection
    elif newDirection == 'down':
        if direction != 'up':
            direction = newDirection


def checkCollisions(snake):
    x, y = snake.coordinates[0]
    if x<0 or x>=GAME_WIDTH:
        return True
    elif y<0 or y>=GAME_HEIGHT:
        return True
    for bodyPart in snake.coordinates[1:]:
        if x == bodyPart[0] and y == bodyPart[1]:
            return True
    return False


def gameOver():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas', 70, 'bold'), text="GAME OVER", fill="#ff0000", tag="gameover")


abhik = Tk()
abhik.title("Snake")
abhik.resizable(False, False)

score = 0
direction = 'down'

scoreLabel = Label(abhik, text=f"SCORE:{score}", font=('consolas', 40, "bold"))
scoreLabel.pack()

canvas = Canvas(abhik, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

abhik.update()

window_width = abhik.winfo_width()
window_height = abhik.winfo_height()
screen_width = abhik.winfo_screenwidth()
screen_height = abhik.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

abhik.geometry(f"{window_width}x{window_height}+{x}+{y}")

abhik.bind('<Left>', lambda event: changeDirection('left'))
abhik.bind('<Right>', lambda event: changeDirection('right'))
abhik.bind('<Up>', lambda event: changeDirection('up'))
abhik.bind('<Down>', lambda event: changeDirection('down'))
abhik.bind('<a>', lambda event: changeDirection('left'))
abhik.bind('<d>', lambda event: changeDirection('right'))
abhik.bind('<w>', lambda event: changeDirection('up'))
abhik.bind('<s>', lambda event: changeDirection('down'))

snake = Snake()
food = Food()

nextTurn(snake, food)

abhik.mainloop()