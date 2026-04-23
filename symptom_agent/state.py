import reflex as rx
from symptom_agent.agents import chat_agent
from symptom_agent.db.db_operations import fetch_messages


class GlobalState(rx.State):
    isPending: bool = False
    chat_messages: list[dict] = fetch_messages(thread_id="1")
    curr_message: dict = {}

    @rx.event
    async def handle_submit(self, formdata: dict):
        try:
            self.isPending = True
            ques = formdata.get("question")
            self.curr_message = {"question": ques, "answer": ""}
            yield

            res = await chat_agent(query=ques)
            self.curr_message.update({"answer": res})

        except Exception as e:
            print(e)
        finally:
            self.isPending = False

    @rx.var
    def get_messages(self) -> list[dict]:
        return self.chat_messages

    @rx.var
    def get_current_message(self) -> dict:
        return self.curr_message
