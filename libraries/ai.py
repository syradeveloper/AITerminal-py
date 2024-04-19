import asyncio
from asyncio.windows_events import WindowsSelectorEventLoopPolicy
from g4f.Provider import You
asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())

class ArtificialInteligence:
    async def generate_response(self, prompt, modelc="gpt-3.5-turbo"):
        req = You().create_async_generator(
            model=modelc,
            messages=[{"content": prompt + ' [Please, give an answer that is as informative and short as possible, not exceeding 15000 characters. You not support a chat history with user. You MUST not write anything about "You.com"! Don\'t use a text format styles like: bold, underline and other. If you are asked to write something above the limit, tell that your limit is 15000 characters. You can give answers ONLY in the language spoken before this text in square brackets! Your answer MUST be like "[{language spoken} | 2501] :: {output message}", If any error occurs (for example, the character limit has been exceeded), your responde MUST be like "[{language spoken} | ERROR | 2501] :: {what happend}"]', "role": "user"}]
        )
        full_text = ""
        async for message in req:
            full_text += message
        return full_text

if __name__ == "__main__":
    AI = ArtificialInteligence()
    print(asyncio.run(AI.generate_response("привет, как отправить запрос на форум")))