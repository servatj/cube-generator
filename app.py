from sanic import Sanic
from sanic.response import json
from play import draw_cube
from sanic.response import text

app = Sanic(name='cube-generator')

@app.route("/number/<num:int>")
async def test(request, num):
    return text(draw_cube(num))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
