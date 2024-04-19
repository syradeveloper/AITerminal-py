import asyncio
from g4f.Provider import Liaobots

class ArtificialInteligence:
    async def generate_response(self, prompt):
        req = Liaobots().create_async_generator(
            model="claude-2.0",
            messages=[{"content": prompt + ' [Please, give an answer that is as informative and short as possible, not exceeding 15000 characters. If you are asked to write something above the limit, tell that your limit is 15000 characters. You can give answers ONLY in the language spoken behind the square brackets! Your answer MUST be like "[{language spoken} | claude-2.0] :: {output message}", If any error occurs (for example, the character limit has been exceeded), your responde MUST be like "[{language spoken} | ERROR | claude-2.0] :: {what happend}"]', "role": "user"}]
        )
        full_text = ""
        async for message in req:
            full_text += message
        return full_text

if __name__ == "__main__":
    AI = ArtificialInteligence()
    print(asyncio.run(AI.generate_response("привет, как отправить запрос на форум")))