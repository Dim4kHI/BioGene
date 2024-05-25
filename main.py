from random import randint
from time import sleep
from turtle import *


day = 0
assistant_title = ['помочник','вице-ученый', 'ученый', 'вице-проффессор', 'професор']#       Это переменные которые как либо еще
count_for_title = 0 #                                                                        еще пригодятся в коде
my_title = assistant_title[count_for_title]

class Asiistant():           
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print('Здраствуй',self.name,'! Ты - новый работник BioGenVegetables. Твоя задача ухаживать за растениями, но готов ли ты?')
        sleep(1)
        print('Сейчас выясним! Твоя цель оставить в живых 3 растения и по возможности модифицировать их гены! за каждую модификацию')
        sleep(1)
        print('Твоя должность на работе повысится! Но будь осторожен, гены не всегда стабильны и часто губят растения. поэтому модифицируй')
        sleep(1)
        print('на свой страх и риск, начнем! Только прочтите инстркутаж если оно надо')
        sleep(1)
        guide = input('1 - Прочитать инструктаж 2 - продолжить без него: ')
        if '1' in guide:
            print('всего за растениями вы будете ухаживать 3 рабочих дня')
            sleep(1)
            print('в течении этого времени каждое растение должно оставатся живым')#             Метод для общего ознакомления
            sleep(1)#                                                                            с смиулятором
            print('Условия жизни растений: влага > макс. влаги растения = растение погибло')
            sleep(1)
            print('влага < мин. влаги растения = растение поигибло')
            sleep(1)
            print('также и с органическими веществами')
            print('также у вас есть СПЕЦИАЛЬНАЯ ВОЗМОЖНОСТЬ - модифицировать растения')
            sleep(1)
            print('за каждую модификацию вам повысят звание на вашей будущей работе(помочник,')
            sleep(1)
            print('вице-ученый, ученый, вице-проффессор, професор) но все не так просто')
            sleep(1)
            print('в чем подвох узнаете сами:) Инструктаж окончен!')
            sleep(15)

    def gene_game(self):
        special = 'True'
        step = 10#                                          метод для реализации мини-игры
        step2 = 10#                                     основную часть кода я взял с Hit it (_:
        counter = 0
        game = True

        class Sprite(Turtle):
            def start_place(self, placeX, placeY, color, shape):
                self.speed(99999)
                self.color(color)
                self.shape(shape)
                self.penup()
                self.goto(placeX, placeY)
                self.points=0

        class MainPlayer(Sprite):
            def move_r(self):
                self.goto(self.xcor()+step, self.ycor())
            def move_l(self):
                self.goto(self.xcor()-step, self.ycor())
            def move_u(self):
                self.goto(self.xcor(), self.ycor()+step)
            def move_d(self):
                self.goto(self.xcor(), self.ycor()-step)

        class Enemy(Sprite):
            def walk(self):
                self.forward(step2)
            def check_life(self):
                if self.distance(player) < 15:
                    player.color('white')
                    enemy.color('white')
                    enemy2.color('white')#                          метод для проверки столкновения игрока с врагом
                    enemy3.color('white')
                    enemy4.color('white')
                    finish.color('white')
                    return 'death'

        enemy = Enemy()
        enemy.start_place(-100, 20, 'red', 'square')

        enemy2 = Enemy()
        enemy2.start_place(-100, 0, 'red', 'square')

        enemy3 = Enemy()
        enemy3.start_place(-100, 40, 'red', 'square')

        enemy4 = Enemy()
        enemy4.start_place(-100, 60, 'red', 'square')

        finish = Sprite()
        finish.start_place(0, 200, 'green', 'triangle')

        player = MainPlayer()
        player.start_place(0, -100, 'blue', 'circle')

        scr = player.getscreen()
        scr.onkey(player.move_r, 'Right')
        scr.onkey(player.move_l, 'Left')
        scr.onkey(player.move_u, 'Up')
        scr.onkey(player.move_d, 'Down')
        scr.listen()


        while game:
            enemy.walk()
            enemy2.walk()
            enemy3.walk()
            enemy4.walk()
            if enemy.check_life() == 'death':
                game = False
                special = 'False'
            if enemy2.check_life() == 'death':
                game = False
                special = 'False'
            if enemy3.check_life() == 'death':
                game = False
                special = 'False'
            if enemy4.check_life() == 'death':
                game = False
                special = 'False'
            if player.xcor() > 50 or player.xcor() < -50 or player.ycor() < -200:
                player.start_place(0, -100, 'blue', 'circle')
            counter+=step2
            if finish.xcor() == player.xcor() and finish.ycor() == player.ycor():
                game = False
                special='True'
                player.color('white')
                enemy.color('white')
                enemy2.color('white')
                enemy3.color('white')
                enemy4.color('white')
                finish.color('white')
            if counter == 160:
                step2 = -10
            if counter == 40:
                step2 = 10
        if special== 'False':
            return False
        if special == 'True':
            return True




