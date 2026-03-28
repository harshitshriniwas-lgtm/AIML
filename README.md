# AIML:

🤖 Harshit’s AI Assistant

A simple AI-powered chatbot built using Streamlit that answers questions about Python, careers, and basic guidance using a predefined knowledge base.

🚀 Features
💬 Interactive chat interface using Streamlit
📚 Predefined knowledge base for quick responses
🔍 Smart matching using difflib (fuzzy matching)
🧠 Maintains chat history during the session
🎯 Beginner-friendly project
🛠️ Tech Stack
Python
Streamlit
difflib (for approximate string matching)
📂 Project Structure
📁 project-folder
│── app.py          # Main Streamlit application
│── README.md       # Project documentation
▶️ How to Run
1. Install dependencies
pip install streamlit
2. Run the app
streamlit run app.py
3. Open in browser

Streamlit will automatically open:

http://localhost:8501
💡 How It Works
User enters a question in the chat input.

The app searches for the closest matching question using:

difflib.get_close_matches()
If a match is found → returns the stored answer.
If no match → shows a fallback response.
📊 Example Questions
What are the best YouTube channels to learn Python?
How do I fix an Indentation Error?
Which framework is better: Django or Flask?
Who made this site?
👨‍💻 Creator

Harshit Shriniwas

Student at VIT Bhopal
Expected Graduation: 2029
🔮 Future Improvements
Integrate real AI models (like OpenAI API)
Add more dynamic knowledge base (database or API)
Improve UI/UX
Add voice input/output
⭐ Contribute

Feel free to fork this project and improve it!

📜 License

This project is open-source and free to use.
