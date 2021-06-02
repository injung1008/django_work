# ******************
# -----Data file-------
# ******************

class Data(object):
    ls = ['abcd', 786, 2.23, 'john', 70.2]
    tinyls = [123, 'john']
    tp = ('abcd', 786, 2.23, 'john', 70.2)
    tinytp = (123, 'john')
    dt = {'abcd': 786, 'john': 70.2}
    tinydt = {'홍': '30세'}

    def ls_create(self):
        self.ls.append(100)

    def ls_read(self):
        print(self.ls.pop())

    def ls_update(self):
        self.ls.extend(self.tinyls)

    def ls_delete(self):
        self.ls.remove(786)

    def tp_create(self):
        print('불가능')

    def tp_read(self):
        print(self.tp)

    def tp_merge(self):
        self.tp + self.tinytp
        print(self.tp)

    def tp_delete(self):
        print('불가능')

    def dt_create(self):
        self.dt['tom'] = 100

    def dt_read(self):
        print(self.dt)

    def dt_update(self):
         self.dt.update(self.tinydt)

    def dt_delete(self):
        del self.dt['abcd']
        print(self.dt)


    @staticmethod
    def main():

        while True:
            menu = int(input('0: exit\n '
                             'list : 1, creat, 2: read 3 :update, 4: delete \n'
                             'tuple : 5, creat, 6: read 7: update, 8: delete \n'
                             'dictionary : 9, creat, 10: read  11: update, 12: delete \n'))
            if menu == 0:
                break
            elif menu == 1:
                d = Data()
                print(d.ls_create())

            elif menu == 2:
                d.ls_read()

            elif menu == 3:
                d.ls_update()

            elif menu == 4:
                d.ls_delete()

            elif menu == 5:
                d.tp_create()

            elif menu == 6:
                d.tp_read()

            elif menu == 7:
                d.tp_update()

            elif menu == 8:
                d.tp_delete()

            elif menu == 9:
                d.dc_create()

            elif menu == 10:
                d.dc_read()

            elif menu == 11:
                d.dc_update()

            elif menu == 12:
                d.dc_delete()

            else:
                d.intinue()


Data.main()

''' def lst(self, l_add,l_read, l_extend,l_remove):

        self.l_add = ls.append(100)
        self.l_read = ls.pop()
        self.l_extend = ls.extend(tinyls)
        self.l_remove = ls.remove(786)

        ls = ['abcd', 786, 2.23, 'john', 70.2]
        tinyls = [123, 'john']

    def tp(self, t_add, t_read, t_extend, t_remove):
        self.t_add = lstp = list(tp)
                     lstp.append(100)
                     tp = tuple(lstp)
        self.t_read = tp3 = tp + tinytp print(tp3)
        self.t_extend =
        self.t_remove = tpdel = list(tp)
                        tpdel.remove(786)
                        tp = tuple(tpdel)


    def dic(self, d_add, d_read, d_extend, d_remove):
        self.d_add = dt['tom'] = 100
        self.d_read =
        self.d_extend = dt.update(tinydt)
        self.d_remove = del dt['abcd']
        '''






