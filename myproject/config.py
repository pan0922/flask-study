import os

# SQLALCHEMY_DATABASE_URI는 데이터베이스 접속 주소
# SQLALCHEMY_TRACK_MODIFICATIONS는 SQLAlchemy의 이벤트를 처리하는 옵션

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False # pybo에 필요하지 않으므로 False 비활성화

# SQLALCHEMY_DATABASE_URI 설정에 의해 SQLite 데이터베이스가 사용되고 데이터베이스 파일은 프로젝트 홈 디렉터리 바로 밑에 pybo.db 파일로 저장
SECRET_KEY = "dev"