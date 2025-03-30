import pyxdf
import matplotlib.pyplot as plt
import numpy as np
import glob
import os

# Get latest XDF file from the Release directory
recordings_dir = "C:/Synsensus/App-LabRecorder/build/Release"
files = glob.glob(f"{recordings_dir}/eeg_*.xdf")

if not files:
    print("No recordings found in", recordings_dir)
    print("Please run record_eeg.ps1 first to create a recording")
    exit()

latest_file = max(files, key=os.path.getctime)
print(f"Reading: {latest_file}")

# Read the XDF file
data, header = pyxdf.load_xdf(latest_file)
# Print stream info
for stream in data:
    print(f"Found stream: {stream['info']['name'][0]}")
    print(f"- Type: {stream['info']['type'][0]}")
    print(f"- Channel count: {len(stream['time_series'][0])}")
    print(f"- Sample count: {len(stream['time_series'])}")


# Get EEG data from first stream
eeg_data = data[0]['time_series']
timestamps = data[0]['time_stamps']
sample_rate = float(data[0]['info']['nominal_srate'][0])

# Create time axis in seconds
time_axis = np.arange(len(eeg_data)) / sample_rate

# Plot each EEG channel
plt.figure(figsize=(15, 8))
n_channels = eeg_data.shape[1]
for ch in range(n_channels):
    plt.subplot(n_channels, 1, ch+1)
    plt.plot(time_axis, eeg_data[:, ch], label=f'Channel {ch+1}')
    plt.ylabel(f'Ch {ch+1} (µV)')
    plt.legend()

# Plot the first few seconds of data
plt.figure()
plt.plot(data[0]['time_series'][:1000])
plt.title('First 1000 samples of EEG data')
plt.show() 


# Print basic stats
print(f"\nRecording length: {len(time_axis)/sample_rate:.2f} seconds")
print(f"Number of channels: {n_channels}")
print(f"Sampling rate: {sample_rate} Hz") 