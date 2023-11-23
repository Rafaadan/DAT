import asyncio

async def handle_client(reader, writer):
    while True:
        data = await reader.read(100)
        message = data.decode()
        addr = writer.get_extra_info('peername')

        print(f"Received {message} from {addr}")

        if message.lower() == 'exit':
            print("Closing the connection")
            writer.close()
            await writer.wait_closed()
            break

        response = f"Received: {message}"
        writer.write(response.encode())
        await writer.drain()

async def main():
    server = await asyncio.start_server(
        handle_client, '127.0.0.1', 8888)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
