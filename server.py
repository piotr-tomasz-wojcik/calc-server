from aiohttp import web
import queue
import copy
import json
import calculator

requests = queue.Queue()


async def get_history(_):
    _requests = copy.deepcopy(requests)
    return web.json_response(list(_requests.queue))


async def calculate(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == web.WSMsgType.text:
            try:
                equation = json.loads(msg.data)
                requests.put(equation)
                result = calculator.calculate(equation)
                code, payload = 200, result
            except json.JSONDecodeError:
                code, payload = 400, "Can't parse request"
            except calculator.InvalidEquation:
                code, payload = 400, "Invalid equation received"
            except Exception as e:
                code, payload = 500, f"Unexpected error {e}"
        else:
            code, payload = 404, 'Invalid message'

        await ws.send_json([code, payload])

    await ws.close()
    return ws


app = web.Application()
app.add_routes([web.get('/', get_history),
                web.post('/', calculate)])


if __name__ == '__main__':
    web.run_app(app)

