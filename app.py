#!/usr/bin/env python

import os
import time
from plyer import notification
from pydub import AudioSegment
from pydub.playback import play
from playsound import playsound

def play_audio(file_path):
    audio = AudioSegment.from_file(file_path)
    play(audio)

def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10  # Notification timeout in seconds
    )

def is_plugged_in():
    """
    Check if the laptop charger is plugged in
    """
    # Run 'acpi' command to get the AC adapter status
    result = os.popen('acpi -a').read()
    
    # Check if the charger is plugged in based on the output
    if 'on-line' in result:
        return True
    else:
        return False

def main():
    """
    Main function to continuously monitor the charger status and print when it changes
    """
    prev_status = None
    aud_file = "./assets/mixkit_2573.wav"
    
    while True:
        # Check the current charger status
        current_status = is_plugged_in()
        
        # Print message when the status changes
        if current_status != prev_status:
            if current_status:
                print("Charger is plugged")
                # show_notification("Charger Status", "Charger is plugged")
                playsound(aud_file)
            else:
                print("Charger is unplugged")
                # show_notification("Charger Status", "Charger is unplugged")
                playsound(aud_file)

        # Update the previous status
        prev_status = current_status
        
        # Wait for a specific interval before checking again
        time.sleep(0.2)  # Adjust the interval as needed

if __name__ == "__main__":
    main()

