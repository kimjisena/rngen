from dotenv import load_dotenv
import os
import openai

load_dotenv()

def get_release_note(markdown_string = ''):
    postfix = '\nI want you to generate release notes for the feature in the following format:\n\n**[Feature in titlecase]**\n\n\t- [Acceptance criteria in two words]: [Brief description of acceptance criterion starting with "User can now..." or "We have..."]\n\nNote: The feature has already been implemented and all acceptance criteria have been checked and they pass\n'
    prompt = markdown_string + postfix
    print(prompt)
    api_key = os.environ.get("OPENAI_API_KEY")
    openai.api_key = api_key
    

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.52,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text
