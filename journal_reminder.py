import time
import schedule
from plyer import notification

def send_journal_reminder():
    notification.notify(
        title="📖 Journal Reminder",
        message="Take a moment to reflect and write in your journal!",
        timeout=10
    )

# Schedule script to run every day at 4:10 AM
schedule.every().day.at("04:10").do(send_journal_reminder)

print("Journal reminder script running... Press Ctrl+C to stop.")

while True:
    schedule.run_pending()
    time.sleep(60)  
