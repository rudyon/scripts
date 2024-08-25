import os
from datetime import datetime

# Function to get battery percentage (for Linux systems)
def get_battery_status():
    battery_status = os.popen("upower -i $(upower -e | grep 'BAT') | grep 'percentage'").read().strip()
    return f"Battery: {battery_status}"

# Function to get the current time
def get_current_time():
    return f"Time: {datetime.now().strftime('%H:%M:%S')}"

# Function to get audio volume (requires `amixer`, available on Linux)
def get_audio_volume():
    try:
        volume = os.popen("amixer get Master | grep -o '[0-9]*%' | head -1").read().strip()
        return f"Audio Volume: {volume}"
    except:
        return "Audio Volume: Unable to retrieve"

# Function to run Neofetch
def run_neofetch():
    os.system("neowofetch")

# Main function
def main():
    print(get_battery_status())
    print(get_current_time())
    print(get_audio_volume())
    print()
    run_neofetch()

if __name__ == "__main__":
    main()

