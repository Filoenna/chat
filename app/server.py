import asyncio


async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info("peername")
    print("Received %r from %r" % (message, addr))

    print("Send: %r" % message)
    writer.write(data)
    await writer.drain()

    print("Close the client socket")
    writer.close()


async def serv():
    print("checktpoint 1")
    coro = await asyncio.start_server(handle_echo, "0.0.0.0", 8888)
    print("checktpoint 2")

    # Serve requests until Ctrl+C is pressed
    print("Serving on {}".format(coro.sockets[0].getsockname()))
    try:
        async with coro:
            await coro.serve_forever()
    except KeyboardInterrupt:
        pass


print("checktpoint 3")
asyncio.run(serv(), debug=True)
