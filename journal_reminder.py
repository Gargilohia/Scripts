import os

def send_journal_reminder():
    message = "Take a moment to reflect and write in your journal!"
    title = "📖 Journal Reminder"
    os.system(f'''osascript -e 'display notification "{message}" with title "{title}"' ''')

send_journal_reminder()

print("Journal reminder script running... Press Ctrl+C to stop.")

