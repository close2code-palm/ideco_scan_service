from aiohttp import web
from aiohttp.abc import Application
from aiohttp.test_utils import AioHTTPTestCase

from sswa.rest_api_handlers import runable_app, process_scan


class ScannerPointTestCase(AioHTTPTestCase):

    async def get_application(self) -> Application:
        app = web.Application()
        app.add_routes([web.get(
            r'/scan/{ip}/{begin_port:\d+}/{end_port:\d+}', process_scan)])
        return app

    async def test_scan_res(self):
        async with self.client.request('GET', '/scan/127.0.0.1/5430/5435') as resp:  # dummy host
            self.assertEqual(resp.status, 200)
            answer = await resp.json()
        self.assertIn({'port': '5433', 'state': 'open'}, answer, )

    async def test_scan_fail(self):
        async with self.client.request('GET', '/scan/127.0.0.1/65555/65666') as response:
            self.assertEqual(response.status, 400)
            response = await response.text()
            self.assertIn('Bad', response)
