# ================================================================
# AI CYBER THREAT ANALYZER - COMPLETE SETUP GUIDE
# For absolute beginners. Follow EVERY step in order.
# ================================================================


## ============================================================
## DAY 1: INSTALL EVERYTHING (2-3 hours)
## ============================================================

### STEP 1: Install Python
--------------------------
1. Go to: https://www.python.org/downloads/
2. Click the big yellow "Download Python 3.12.x" button
3. Run the installer
4. ⚠️ VERY IMPORTANT: On the first screen, CHECK the box that says
   "Add Python to PATH" before clicking Install Now
5. Click "Install Now"
6. After install, open Command Prompt (search "cmd" in Windows Start)
7. Type this and press Enter:
      python --version
8. You should see: Python 3.12.x
   If you see this, Python is installed correctly ✅


### STEP 2: Install VS Code (Code Editor)
-----------------------------------------
1. Go to: https://code.visualstudio.com/
2. Click "Download for Windows" (or Mac)
3. Run the installer, keep clicking Next
4. VS Code is where you will write and read all your code


### STEP 3: Get Your Claude API Key (FREE)
-------------------------------------------
1. Go to: https://console.anthropic.com/
2. Click "Sign Up" — create a free account
3. After signing in, go to: https://console.anthropic.com/keys
4. Click "Create Key"
5. Give it a name like "college-project"
6. COPY the key that appears — it looks like: sk-ant-api03-xxxxx...
7. ⚠️ SAVE IT SOMEWHERE. You only see it once.
   Paste it in Notepad for now.


### STEP 4: Set Up Your Project Folder
---------------------------------------
1. Create a folder on your Desktop called "CyberThreatApp"
2. Copy all these files into that folder:
   - app.py
   - requirements.txt
   - static/ folder (with index.html inside)
   
Your folder should look like this:
   CyberThreatApp/
   ├── app.py
   ├── requirements.txt
   └── static/
       └── index.html


### STEP 5: Open Project in VS Code
-------------------------------------
1. Open VS Code
2. Click File → Open Folder
3. Select your "CyberThreatApp" folder
4. You should see your files in the left sidebar


### STEP 6: Open Terminal in VS Code
--------------------------------------
1. In VS Code, click Terminal → New Terminal (top menu)
2. A black panel appears at the bottom — this is your terminal
3. This is where you type commands to run your code


### STEP 7: Install Python Libraries
--------------------------------------
In the VS Code terminal, type this EXACTLY and press Enter:
   pip install flask flask-cors anthropic

Wait for it to finish. You'll see lots of text scrolling.
When it stops and shows your cursor again, it's done ✅


## ============================================================
## DAY 2: ADD YOUR API KEY AND RUN THE APP
## ============================================================

### STEP 8: Add Your API Key to the Code
-----------------------------------------
1. Open app.py in VS Code (click it in the left sidebar)
2. Find line 17 that says:
      client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY', 'your_api_key_here'))
3. Replace 'your_api_key_here' with your actual key:
      client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY', 'sk-ant-api03-YOUR-ACTUAL-KEY'))
4. Save the file: Ctrl+S


### STEP 9: Run The App!
--------------------------
In the VS Code terminal, type:
   python app.py

You should see:
   ==================================================
     Cyber Threat Analyzer is RUNNING!
     Open your browser and go to:
     http://localhost:5000
   ==================================================

If you see this → YOUR APP IS RUNNING! 🎉


### STEP 10: Open In Browser
------------------------------
1. Open Chrome or any browser
2. Type in the address bar: http://localhost:5000
3. Press Enter
4. You should see your beautiful CyberShield AI app!


### STEP 11: Test It!
----------------------
1. Click "→ Load sample phishing email" link
2. Click the blue "Analyze for Threats" button
3. Wait 5-10 seconds
4. You should see a red result card saying HIGH or CRITICAL threat!

If it works → CONGRATULATIONS! Your app is working! 🎉🎉


