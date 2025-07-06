\# 📦 webhook-repo



This repository is the \*\*Flask-based webhook server\*\* built for the TechStaX Developer Assessment. It listens for GitHub webhook events (Push, Pull Request, and Merge), stores them in \*\*MongoDB\*\*, and displays updates live in a minimal web UI that polls the backend every 15 seconds.



---



\## 🚀 Features



\- ✅ Receives \*\*GitHub webhook events\*\* (`push`, `pull\_request`)

\- ✅ Detects \*\*merge\*\* events from merged pull requests

\- ✅ Stores data in \*\*MongoDB\*\*

\- ✅ Minimalistic frontend that auto-updates every 15 seconds

\- ✅ Built with \*\*Flask\*\*, \*\*pymongo\*\*, \*\*JavaScript polling\*\*



---



\## 📁 Project Structure



webhook-repo/

├── app.py # Flask server

├── models.py # MongoDB connection

├── templates/

│ └── index.html # Frontend UI

├── static/

│ └── style.css # Styling for UI

├── .env # Environment variables (Mongo URI)

├── requirements.txt # Python dependencies


---



\## 📡 Webhook Endpoint


The server exposes:

POST /webhook


GitHub sends JSON payloads here, and the app handles:

\- Push events → `"author pushed to branch on timestamp"`

\- Pull request events → `"author submitted a pull request from ..."`

\- Merge events → `"author merged branch ..."`



---



\## 🧪 How to Run Locally



1\. \*\*Install Python packages\*\*:



```bash

pip install -r requirements.txt

Set up .env:



MONGO\_URI=mongodb://localhost:27017/webhookDB

Start MongoDB:


mongod --dbpath "C:\\data\\db"

Run Flask server:


python app.py

Open in browser:

👉 http://localhost:5000



🔗 Connect with GitHub

To test with real GitHub events:



Use ngrok to expose the Flask server:


ngrok http 5000

Copy the HTTPS link and add it as a webhook to your GitHub repo (action-repo):


Payload URL: https://<ngrok-id>.ngrok-free.app/webhook

Content type: application/json

Events: Push + Pull Request

📸 Sample Output


Punya pushed to main on 6 July 2025 - 12:34 PM UTC

Punya submitted a pull request from dev to main on 6 July 2025 - 12:40 PM UTC

👩‍💻 Built With
Flask
MongoDB
Ngrok
GitHub Webhooks

🧠 Author

Punya Shree T S
punyashree7.27@gmail.com


---


\### 📍 Step 3: Save and Close Notepad

After pasting → `Ctrl + S` to save → `Ctrl + W` to close



---



\### 📍 Step 4: Add, Commit \& Push to GitHub

In terminal:



```bash

git add README.md

git commit -m "Add README for webhook-repo"

git push origin main

✅ Done! Your repo is now complete and professional-looking.

