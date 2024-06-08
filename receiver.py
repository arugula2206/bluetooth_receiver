import bluetooth
import time

PORT = 5  # ネット記事だとPORT=1と記述していることが多いですが、OSErrorが出ます！


def main():
    global PORT

    server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server.bind(('', PORT))
    server.listen(1)

    uuid = "00001101-0000-1000-8000-00805F9B34FB"
    bluetooth.advertise_service(
        server,
        "SampleServer",
        service_id=uuid,
        service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
        profiles=[bluetooth.SERIAL_PORT_PROFILE]
    )

    print("Waiting for connection on RFCOMM channel", PORT)
    sock, addr = server.accept()
    print(f'Accepted connection from {addr}')

    try:
        while True:
            print("Waiting for data...")
            data = sock.recv(1024)
            if not data:
                print("No data received, closing connection...")
                break
            print(f'Received: {data}')
            # 動作確認用に定期的にメッセージを表示
            time.sleep(1)  # 1秒待機
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        sock.close()
        server.close()
        print("Server closed")


if __name__ == '__main__':
    print("Starting Bluetooth server...")
    main()
    print("Bluetooth server stopped.")
