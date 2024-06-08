import bluetooth

def connect_device(mac_address, port=5):
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    
    try:
        print(f"Trying to connect to {mac_address} on port {port}")
        sock.connect((mac_address, port))
        print(f"Connected to {mac_address} on port {port}")
        sock.close()
    except bluetooth.btcommon.BluetoothError as err:
        print(f"Failed to connect to {mac_address}: {err}")

if __name__ == '__main__':
    target_mac = "8C:52:19:6C:97:A1"  # 取得したMACアドレスをここに設定してください
    connect_device(target_mac)
