import pandas as pd

from titanic.models.service import Service
from titanic.models.dataset import Dataset
from sklearn.ensemble import RandomForestClassifier
#랜덤포레스트 모델을 불러와서 학습 모델을 형성


class Controller(object):
    dataset = Dataset()
    service = Service()

    def modeling(self, train, test) -> object:
        service = self.service # self는 클래스를 뜻함
        this = self.preprocess(train, test)
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        return this # this는 데이터 프레임

    def learning(self, train, test) -> object:
        this = self.modeling(train, test)
        print(f'사이킥런의 SVC 알고리즘 정확도 {self.service.accuracy_by_svm(this)} % ')

    def submit(self, train, test):
        this = self.modeling(train, test)
        clf = RandomForestClassifier()
        clf.fit(this.train, this.label)
        prediction = clf.predict(this.test)
        pd.DataFrame({'PassengerId' : this.id, 'Survived': prediction}).to_csv('./data/submission.csv', index=False)



    def preprocess(self, train, test) -> object:
        service = self.service
        this = self.dataset
        #초기모델 생성
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        this.id = this.test['PassengerId']
        #norminal ordinal 로 정형화
        this = service.embarked_nominal(this)
        this = service.title_norminal(this)
        this = service.gender_norminal(this)
        this = service.fare_ordinal(this)
        # 불필요한 feature  제거
        this = service.age_original(this)
        this = service.drop_feature(this, 'Name', 'Sex', 'Age', 'Cabin', 'Ticket', 'Fare')
        self.print_this(this)

        return this

    @staticmethod
    def print_this(this):
        print('*' * 100)
        print(f'1.Train의 Type 은 \n {type(this.train)}이다.')
        print(f'2.Train의 column 은  \n  {this.train.columns}이다.')
        print(f'3.Train의 상위 1개 데이터는  \n  {this.train.head()}이다.')
        print(f'4.Train의 null의 갯수  \n  {this.train.isnull().sum()}개') #null인것의 합을 보여줌
        print(f'5.test의 type은  \n {type(this.test)}')
        print(f'6.test의 column은  \n {this.test.columns} 이다')
        print(f'7.Test의 상위 1개 데이터는  \n {this.test.head()}이다.')
        print(f'8.Test 의 null의 갯수  \n {this.test.isnull().sum()}개')


        print('*' * 100)





