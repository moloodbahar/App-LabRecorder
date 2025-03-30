from pylsl import StreamInfo, StreamOutlet
import numpy as np
import time

# Create a new stream info with simple name
info = StreamInfo(
    name='TestStream',          # Simple name that matches what LabRecorder sees
    type='EEG',
    channel_count=4,
    nominal_srate=256,
    channel_format='float32',
    source_id='myuid12345'
)

# Create an outlet to broadcast the stream
outlet = StreamOutlet(info)

# Send data forever
print(f"Now sending data as {info.name()}...")
while True:
    # Create random data to simulate 4 EEG channels
    mysample = np.random.rand(4)
    outlet.push_sample(mysample)
    time.sleep(1/256)  # Match Muse's sampling rate 