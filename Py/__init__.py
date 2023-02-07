async def join(client):
    try:
        await client.join_chat("ZikaSupportGroup")
        await client.join_chat("heinoob")
    except BaseException:
        pass
