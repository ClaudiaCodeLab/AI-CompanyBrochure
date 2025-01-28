import json
from openai import OpenAI
from config import API_KEY, OLLAMA_API_URL, MODEL_NAME

openai_client = OpenAI(base_url=OLLAMA_API_URL, api_key=API_KEY)

def query_llm(messages, response_format="text"):
    response = openai_client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        response_format={"type": "json_object"} if response_format == "json" else None
    )
    return response.choices[0].message.content

def get_relevant_links(website):
    link_system_prompt = (
        "You are provided with a list of links found on a webpage. "
        "You are able to decide which of the links would be most relevant to include in a brochure about the company."
        "such as links to an About page, or a Company page, or Careers/Jobs pages."
        "Respond in JSON with full URLs as in this example:"
        """
        {
            "links": [
                {"type": "about page", "url": "https://full.url/goes/here/about"},
                {"type": "careers page": "url": "https://another.full.url/careers"}
            ]
        }
        """     
    )

    user_prompt = f"Here is the list of links on the website of {website.url} - "
    user_prompt += "please decide which of these are relevant web links for a brochure about the company, respond with the full https URL in JSON format. \
    Do not include Terms of Service, Privacy, email links.\n"
    user_prompt += "Links (some might be relative links):\n"
    user_prompt += "\n".join(website.links)

    messages = [
        {"role": "system", "content": link_system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    response = query_llm(messages, response_format="json")
    return json.loads(response)