# gimme-active-developer
free script to get Discord's Active Developer Badge

This Python script will easily get you this funky badge 👍

## Prerequisites

1. Download the latest version of Python (https://www.python.org/downloads/)
2. Open Command Prompt and enter this command:
  pip install discord

## Actual tutorial
1. Go to https://discord.com/developers/applications and sign in
2. Create a new application (name doesn't matter)
3. Go to the Bot tab and give it a bot (click "Yes, do it" on the dialog box)
4. Scroll down and enable everything under the "Privileged Gateway Intents" (idk if this matters but just to be safe 🙂)
5. Click on the OAuth2/URL Generator tab
6. Under Scopes, select "bot" and "applications.commands" and under Bot Permissions, select "Administrator" (or if you're scared just "Send Messages")
7. Open Discord and create a new Discord server (keep the Developer Portal page **open**
8. Enable Community (for the last page don't bother with the first 2 options, but check everything else)
9. Go back to the Portal and copy the URL
10. Paste it in a **new** tab
11. Invite it to your new server
12. Download the "get-developer-badge.py" file provided
13. Open it in Python (or any IDE)
14. At the top, there is this line of code:
  token = "INSERT TOKEN HERE"
15. Go back into the Portal, go to the Bot tab and click on "Reset Token" (if you have 2FA enabled you need your phone)
16. Copy the token and replace it where it says "INSERT TOKEN HERE" (**KEEP THE QUOTATION MARKS**)
17. Run the code
18. Go into your server and run the /givemebadge command
19. Success! Now save this page (https://discord.com/developers/active-developer) and check every day :)
