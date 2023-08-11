import os
import openai
import dotenv

dotenv.load_dotenv()

## Must Read The Guide - https://docs.metaphor.systems/reference/prompting-guide

openai.api_key = os.getenv("OPENAI_API_KEY")

USER_QUESTION = "What's the recent news on physics today?"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": USER_QUESTION},
    ],
)

print(completion.choices[0].message.content)
'''
As of today, some recent news in the field of physics includes the following:

1. NASA's Perseverance rover successfully landed on Mars on February 18, 2021. Its mission includes studying Martian geology, searching for signs of ancient life, and collecting rock samples for potential return to Earth.

2. The Large Hadron Collider (LHC) at CERN has entered a two-year shutdown phase for upgrades and maintenance. The LHC is the most powerful particle accelerator in the world and has made significant contributions to the field of particle physics.

3. Researchers at MIT have developed a new method to produce high-temperature superconductors, which may significantly impact various industries, from energy transmission to transportation.

4. Scientists have discovered a new state of matter called time crystals. These are systems that break time symmetry and exhibit spontaneous time-translation symmetry breaking.

5. The first-ever image of a black hole was captured in 2019 using the Event Horizon Telescope (EHT). Since then, further analysis of the data has allowed researchers to better understand the magnetic fields surrounding black holes, furthering our knowledge of these mysterious objects.

Remember, news in the field of physics is constantly evolving, so it's always a good idea to keep an eye on reliable sources for the most up-to-date information.
'''
