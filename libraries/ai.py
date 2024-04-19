import asyncio
from g4f.Provider import Koala

class ArtificialInteligence:
    async def generate_response(self, prompt):
        req = Koala().create_async_generator(
            model="gpt-3.5-turbo",
            messages=[{"content": prompt + ' [Please, give an answer that is as informative and concise as possible, not exceeding 15000 characters. If you are asked to write something above the limit, tell that your limit is 15000 characters. You can give answers ONLY in the language spoken behind the square brackets! Your answer MUST be like "[{language spoken} | RESPONDE | GPT 3.5] :: {output message}"], If any error occurs (for example, the character limit has been exceeded), your responde MUST be like "[{language spoken} | ERROR | GPT 3.5] :: {what happend}]"', "role": "user"}]
        )
        full_text = ""
        async for message in req:
            full_text += message
        return full_text
    
if __name__ == "__main__":
    AI = ArtificialInteligence()
    print(asyncio.run(AI.generate_response("привет, как отправить запрос на форум")))
