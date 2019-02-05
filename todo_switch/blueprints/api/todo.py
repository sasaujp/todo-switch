from sanic import Blueprint, response
from sanic.views import HTTPMethodView
from todo_switch.models import Task

todo = Blueprint('todo_api', url_prefix='/todo')


class TodoView(HTTPMethodView):
    async def get(self, request):
        todos = await Task.query.gino.all()
        return response.json({'todo_list': [todo.to_dict() for todo in todos]})

    async def post(self, request):
        data = request.json
        await Task.create(name=data['name'])
        return response.json({'result': 'OK'}, status=201)


@todo.route('/<todo_id>', methods=['DELETE'])
async def delete_todo(request, todo_id):
    await Task.delete.where(Task.id == int(todo_id)).gino.status()
    return response.json({'result': 'OK'})


todo.add_route(TodoView.as_view(), '')