## ============================================================
## COMMON ERRORS AND HOW TO FIX THEM
## ============================================================

ERROR: "python is not recognized as a command"
FIX: Python was not added to PATH. Reinstall Python and check 
     the "Add Python to PATH" box.

ERROR: "ModuleNotFoundError: No module named 'flask'"
FIX: Run this again: pip install flask flask-cors anthropic

ERROR: "Address already in use"
FIX: Another program is using port 5000. Change the last line 
     in app.py from port=5000 to port=5001
     Then visit http://localhost:5001

ERROR: "Authentication error" or "Invalid API key"  
FIX: Your API key is wrong. Go back to console.anthropic.com,
     create a new key, and paste it correctly in app.py

ERROR: Page loads but Analyze button gives error
FIX: Make sure python app.py is still running in your terminal.
     If the terminal shows an error, read it and Google it.


## ============================================================
## DAY 6: DEPLOY YOUR APP ONLINE (So professors can see it)
## ============================================================

### Deploy to Render (Free Hosting)
1. Go to: https://github.com and create a free account
2. Create a new repository called "cyber-threat-analyzer"
3. Upload all your project files to GitHub
   (Search YouTube: "how to upload files to github" — 5 min video)
4. Go to: https://render.com and sign up with your GitHub account
5. Click "New" → "Web Service"
6. Connect your GitHub repository
7. Settings:
   - Build Command: pip install -r requirements.txt
   - Start Command: python app.py
8. Add Environment Variable:
   - Key: ANTHROPIC_API_KEY
   - Value: your actual API key
9. Click "Create Web Service"
10. Wait 3-5 minutes → You get a live URL like: 
    https://cyber-threat-analyzer.onrender.com


## ============================================================
## YOUTUBE VIDEOS TO WATCH (IN THIS ORDER)
## ============================================================

Search these EXACT terms on YouTube:

Day 1 (Before coding):
□ "Python installation tutorial for beginners 2024" (Watch first 10 min)
□ "VS Code setup for Python beginners" (Watch first 10 min)

Day 2 (Understanding what you built):  
□ "Flask Python tutorial for beginners" (Watch first 20 min)
□ "What is a REST API explained simply" (Watch any 5 min video)
□ "Anthropic Claude API Python tutorial" (Watch full video)

Day 5-6 (Making it pretty):
□ "Tailwind CSS crash course" by Traversy Media

Day 6 (Deploying):
□ "Deploy Flask app to Render free 2024"
□ "How to upload project to GitHub for beginners"


## ============================================================
## EXPLAINING THE CODE TO YOUR PROFESSOR
## ============================================================

If your professor asks "explain your code", say this:

"The project has two main parts:
1. The Frontend (index.html) - this is what users see in the browser.
   It has three tabs for email, URL, and log analysis. When the user
   clicks Analyze, it sends the input to our backend using a fetch API call.

2. The Backend (app.py) - this is a Python Flask server running on port 5000.
   It has three API endpoints: /analyze/email, /analyze/url, and /analyze/log.
   When it receives input, it constructs a specialized cybersecurity prompt
   and sends it to the Claude AI API using the Anthropic Python SDK.
   The AI returns a structured analysis which we send back to the frontend.

The key innovation is the prompt engineering - we designed specialized prompts
for each threat type that instruct the AI to analyze like a senior cybersecurity
analyst and return structured output with threat level, red flags, and recommendations."


## ============================================================
## PROJECT FILES OVERVIEW
## ============================================================

app.py          → The brain. Python Flask server. Handles all API calls.
requirements.txt → List of Python libraries your project needs.
static/index.html → The face. Everything users see and interact with.


## ============================================================
## NEED HELP?
## ============================================================

If you get stuck:
1. Copy the EXACT error message from your terminal
2. Paste it into Google
3. The first StackOverflow result almost always has the answer

Or ask Claude at claude.ai — paste your error and say
"I'm building a Flask app and got this error, how do I fix it?"
