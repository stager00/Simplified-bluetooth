import asyncio
from bleak import BleakScanner

phone_mac_address = "20:20:08:59:27:13"

async def find_phone():
    try:
        devices = await BleakScanner.discover()
        print("Devices found:", devices)
        for device in devices:
            print(f"Device: {device.name}, Address: {device.address}")
            if device.address == phone_mac_address:
                print("Phone detected!")
                return True
        print("Phone not detected.")
        return False
    except Exception as e:
        print(f"An error occurred during Bluetooth scanning: {e}")
        return False

async def main():
    while True:
        phone_detected = await find_phone()
        if phone_detected:
            print("Phone detected! Moving towards it.")
        else:
            print("Phone not detected. Scanning...")
        await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(main())
