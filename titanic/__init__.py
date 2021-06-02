from titanic.views.controller import Controller
from titanic.templetes.plot import Plot


if __name__ == '__main__':
    controller = Controller()


    while True:
        menu = int(input('0:exit, 1-data visualization \n'
                         ' 2:modeling\n'
                         ' 3: machine learning \n'
                         ' 4: machine release '))

        if menu == 0:
            break
        elif menu == 1:
            plot = Plot('train.csv')
            plot.draw_survived_dead()
            plot. draw_pclass()
            plot.draw_sex()
            plot.sex_draw()
            plot.draw_embarked()

        elif menu == 2:
            controller.modeling('train.csv','test.csv')

        elif menu == 3:
            controller.learning('train.csv','test.csv')

        elif menu == 4:
            controller.submit('train.csv','test.csv')

        else:
            print('오류')
            continue
