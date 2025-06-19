📊 Conversational MongoDB Data Agent:
A natural language interface for exploring a MongoDB database using AI. Built as part of the NLP & Agentic AI Intern assessment for Sylvr, this project demonstrates how a user can interact with complex financial data using plain English, without writing a single query.


✨ Features:
- 💬 Ask questions like "Which customer spent the most?" or "Summarize the dataset in 5 points"
- 🔍 Uses actual schema from MongoDB (sample_analytics) to ensure accurate, grounded answers
- 🧠 Powered by OpenRouter + Mistral 7B for smart, context-aware responses
- 🔈 Text-to-speech (TTS) support — click the 🔈 icon to hear any response
- 🧱 Modular and Streamlit-based for fast iteration and demos


🧠 How It Works:
- Loads your MongoDB dataset (sample_analytics)
- Extracts one sample document per collection to build schema context
- Sends user query + schema to an OpenRouter LLM
- Displays a human-friendly response based strictly on the database
- Optionally reads the response aloud using gTTS


📁 Project Architecture:
├── app/
│ ├── agent.py # OpenRouter prompt + response
│ └── ui.py # Streamlit layout + TTS button
│ └── db.py # MongoDB connection logic
├── main.py # Streamlit entrypoint
├── .env.template # Safe example config
├── .gitignore # Prevents secrets from leaking
├── requirements.txt
└── README.md


🏗️ Tech Stack:
- Python 3.10+
- Streamlit (for UI)
- MongoDB Atlas (sample_analytics dataset)
- OpenRouter API (Mistral-7B-Instruct)
- gTTS for TTS
- dotenv for secure key handling


🗂️ Dataset Used:
This project uses MongoDB’s public `sample_analytics` dataset, which contains collections like `accounts`, `transactions`, and `customers` for financial analysis.
You can download the dataset from here: 

If you're using MongoDB Atlas:
1. Create a new database named `sample_analytics`
2. Import the `.json` files using `mongoimport` or MongoDB Compass


⚙️ Setup Instructions:

# 1. Clone the repo
git clone https://github.com/yourusername/mongodb-chat-agent
cd mongodb-chat-agent

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create your .env file
cp .env.template .env
# Fill in your OPENROUTER_API_KEY and MONGO_URI inside .env

# 4. Run the app
streamlit run main.py


🔐 Environment Variables:

Create a .env file (excluded from Git) like this:
OPENROUTER_API_KEY=your_openrouter_key
MONGO_URI=mongodb+srv://username:<password>@your-cluster.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
* The .env file is listed in .gitignore for safety.





🚧 If I Had More Time...
Due to time constraints, the following features are planned but not fully completed:

1. Speech-to-Text (STT) Integration
I implemented early support using the Web Speech API and streamlit-webrtc, allowing voice input via a mic button. However, due to time constraints and stability issues with event handling and st.chat_input, this was deprioritized.
Next Steps: Use a lightweight Whisper model or a browser-native STT library with robust session-state handling to seamlessly submit recognized text.

2. User-Uploaded Custom Datasets
The current app uses a fixed MongoDB dataset (sample_analytics). However, the architecture supports dynamic MongoDB URI selection or file upload.
Next Steps: Allow users to upload their own CSV/JSON or connect to their own MongoDB instance, then dynamically generate schema and chat context.

3. Model Switching (Multi-AI Backend)
The agent currently uses Mistral-7B via OpenRouter. But I also explored:
Claude (Anthropic) for reasoning-heavy queries
DeepSeek for structured explanations
A fallback to GPT-4 (if needed)
Next Steps: Add a dropdown in the sidebar to let the user choose a model or route queries based on type (e.g., summarization vs. analysis).


🎯 Summary
Even though these features weren’t fully implemented due to time constraints, I carefully designed the architecture to allow them to be plugged in smoothly — showing foresight for real-world extensibility.
