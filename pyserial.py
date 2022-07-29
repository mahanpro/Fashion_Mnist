import serial
import numpy as np
import pandas as pd
import time


if __name__ == "__main__":
    # configure the serial connections (the parameters differs on the device you are connecting to)
    ser = serial.Serial(
        port='COM10',
        baudrate=115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=3)
    ser.isOpen()    # Open Serial
    out = ''
    time.sleep(2)
    if ser.inWaiting() > 0:
        while ser.inWaiting() > 0:
            out += str(ser.readline().decode("utf-8"))
        print(out)

    # Test Data
    test = pd.read_csv("fashion-mnist_test.csv")
    test_label = test.pop('label').to_numpy()
    test = test.to_numpy(dtype=int)

    for counter in range(0, 10):
        print(counter)
        send = bytearray(list(test[counter, :]))
        ser.write(send)
        time.sleep(0.5)
        out = ''
        if ser.inWaiting() > 0:
            while ser.inWaiting() > 0:
                out += str(ser.readline().decode("utf-8"))
            print(out)
        time.sleep(1)
