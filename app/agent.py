import os
from pymongo.database import Database
import openai
from openai import OpenAI
from bson.json_util import dumps as bson_dumps
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

MODEL = "mistralai/mistral-7b-instruct:free"

global_db = None

def initialize_agent(db: Database):
    global global_db
    if db is not None:
        global_db = db
        print("Agent initialized with DB")
        return True
    else:
        print("Agent initialization failed: No DB provided")
        return False

def process_query(user_query: str) -> str:
    """
    Sends the user query to the OpenRouter LLM and returns both a MongoDB query and a natural-language answer.
    """
    if global_db is None:
        return "Database not initialized."

    try:
        schema = []
        for collection_name in global_db.list_collection_names():
            sample_doc = global_db[collection_name].find_one()
            if sample_doc:
                schema.append(f"{collection_name} → {bson_dumps(sample_doc, indent=2)}")
            else:
                schema.append(f"{collection_name} → [no documents]")

        schema_str = "\n\n".join(schema)

        prompt = f"""
        You are a smart data analyst working with a MongoDB finance database.

        Your job is to answer the user's question using the available data. Always respond with:
        1. A **clear and direct answer** to the user's question.
        2. A short explanation of how you arrived at that answer (if helpful).
        
        You can only answer questions based on the content available in the database.
        If the user asks something that is unrelated to the database or not supported by the data, politely say you cannot answer.
        Do NOT provide general information or facts from the internet or your own knowledge.
        
        Respond in natural, friendly, informative language.

        User: {user_query}
        Response:
        """

        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4
        )
        reply = response.choices[0].message.content.strip()

        return reply

    except Exception as e:
        return f"Error from OpenRouter: {str(e)}"
