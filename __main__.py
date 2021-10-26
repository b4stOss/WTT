from aiohttp import web
import aiofiles
import flask
from utils import get_top_100_cryptos

routes = web.RouteTableDef()

@routes.get('/result')
async def results(request):
    
    indicator = request.rel_url.query['indicator']

    if indicator != "RSI":
        period = int(request.rel_url.query['period'])
    else:
        period = 14

    resp = await get_top_100_cryptos(indicator, period)
    return web.Response(text=resp)

@routes.get("/")
async def index(request):
    
    async with aiofiles.open("templates/index.html", "r") as r:
        return web.Response(text=await r.read(), content_type='text/html')
    

app = web.Application()
app.add_routes(routes)
web.run_app(app)