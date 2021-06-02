from titanic.models.dataset import Dataset
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score


class Service(object):

    dataset: object = Dataset()


    def new_model(self, payload) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)
        # △데이터 프레임 생성/ 기본데이터만 가지고 있는 상태로 훈련을 통해서 결과 예측해주길 기대하고 있음
    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis=1)

    @staticmethod
    def create_label(this):
        return this.train['Survived']

    @staticmethod
    def drop_feature(this, *feature) -> object: # *feature → 입력값을 전부 모아서 튜플로 만들어준다 /**feature - 딕셔너리 생성
        for i in feature:
            this.train = this.train.drop([i], axis=1)  # axis = 1  세로축 지워라/ 0 가로축을 지워라
            this.test = this.test.drop([i], axis=1)

        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        this.train = this.train.fillna({'Embarked': 'S'})
        this.test = this.test.fillna({'Embarked': 'S'})
        dictionary = {'S': 1, 'C': 2, 'Q': 3}
        this.train["Embarked"] = this.train["Embarked"].map(dictionary)
        this.test["Embarked"] = this.test["Embarked"].map(dictionary)
        return this

        # fillna({'Embarked':'S'}) 빈곤 계층이 S에서 많이 탔고, 이에 표검표를 안했을 확률이 높으므로  결측치는 S로 주기로한다
        # 왜 딕셔너리? pcalss = 키 / 어떤값은 비어있는 형태다 (NA) 이러면 에러가남 na가 있으면 fillna 해야함
        #train.csv 형태가 딕셔너리 형태이기떄문이다
        #map 함수로 사용하여 s : 1 c :2 q : 3


    @staticmethod
    def fare_ordinal(this) -> object:

        this.test['Fare'] = this.test['Fare'].fillna(1)
        print(f'9. >>>>>>>>>>>>>{this.test[this.test.isna().any(axis=1)]}') # 결측값이 무엇인지 보여주는 함수
        this.train['FareBand'] = pd.qcut(this.train['Fare'], 4)
        # quct 으로 bins 값 설정 {this.train["FareBand"].head(10)}
        # bins = list(pd.qcut(this.train['Fare'], 4, retbins=True))
        bins = [-1, 8, 15, 31, np.inf]
        this.train = this.train.drop(['FareBand'], axis=1)
        for these in this.train, this.test:
            these['FareBand'] = pd.cut(these['Fare'], bins=bins, labels=[1, 2, 3, 4])  # {[labels]:[bins]}
        this.test['FareBand'] = this.test['FareBand'].fillna(1)
        return this








    #요금을 구간별로 구분한다
    @staticmethod
    def fare_band_fill_na(this) -> object:
        return

    @staticmethod
    def title_norminal(this) -> object:
        combine = [this.train, this.test]
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
            # '([A-Za-z]+\. 정규표현식 (조건이 알파벳이라는 것) posix확장 문법 . expand . 앞에 있는 문자만 추출해라
        for dataset in combine:
            dataset['Title'] = dataset['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona'], 'Rare')
            dataset['Title'] = dataset['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal') #['Countess', 'Lady', 'Sir'] 이것들은 royal 족이기 떄문에 전체 reoyal로 변경
            dataset['Title'] = dataset['Title'].replace('Mlle', 'Mr')
            dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
            dataset['Title'] = dataset['Title'].replace('Mme', 'Rare')
            title_mapping = {'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}

            dataset['Title'] = dataset['Title'].fillna({'Title': 0})
            dataset['Title'] = dataset['Title'].map(title_mapping)


            #여러가지 신분 타입을 4가지로 통일 시키는 과정
        return this

    @staticmethod
    def gender_norminal(this) -> object:
        combine = [this.train, this.test]
        gender_mapping = {'male': 0, 'female': 1}
        for dataset in combine:
            dataset['Gender'] = dataset['Sex'].map(gender_mapping)
        return this

    @staticmethod
    def age_original(this) -> object:
        train = this.train
        test = this.test
        combine = [train, test]
        for dataset in combine:
            dataset['Age'] = dataset['Age'].fillna(-0.5)  # -1과 0 사이에 넣고 이건 unknown값 처리
            bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]  # 값이 아니고 구간 /  np.inf - 60세 이상 한꺼번에 묶기
            labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
            # train['AgeGroup'] 새로운 feature 만드는것 (편집하기 때문에 variable아니고 fesature임)
            dataset['AgeGroup'] = pd.cut(dataset['Age'], bins=bins, labels=labels)
            age_title_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2,'Teenager': 3, 'Student': 4, 'Young Adult': 5,
                                 'Adult': 6, 'Senior': 7}
            dataset['AgeGroup'] = dataset['AgeGroup'].map(age_title_mapping)

        return this
#사이킷런으로 문제를 풀게 만드는것
    @staticmethod
    def create_k_fold() -> object:
        return KFold(n_splits=10, shuffle=True, random_state=0)

    def accuracy_by_svm(self, this):
        score = cross_val_score(SVC(),
                                this.train,
                                this.label,
                                cv=KFold(n_splits=10,
                                         shuffle=True,
                                         random_state=0),
                                n_jobs=1,
                                scoring='accuracy')
        return round(np.mean(score) * 100, 2)











