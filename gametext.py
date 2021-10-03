import time
import random

class Game():
        def __init__(self):
            self.using = None
            self.day=0
            self.health=100
            self.food=100
            self.ills=0
            time.sleep(2)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n███╗░░░███╗░█████╗░██╗░░██╗░██████╗███╗░░░███╗░█████╗░██████╗░░██████╗\n"
                                                      "████╗░████║██╔══██╗██║░██╔╝██╔════╝████╗░████║██╔══██╗██╔══██╗██╔════╝\n"
                                                      "██╔████╔██║███████║█████═╝░╚█████╗░██╔████╔██║███████║██████╔╝╚█████╗░\n"
                                                      "██║╚██╔╝██║██╔══██║██╔═██╗░░╚═══██╗██║╚██╔╝██║██╔══██║██╔══██╗░╚═══██╗\n"
                                                      "██║░╚═╝░██║██║░░██║██║░╚██╗██████╔╝██║░╚═╝░██║██║░░██║██║░░██║██████╔╝\n"
                                                      "╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░")
            time.sleep(2)
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            self.name_changer()
            self.food_num=4
            self.medic_num=1
            self.pills=2
            self.energy = 0
            self.coffe = 1
            self.super_live=0
            print('Пролог\nКак самого успешного космического туриста, вас отправляют в полёт от Земли до Марса.\nКосмический корабль, на котором вас отправили, оборудован новейшей системой жизнеобеспечения, техническими посещениями и небольшой фермой.')
            time.sleep(5)
            print('Также, двигатели нового образца доставят вас до нужной точки за 100 дней!\nУдивительно, не правда ли?!После запуска, к несчастью, вы обнаружили, что вам забыли обновить припасы... В вашем грузовом отсеке вы наблюдаете лишь одну коробку, в которой находится:')
            time.sleep(5)
            print(f'Консервы {self.food_num} Таблетки {self.pills} Аптечка {self.medic_num} BlackBool {self.coffe}.')
            print('И ни одного тюбика с джемом! Какая досада!Но, несмотря на это, руководство продолжило полёт. Сырых ресурсов достаточно для изготовления всего необходимого, а системы налажены и не поддадутся сбою.Вы в космосе, дорогой турист!')
            time.sleep(12)
            self.runing()

        def name_changer(self):
            space=' '
            self.player_name = input('Имя персонажа:')
            if self.player_name == None:
                print('Uncorrect Name')
                self.name_changer()
            if self.player_name == '':
                print('Uncorrect Name')
                self.name_changer()
            for spaces in self.player_name:
                if space == spaces:
                    print("don't use space or void")
                    self.name_changer()

        def stats(self):
            print("\n Статистика:              Вещи:\nЗдоровье = {}             Консервы(+FOOD): {}"
                  "\nСытность = {}              Аптечка(+HP): {}\nЗаболевание = {}           Таблетки(-ILLS): {}\n"
                  "Усталость: {}            BlackBools: {}\n                        Полное востановление {}\n".format(self.health,
                                                                                              self.food_num, self.food,
                                                                                              self.medic_num, self.ills,
                                                                                              self.pills, self.energy,
                                                                                              self.coffe,
                                                                                              self.super_live))

        def louses(self):
            a = random.randint(1, 3)
            if a == 1:
                a=random.randint(1,4)
                if a == 1:
                    if self.food_num>0:
                        self.food_num= self.food_num-1
                        print('Мы потеряли\n\nКонсервы -1')
                    else:
                        self.louses()
                if a == 2:
                    if self.pills>0:
                        self.pills=self.pills-1
                        print('Мы потеряли\n\nТаблетки -1')
                    else:
                        self.louses()
                if a == 3:
                    if self.medic_num>0:
                        self.medic_num=self.medic_num-1
                        print('Мы потеряли\n\nАптечка -1')
                    else:
                        self.louses()
                if a == 4:
                    if self.coffe>0:
                        self.coffe=self.coffe-1
                        print('Мы потеряли\n\nBlackBool -1')
                    else:
                        self.louses()
                print('О нет мы потеряли несколько ресурсов')
            elif a == 2:
                print('О нет капитан вас задело камушком')
                self.health=self.health-random.randint(1,40)
                if self.health < 1:
                    self.health=0
            elif a == 3:
                print('Нам повезло!!! Всё осталось цело и невредимо')

        def events(self):
            b=random.randint(1, 50)
            if b <= 5:
                c = random.randint(1,4)
                print('Сегодня вы обнаружили обломки корабля, обыскав их вам удалось найти кое какие припасы ')
                if c == 1:
                    self.food_num=self.food_num+1
                    print('\nКонсервы +1')
                elif c == 2:
                    self.pills=self.pills+1
                    print('\nТаблетки +1')
                elif c == 3:
                    self.medic_num=self.medic_num+1
                    print("\nАптечка +1")
                elif c ==4:
                    self.coffe=self.coffe+1
                    print("\nBlackBool +1")
            elif 6<=b<=8:
                a = random.randint(1, 2)
                print('Вы видели космических пиратов')
                if a == 1:
                    print('Но ничего не произошло')
                elif a == 2:
                    print("Они начали обстрел из своих лазерных орудий!!! О НЕТ КАПИТАН ВАС ЗАДЕЛО")
                    self.health=self.health-random.randint(1,99)
                    if self.health < 1:
                        self.health=1
            elif 9<=b<11:
                print("Капитан В каюту!!!! Начался МЕТЕОРИТНЫЙ ДОЖДЬ!!!")
                self.louses()
            elif b == 11:
                print("Ваш сын вырос\nНедавно, вы узнали, что ваш сын подрос и собирается жениться... А ведь вы помните, что ему было лишь 14, когда вы отправились в далёкий космос... Время летит быстро... Даже слишком...")
            elif 11<b<=13:
                print('Солнечная вспышка\nВо время путешествия, вы чувствуете себя не слишком хорошо. Наоборот, вы страдаете от головной боли и тошноты, вам необходимо принять таблетку для излечения\n\nБолезни +10')
                self.ills=self.ills+10
                if self.ills>100:
                    self.ills=100
            elif 14<=b<18:
                print("Чайник?\nВо время вашего полёта, радар засёк неопознанный объект. Когда вы пролетаете мимо него, на камерах слежения становится заметен маленький фарфоровый чайник. Или вам это уже кажется? Что вообще происходит?\n\nУсталость +10")
                self.energy=self.energy+10
                if self.energy>100:
                    self.energy=100
            elif 18<=b<21:
                print('Космический мусор.\nВнезапным ударом об обломки спутника, вас откидывает в панель управления. В следующий раз советуем вам пристегнуться!\n\nЗдоровье -10\nУсталость +10')
                self.energy=self.energy+10
                self.health=self.health-10
                if self.energy>100:
                    self.energy=100
            elif 21<=b<24:
                print('Заначка.\nВы нашли коробку, оставленную предыдущем пилотом! Какая удача!\n\nРедбулл +2\nКонсервы +1')
                self.coffe=self.coffe+1
                self.food_num=self.food_num+1
            elif 24<=b<28:
                print("Крысы на борту!\nТолько не это! Крыса попала к вам на борт! И она съела часть запасов! Благо, вы её быстро нашли и посадили в надёжное место. Не забывайте её кормить!\n\nКонсервы -2")
                self.food_num=self.food_num-2
                if self.food_num<0:
                    self.food_num=0
            elif 28<=b<32:
                print("Бессонница.\nВы устали, но никак не можете уснуть. Вас беспокоят вести с Земли, да и стресс от полёта начинает проявляться.\n\nУсталость +30\nЗдоровье -5")
                self.energy=self.energy+30
                self.health=self.health-5
            elif 32<=b<=35:
                print("")
            elif 46 <= b < 50:
                print("Одиночество. Вы чувствуете себя разбито.\n Вы давно не слышали голоса своих родственников и одиночество тяготит вашу душу.\n А ещё, вы потихоньку начали сходить с ума...\n Вы заметили это, после того, как пытались обвинить консервную банку с ананасами в измене и выкинуть предателя за борт!\n\n Здоровье -10\n Консервы -1\n Усталость +10")
                self.health = self.health - 10
                self.food_num = self.food_num - 1
                self.energy = self.energy + 10
            elif 42 <= b < 45:
                print("Странный мужик. На корабле, вы обнаружили странного мужика, лет 40...\n Но вас больше удивила телефонная будка синего цвета за его спиной...\n Более того, вы чувствуете себе намного лучше...\n\n Здоровье +40\n Усталость -5")
                self.health = self.health + 40
                self.energy = self.energy - 5
            elif 38 <= b < 44:
                print("Хороший сон. Вам удалось хорошенько отдохнуть!\n Вы чувствуете себя полным сил и здоровым как бык!\n\n Здоровье +10\n Усталость -10")
                self.health = self.health + 10
                self.energy = self.energy - 10
            else:
                print('Ночь прошла без проишествий!')


        def scripting(self):
            a = random.randint(0, 100)
            try:
                self.using = input("{} Виберите действие:\n\n1.Кушать\n2.Использовать аптечку\n3.Таблетки\n4.Создать консервы (шанс 50%)\n5.Создание медикаментов(шанс таблеток 30%; шанс аптечки 20%)\n6.Закончить день     7.Выпить BlackBool      8.Super_live     0.Status\n ==> ".format(self.player_name))
            except ValueError:
                print("Укажите цельное значение\n")
            try:
                if int(self.using) == int(self.using):
                    if int(self.using) == 1:
                        if self.food_num >0:
                            self.food_num=self.food_num-1
                            self.food = self.food + random.randint(15, 41)
                            print('Вы кушаете')
                            if self.food>100:
                                self.food=100
                            self.scripting()
                        else:
                            print('У вас недостаточно консерв!')
                            self.scripting()
                        if self.food>100:
                            self.food = 110
                    elif int(self.using) == 2:
                        if self.medic_num>0:
                            self.energy=self.energy+5
                            self.medic_num=self.medic_num-1
                            self.health=self.health + random.randint(45, 90)
                            if self.health>100:
                                self.health=100
                            print('Вы применили Аптечку')
                            self.scripting()
                        else:
                            print('У вас недостаточно аптечек!')
                            self.scripting()
                        if self.health > 100:
                            self.health=100
                    elif int(self.using)==3:
                        if self.pills>0:
                            self.energy=self.energy+5
                            self.pills=self.pills-1
                            self.ills=self.ills - random.randint(5,20)
                            if self.ills<0:
                                self.ills=0
                            print('Вы лечитесь')
                            self.scripting()
                        else:
                            print('У вас недостаточно таблеток!')
                            self.scripting()
                        if self.ills > 100:
                            self.ills=0
                    elif int(self.using) == 4:
                        if self.energy<85:
                            self.energy=self.energy+random.randint(15,30)
                            if self.energy>100:
                                self.energy=100
                            if 0<=a<=30:
                                print('Вы создали консервы')
                                self.food_num=self.food_num+1
                            else:
                                a = random.randint(1, 4)
                                if a ==1:
                                    print('Вы питались приготовить еду но её украл ТАРАКАН! Настоящий ТАРАКАН? Вы в печали(((')
                                if a==2:
                                    print('Вам попалось испорченное сырье, но вы слишком поздно это заметили. Готовка не задалась.')
                                if a ==3:
                                    print("Вы слишком плохо готовите :(")
                                if a ==4:
                                    print('После того, как вы приготовили себе консерву, вы ловите себя на мысли, что забыли её закрыть??? Как такое вообще возможно???')
                            self.scripting()
                        else:
                            print('Вы слишком устали выпейте BlackBool или закончите день!')
                            self.scripting()
                    elif int(self.using) == 5:
                        if self.energy<85:
                            self.energy = self.energy + random.randint(15,30)
                            if self.energy>100:
                                self.energy=100
                            if 0<=a<=10:
                                self.medic_num=self.medic_num+1
                                print("Вы чудом создали аптечку!!")
                            elif 21<=a<=35:
                                self.pills=self.pills+1
                                print('Вам удалось изготовить таблетки!')
                            else:
                                a = random.randint(1,4)
                                if a ==1:
                                    print('Как бы вы не пытались у вас ничего не вышло, Вы плохи в медицине!!!')
                                if a ==2:
                                    print("Произошёл программный сбой и вам не удалось изготовить медикаменты. Зато, вы устранили неполадки в устройстве!")
                                if a==3:
                                    print("Вы не слишком уверены, но вполне вероятно, что вы смешали не те реагенты... Это явно нельзя использовать как лекарство...")
                                if a==4:
                                    print("Вы забыли куда положили лекарство...")
                            self.scripting()
                        else:
                            print('Вы слишком устали выпейте BlackBool или закончите день!')
                            self.scripting()
                    elif int(self.using) == 6:
                        print('Вы провели день в надежде на спасение')
                        self.energy=self.energy-random.randint(28, 48)
                        pass
                    elif int(self.using) == 7:
                        if self.coffe>0:
                            self.coffe=self.coffe-1
                            self.energy= self.energy - random.randint(50, 80)
                            self.health= self.health - random.randint(10, 20)
                            print('You drink BlackBool')
                            self.scripting()
                        else:
                            print('Not BlackBool')
                            self.scripting()
                    elif int(self.using) == 8:
                        if self.super_live > 0:
                            self.health = 100
                            self.food = 100
                            self.energy = 0
                            self.ills = 0
                        else:
                            print('Buy some things')
                        self.scripting()
                    elif int(self.using) == 0:
                        self.stats()
                        self.scripting()
                    else:
                        print('Не существует такого действия!\n')
                        self.scripting()
            except Exception:
                if self.using == 'give_super_live':
                    self.super_live = self.super_live + 1
                    print('Using Cheats')
                else:
                    print('Не существует такого действия!\n')
                self.scripting()

        def yslovia(self):
            if self.energy < 0:
                self.energy = 0
            if self.energy > 100:
                self.energy = 100
            if self.food < 40:
                self.ills += random.randint(3, 9)
            if self.ills > 40:
                self.health -= random.randint(4, 11)
                self.food = self.food - random.randint(2, 6)
            if self.ills > 100:
                self.ills = 100
            if self.ills < 0:
                self.ills = 0
            if self.food < 0:
                self.food = 0
            if self.food == 0:
                self.health -= random.randint(8, 12)
            if self.health <= 0:
                self.health = 0
            if self.health < 80:
                self.ills += 1
            if self.health>100:
                self.health=100

        def runing(self):
            while True:
                self.yslovia()
                self.day+=1
                save = random.randint(1, 100)
                if save == True:
                    print('Вас нашла спасательная группа!!!\n Вам удалось выжить, но вы не достигли нужного результата.\n  Может, когда-нибудь, вы захотите попробовать снова...\n  Но это уже другая история ;)\n Количество прожитых дней:{}\n\n\n\n'.format(self.day))
                    break
                if self.day == 100:
                    print('Поздравляем, вы стали героем не только Земли, но и всего космоса!\n Ваша поездка была записана и выдана в новом выпуске журнала: "Жизнь в космосе с нуля!".\n Количество прожитых дней:{}\n\n\n\n'.format(self.day))
                    break
                time.sleep(1)
                print('\nДень {}'.format(self.day))
                print("Событие:\n")
                self.events()
                if self.health <= 0:
                    self.health = 0
                    print('К сожалению, вы погибли!\n Вы не смогли выдержать нагрузки и впали в обморок.\n Ближайший комический патруль подобрал вас и вернул обратно на Землю, после оказания помощи.\n Вы получили этот бесценный жизненный опыт, который сможете использовать ещё раз...\n  Если вас снова допустят до полёта, конечно же...\n Количество прожитых дней:{}\n\n\n\n'.format(self.day))
                    break
                self.yslovia()
                print("\n Статистика:              Вещи:\nЗдоровье = {}             Консервы(+FOOD): {}"
                      "\nСытность = {}              Аптечка(+HP): {}\nЗаболевание = {}           Таблетки(-ILLS): {}\n"
                      "Усталость: {}            BlackBools: {}\n                    Полное востановление {}\n".format(self.health, self.food_num, self.food, self.medic_num, self.ills, self.pills, self.energy, self.coffe, self.super_live))
                time.sleep(1.9)
                self.scripting()
                self.food -= random.randint(8, 25)

def start():
    if __name__ == '__main__':
        app = Game()

while True:
    start_game = input('Выберите действие: \n 1.Start new game \n 2.Exit \n==>')
    try:
        if int(start_game) == 1:
            start()
        if int(start_game) == 2:
            print('Good bye!')
            break
    except ValueError:
        print('Выберите правильное действие\n')
        time.sleep(2)