from flask import Flask, render_template, request, jsonify
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os
from langchain_core.messages import SystemMessage, HumanMessage

os.environ["HF_HOME"] = 'D:/huggingface_cache'
# model_id= "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
llm = HuggingFacePipeline.from_model_id(
    model_id= "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature = 0.5,
        max_new_tokens = 100
    )
)

model = ChatHuggingFace(llm = llm)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.form.get("question")
    messages = [
        SystemMessage(content="Act like a helpful personal assistant"),
        HumanMessage(content=question)
    ]
    response = model.invoke(messages)
    answer = response.content.strip()
    return jsonify({"response": answer})

@app.route("/summarize", methods=["POST"])
def summarize():
    email_text = request.form.get("email")
    prompt = f"summarize the following email in 2-3 sentence: {email_text}"
    messages = [
        SystemMessage(content="Act like an expert email assistant"),
        HumanMessage(content=prompt)
    ]
    response = model.invoke(messages)
    summary = response.content.strip()
    return jsonify({"summary": summary})


if __name__ == "__main__" :
    app.run(debug=True)