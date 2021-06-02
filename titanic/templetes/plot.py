from titanic.models.dataset import Dataset
from titanic.models.service import Service
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns
rc('font', family = font_manager.FontProperties(fname='C:/Windows/Fonts/H2GTRE.ttf').get_name())

class Plot(object):

    dataset = Dataset()
    service = Service()

    def __init__(self, fname) :

        self.entity = self.service.new_model(fname)

    def draw_survived_dead(self):
        this = self.entity
        f, ax = plt.subplots(1,2, figsize = (18,8))
        this['Survived'].value_counts().plot.pie(explode=[0,0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        ax[0].set_title('0:사망자 vs 1.생존자')
        ax[0].set_ylabel('')
        ax[1].set_title('0:사망자 vs 1.생존자')
        sns.countplot('Survived', data=this, ax=ax[1])
        plt.show()

#객실 등급별로 사망
    def draw_pclass(self):
        this = self.entity #원본데이터는 건들지 않고 복사해서 사용하는 의미
        this['Survived'].value_counts()
        this['Survived(humanized)'] = this['Survived'].replace(0, 'Perish').replace(1, 'Survived')
        this['Pclass(humanized)'] = this['Pclass'].replace(1, '1등석').replace(2, '2등석').replace(3, '3등석')
        sns.countplot(data=this, x='Pclass(humanized)', hue='Survived(humanized)')
        plt.show()
#성별
    def draw_sex(self):
        this = self.entity
        this['Survived'].value_counts()
        this['Survived(humanized)'] = this['Survived'].replace(0, 'Perish').replace(1, 'Survived')
        this['Sex'] = this['Sex'].replace(0, 'male').replace(1, 'female')
        sns.countplot(data=this, x='Sex', hue='Survived(humanized)')
        plt.show()
#성별 원형 차트 버전
    def sex_draw(self):
        this = self.entity
        f, ax = plt.subplots(1,2, figsize = (18,8))
        this['Survived'][this['Sex'] == 'male'].value_counts().plot.pie(explode=[0,0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        this['Survived'][this['Sex'] == 'female'].value_counts().plot.pie(explode=[0,0.1], autopct='%1.1f%%', ax=ax[1], shadow=True)
        ax[0].set_title('0:사망자 vs 1.생존자')
        ax[1].set_title('0:사망자 vs 1.생존자')
        plt.show()

#탑승지
    def draw_embarked(self):
        this = self.entity
        this['Survived'].value_counts()
        this['Survived(humanized)'] = this['Survived'].replace(0, 'Perish').replace(1, 'Survived')
        this['Embarked(humanized)'] = this['Embarked'].replace('C', 'Cherbourg').replace('S', 'Southampton').replace('Q','Queenstown')
        sns.countplot(data=this, x='Embarked(humanized)', hue='Survived(humanized)')
        plt.show()






        #print(f'Train의 Type 은 {type(this)}이다.')
        #print(f'Train의 column 은 {this.columns}이다.')
        #print(f'Train의 상위 5개 데이터는 {this.head}이다.')
        #print(f'Train의 하위 5개 데이터는 {this.tail}이다.')



'''
Train의 Type 은 <class 'pandas.core.frame.DataFrame'>
Train의 column 은 Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
       'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
      dtype='object')이다.
Train의 상위 5개 데이터는 <bound method NDFrame.head of      PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0              1         0       3  ...   7.2500   NaN         S
1              2         1       1  ...  71.2833   C85         C
2              3         1       3  ...   7.9250   NaN         S
3              4         1       1  ...  53.1000  C123         S
4              5         0       3  ...   8.0500   NaN         S
..           ...       ...     ...  ...      ...   ...       ...
886          887         0       2  ...  13.0000   NaN         S
887          888         1       1  ...  30.0000   B42         S
888          889         0       3  ...  23.4500   NaN         S
889          890         1       1  ...  30.0000  C148         C
890          891         0       3  ...   7.7500   NaN         Q

[891 rows x 12 columns]>이다.
Train의 하위 5개 데이터는 <bound method NDFrame.tail of      PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0              1         0       3  ...   7.2500   NaN         S
1              2         1       1  ...  71.2833   C85         C
2              3         1       3  ...   7.9250   NaN         S
3              4         1       1  ...  53.1000  C123         S
4              5         0       3  ...   8.0500   NaN         S
..           ...       ...     ...  ...      ...   ...       ...
886          887         0       2  ...  13.0000   NaN         S
887          888         1       1  ...  30.0000   B42         S
888          889         0       3  ...  23.4500   NaN         S
889          890         1       1  ...  30.0000  C148         C
890          891         0       3  ...   7.7500   NaN         Q
'''






