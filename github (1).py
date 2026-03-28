import streamlit as st
import difflib

# 1. Your Knowledge Base (Now with Harshit Shriniwas info)
knowledge_base = {
    "What are the best YouTube channels or online resources to learn Python?": 
        "Top YouTube channels include freeCodeCamp, Programming with Mosh, and Corey Schafer. For structured courses, try the University of Helsinki's MOOC or Harvard's CS50P.",
    "How do I fix an Indentation Error in my Python script?": 
        "Ensure all lines in a code block have the same number of spaces (usually 4). Most editors have a 'Convert Tabs to Spaces' feature to fix this instantly.",
    "Can you show me a simple example of a for loop?": 
        "Sure! Here is a simple loop:\nfruits = ['apple', 'banana', 'cherry']\nfor x in fruits:\n    print(x)",
    "Which framework (Django or Flask) is better for a beginner in web development?": 
        "Flask is lightweight and easier to learn first. Django is better if you want a 'batteries-included' framework with built-in admin panels and security.",
    "How can I transition from basic Python to AI/ML?": 
        "Master NumPy and Pandas for data handling first. Then, learn Scikit-learn for algorithms before moving into Deep Learning with TensorFlow or PyTorch.",
    "Which programming language should a first-year student start with?": 
        "Python is the most recommended starting language due to its simple syntax. However, C or C++ is great for understanding how computers manage memory.",
    "What are the essential steps to build a professional GitHub profile?": 
        "Upload a clear profile picture, write a concise bio, pin your best projects, and ensure every repository has a high-quality README file with instructions.",
    "How should I showcase my technical projects on a resume?": 
        "Use the STAR method (Situation, Task, Action, Result). Focus on the 'Action' (technologies used) and 'Result' (what the project actually achieved).",
    "When is the right time to start applying for technical internships?": 
        "The 'recruiting season' often starts 6-8 months before the internship begins. Start applying as soon as you have 1-2 solid projects to show.",
    "Can you suggest a unique Python project idea for my portfolio?": 
        "Try building a 'Personal Finance Dashboard' that reads your bank CSV files and categorizes spending automatically using basic data analysis.",
    
    # --- NEW QUESTIONS ADDED ---
    "Who made this site?": 
        "Harshit Shriniwas",
    "What does Harshit Shriniwas do?": 
        "He is a student in VIT BHOPAL and will graduate in the year 2029."
}

st.title("🤖 Harshit's AI Assistant")
st.write("Ask me about Python, Careers, or the creator of this site!")

# 2. Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Handle User Input
if prompt := st.chat_input("Ask me a question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Find best match (0.5 = 50% similarity required)
    matches = difflib.get_close_matches(prompt, knowledge_base.keys(), n=1, cutoff=0.5)
    
    if matches:
        best_match = matches[0]
        answer = knowledge_base[best_match]
        response = f"{answer}" 
    else:
        response = "I'm sorry, I couldn't find an answer to that in my database."

    with st.chat_message("assistant"):
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
