from pylsl import resolve_streams
import time

print("Looking for streams...")
streams = resolve_streams()
for stream in streams:
    print(f"Found stream: {stream.name()} ({stream.type()})") 