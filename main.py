import time
from turtle import Screen
from player import Player
from Car_Manager import CarManager
from score import Scoreboard

screen = Screen()
screen.setup(width = 600, height= 600)
screen.tracer(0)

player = Player()

scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()

screen.onkey(player.move_forward, 'Up')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    if player.crossed_finish():
        player.reset_turtle()
        scoreboard.increase_level()
        car_manager.increase_speed()
    
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()