class Vegetable():
    def __init__(self, type, max_wet, min_wet, max_nutrients, min_nutrients, wet=100, nutrients=100, gene=0, life=True):
        self.type = type
        self.wet = wet
        self.nutrients = nutrients
        self.gene = gene
        self.life = life
        self.max_wet = max_wet
        self.min_wet = min_wet
        self.max_nutrients = max_nutrients
        self.min_nutrients = min_nutrients

    def print_status(self):
        print('Вид -',self.type)
        sleep(0.7)
        print('Влажность -',self.wet)
        sleep(0.7)
        print('Органические вещества -', self.nutrients)
        sleep(0.7)
        print('добавленые гены -',self.gene)#                               с помощью этого метода игрок знает
        sleep(0.7)#                                                         актуальные характеристеки растений
        print('максимальная допустимая влажность -', self.max_wet)
        sleep(0.7)
        print('минимальная допустимая влажность -', self.min_wet)
        sleep(0.7)
        print('максимальное допустимое количество органических веществ -', self.max_nutrients)
        sleep(0.7)
        print('минимальное допустимое количество органических веществ -', self.min_nutrients)
        print()

    def days(self, day_number):
        print('day', day_number)
        sleep(1)#                               метод для основного алгоритма смиулятора 
        self.print_status()#                нужен чтобы не вызывать каждый раз функции в цикле
        sleep(2)
        self.action()

    def action(self):
        print('выберетите действия(любое количество номеров)')
        print('1-Полить 2-удобрить 3-модифицировать гены:')
        action = input('>>>')
        if '1' in action:
            print('влажность повышена')
            self.wet += randint(10, 25)
        else:
            print('влажность понижена')
            self.wet -= randint(10, 25)
        if '2' in action:
            print('органические вещества повышенны')#            метод для проверки действий игрока
            self.nutrients += randint(10, 25)
        else:
            print('органические вещества пониженны')
            self.nutrients -= randint(10, 25)
        if '3' in action:
            if assistant.gene_game():
                global count_for_title
                count_for_title += 1
                print('модификация успешна!')
                print('ваша должность повышена')
                print('на данный момент ваша должность: ', my_title)
                print('')
                sleep(1)
                self.gene+=1
            else:
                print('растение погибло):')
                print('после рабочего дня вашу заявку на работы отклонят')
                print('')
                self.life = False
                
    def chech_func(self, max_wet,min_wet, max_nutrients, min_nutrients):
        if self.wet > max_wet or self.wet < min_wet or self.nutrients > max_nutrients or self.nutrients <min_nutrients:
            return True#                            метод для проверки правило ли игрок ухаживает за растениями
        return False


Your_name = input('Ведите имя...>')
potato = Vegetable('potato', 100, 20, 140, 40, 40, 100)
tomato = Vegetable('tomato', 130, 30, 120, 30, 100, 90)
cucumber = Vegetable('cucumber', 140, 60, 110, 20, 100, 80)
assistant = Asiistant(Your_name)

assistant.welcome()

for i in range(3):
    day+=1
    potato.days(day)
    tomato.days(day)
    cucumber.days(day)
    if potato.life == False or tomato.life == False or cucumber.life == False:
        print('надо быть профессиональней')
        break
    if tomato.chech_func(130, 30, 200, 50):
        print('Упс! вы неправильно ухаживали за томатом!')
        break
    if potato.chech_func(100, 20, 180, 40):
        print('Упс! вы неправильно ухаживали за картошкой!')
        break
    if cucumber.chech_func(140, 30, 170, 20):
        print('Упс! вы неправильно ухаживали за огурцом!')
        break
