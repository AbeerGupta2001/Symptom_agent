import reflex as rx
from symptom_agent.state import GlobalState


def action_input(isPending: bool) -> rx.Component:
    return rx.box(
        rx.form(
            rx.hstack(
                rx.text_area(
                    placeholder="Enter your symptom here",
                    width="100%",
                    name="question",
                    required=True,
                ),
                rx.button("Send", type="submit", variant="outline", loading=isPending),
                align="center",
                justify="center",
                padding_x="10px",
            ),
            reset_on_submit=True,
            on_submit=GlobalState.handle_submit,
        ),
        width="100%",
    )
