import bluetooth
import webbrowser

# Chromeのパスを指定
CHROME_PATH = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" %s'

def start_bluetooth_server():
    # Bluetoothサーバーのセットアップ
    server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_socket.bind(("", bluetooth.PORT_ANY))
    server_socket.listen(1)

    port = server_socket.getsockname()[1]

    # サーバーを知らせるためにサービスの登録
    bluetooth.advertise_service(server_socket, "BluetoothServer", 
                                service_id="00001101-0000-1000-8000-00805F9B34FB",
                                service_classes=["00001101-0000-1000-8000-00805F9B34FB", bluetooth.SERIAL_PORT_CLASS],
                                profiles=[bluetooth.SERIAL_PORT_PROFILE])

    print(f"Waiting for connection on RFCOMM channel {port}")

    client_socket, client_info = server_socket.accept()
    print(f"Accepted connection from {client_info}")

    # データの受信と処理
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            url = data.decode('utf-8')
            print(f"Received URL: {url}")
            webbrowser.get(CHROME_PATH).open(url)
            break  # URLを受け取って開いたらループを抜ける

    except OSError:
        pass

    print("Disconnected.")

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_bluetooth_server()
