from flaskext.markdown import Markdown
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData


import config

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()
# 플라스크 애플리케이션을 생성하는 코드
# # __name__에 모듈명이 담김 
def create_app():
# create_app 함수는 애플리케이션 펙토리
# 전역 변수로 db, migrate 객체를 만든 다음 create_app 함수 안에서 init_app 메서드를 이용해 app에 등록
    app = Flask(__name__)
    app.config.from_object(config) # config.py 파일에 작성한 항목을 읽음

    # ORM
    db.init_app(app) # init_app()메서드를 이용하여 app에 등록
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
    migrate.init_app(app, db)
    # db 객체를 create_app 함수 밖에서 생성하고, 앱에 등록 할 때 create_app함수에서 init_app함수를 통해 진행
    from . import models # 데이터 모델
    # 블루프린트
    from .views import main_views, question_views, answer_views, auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)
# URL과 플라스크 코드를 매핑하는 데코레이터
# / (URL)이 요청되면 플라스크 hello_pybo 함수 실행
    # @app.route('/')
    # def hello_pybo():
    #     return 'Hello, Pybo!'   # Hello Pybo! 를 출력
    
    # 필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime
    # markdown
    Markdown(app, extensions=['nl2br', 'fenced_code'])
    return app
    # jinja_env 환경 등록된 내용 중에서 datetime을 필터링 호출하여 format_datetime으로 설정