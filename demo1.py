import time
import tidevice
from tidevice._perf import DataType

t = tidevice.Device()
print(t)
perf = tidevice.Performance(t, [DataType.CPU, DataType.MEMORY, DataType.NETWORK, DataType.FPS, DataType.PAGE, DataType.SCREENSHOT, DataType.GPU])
# tidevice version <= 0.4.16:
# perf = tidevice.Performance(t)

def callback(_type: tidevice.DataType, value: dict):
    print("R:", _type.value, value)


perf.start("com.gpower.filtoDevelopment", callback=callback)
time.sleep(10)
# perf.stop()