from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food
from time import sleep

WIDTH = 600
HEIGHT = 600
FOOD_SIZE = 10
FOOD_THRESHOLD = FOOD_SIZE * 1.5
WALL_THRESHOLD = 20
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Snake")

screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < FOOD_THRESHOLD:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > WIDTH/2-WALL_THRESHOLD or snake.head.ycor() > HEIGHT/2-WALL_THRESHOLD or snake.head.xcor() < -WIDTH/2+WALL_THRESHOLD or snake.head.ycor() < -HEIGHT/2+WALL_THRESHOLD:
        scoreboard.reset()
        snake.reset()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < FOOD_SIZE:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
