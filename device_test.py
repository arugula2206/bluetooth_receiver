import bluetooth


def main():
    for addr, name in bluetooth.discover_devices(lookup_names=True):
        print(f'{addr} - {name}')


if __name__ == '__main__':
    main()
