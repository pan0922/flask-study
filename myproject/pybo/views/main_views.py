from flask import Blueprint,  url_for
from werkzeug.utils import redirect

# from pybo.models import Question

# __name__ --> main_views가 인수로 전달
# url_prefix는 라우팅 함수의 애너테이션 URL 앞에 기본으로 붙일 접두어 URL을 의미
# url_prefix='/main'이라고 입력했다면 hello_pybo 함수를 호출하는 URL은 localhost:5000/이 아니라 localhost:5000/main/이 됨
bp = Blueprint('main', __name__, url_prefix='/')

# localhost:5000/hello /hello에 매핑된 함수 호출
@bp.route('/hello') # /main/hello
def hello_pybo():
    return 'Hello, Pybo!'

# localhost:5000/ 에 접속하면 / 에 매핑된 함수 호출
# @bp.route('/')
# def index():
#     # 질문 목록 데이터
#     # order_by는 조회 결과를 정렬하는 함수
#     # order_by(Question.create_date.desc()) = 조회된 데이터를 작성일시 기준으로 역순으로 정렬
#     question_list = Question.query.order_by(Question.create_date.desc())
#     return render_template('question/question_list.html', question_list=question_list)
@bp.route('/') # /main/ main.index
def index():
    return redirect(url_for('question._list')) # url_for: 매핑 되어 있는 url리턴

# 즉 페이지를 불러 올 때 활용

# @bp.route('/detail/<int:question_id>/')
# def detail(question_id):
#     # question = Question.query.get(question_id)
#     question = Question.query.get_or_404(question_id)
#     return render_template('question/question_detail.html', question=question)
