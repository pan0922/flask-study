#해당 코드 파일은 __init__의 SQLAlchemy() 함수를 통해 데이터를 불러 올 수 있는 데이터 모델 파일

# db는 __init__.py의 db = SQLAlchemy()
# DB 공부 필요

from pybo import db

# db.Column() 괄호 안의 첫 번째 인수는 데이터 타입을 의미
# 데이터 타입은 속성에 저장할 데이터의 종류를 결정

# db.Integer는 고유 번호와 같은 숫자값에 사용

# db.String은 제목처럼 글자 수가 제한된 텍스트에 사용

# 글 내용처럼 글자 수를 제한할 수 없는 텍스트는 db.Text를 사용

# db.Column에는 데이터 타입 외에 다음과 같은 속성을 추가로 설정할수 있음

# n:n관계의 테이블 생성 user_id:question_id 관계, 중복된 관계는 있을 수 없음
question_voter = db.Table(
    'question_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('question_id', db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'), primary_key=True)
)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('question_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)
   # 추천인 데이터는 question_voter 테이블에 저장됨, 추천인 정보는 voter로 참조 가능
   # 어떤 계정이 a_user 라는 객체로 참조되었다면 a_user.question_voter_set 으로 해당 계정이 추천한 질문 리스트를 구할수 있음
    voter = db.relationship('User', secondary=question_voter, backref=db.backref('question_voter_set'))    

answer_voter = db.Table(
    'answer_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('answer_id', db.Integer, db.ForeignKey('answer.id', ondelete='CASCADE'), primary_key=True)
)
# primary_key: 데이터베이스에서 중복된 값을 가질 수 없게 만들기 위해 기본키로 설정

# nullable: 속성에 빈값을 허용할지 여부
# --------------------------------------------------------------------------------------------

# 답변 모델에서 id와 content, create_date 속성은 질문 모델의 id, content, create_date와 의미와 목적이 같음

# question_id: 답변과 질문을 연결하기 위한 속성
# 답변은 어떤 질문에 대한 답변인지 알아야 하므로 질문의 id 속성이 필요

# 데이터베이스에서는 기존 모델과 연결된 속성을 외부 키(foreign key)라고 함
# 모델을 서로 연결할 때에는 위와 같이 db.ForeignKey를 사용

# db.ForeignKey의 첫 번째 파라미터 'question.id'는 question 테이블의 id 컬럼을 의미
# Answer 모델의 question_id 속성은 question 테이블의 id 컬럼과 연결됨
# ondelete는 삭제 연동 설정이다. 즉, ondelete='CASCADE'는 질문을 삭제하면 해당 질문에 달린 답변도 함께 삭제

# question 속성을 생성하면 답변 모델에서 연결된 질문 모델의 제목을 answer.question.subject처럼 참조
# 첫 번째 파라미터는 참조할 모델명
# 두 번째 backref 파라미터는 역참조 설정
# 역참조: 질문에서 답변을 거꾸로 참조하는 것을 의미
# a_question이라면 a_question.answer_set와 같은 코드로 해당 질문에 달린 답변들을 참조

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set',cascade='all, delete-orphan'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('answer_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)
    voter = db.relationship('User', secondary=answer_voter, backref=db.backref('answer_voter_set'))
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
# 이렇게 짜여진 테이블은 SQLite에서 테이블을 볼 수 있음

