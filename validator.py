import os, requests
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def score(url):
    resp = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role":"system","content":"You are an API valuation expert."},
            {"role":"user","content":f"Score monetization potential for this endpoint: {url}"}
        ]
    )
    print(resp.choices[0].message.content)

if __name__=="__main__":
    score(os.getenv("TEST_URL","https://api.example.com/data"))
