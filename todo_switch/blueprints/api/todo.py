from sanic import Blueprint, response
from sanic.views import HTTPMethodView
from sanic.exceptions import NotFound
from todo_switch.models import Task
from uuid import UUID


todo = Blueprint('todo_api', url_prefix='/todo')


class TodoView(HTTPMethodView):
    async def get(self, request):
        todos = await Task.query.gino.all()
        print({'todo_list': [todo.to_dict() for todo in todos]})
        return response.json({'todo_list': [todo.to_dict() for todo in todos]})

    async def post(self, request):
        data = request.json
        await Task.create(name=data['name'])
        return response.json({'result': 'OK'}, status=201)


@todo.route('/<todo_id>', methods=['DELETE'])
async def delete_todo(request, todo_id):
    try:
        todo_id = UUID(hex=todo_id)
    except ValueError:
        raise NotFound('Resource not found')
    await Task.delete.where(Task.id == todo_id).gino.status()
    return response.json({'result': 'OK'})


todo.add_route(TodoView.as_view(), '')
