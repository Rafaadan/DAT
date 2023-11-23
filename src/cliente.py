import asyncio

async def send_text():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    while True:
        message = input("Ingrese un mensaje (o escriba 'exit' para salir): ")
        writer.write(message.encode())

        if message.lower() == 'exit':
            print("Cerrando la conexión con el servidor.")
            break

        data = await reader.read(100)
        response = data.decode()
        print(f"Recibido del servidor: {response}")

    writer.close()

asyncio.run(send_text())
