"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from symptom_agent.components import action_input, messages
from symptom_agent.ui.sibar_ui import sidebar_bottom_profile
from symptom_agent.ui.nav_bar_ui import navbar_user
from symptom_agent.state import GlobalState


def index() -> rx.Component:

    chat_messages = GlobalState.get_messages
    curr_message = GlobalState.get_current_message
    isPending = GlobalState.isPending
    # Welcome Page (Index)
    return rx.box(
        rx.desktop_only(
            rx.flex(
                sidebar_bottom_profile(),
                rx.flex(
                    rx.cond(
                        chat_messages.length() | curr_message,
                        messages(chat_messages, curr_message, isPending),
                        rx.text(
                            "Get advice from the AI Agent for any medical symptom",
                            class_name="text-center",
                        ),
                    ),
                    action_input(isPending=isPending),
                    width="100%",
                    direction="column",
                    padding="10px",
                    height="100vh",
                    justify=rx.cond(
                        chat_messages.length() | curr_message, "between", "center"
                    ),
                ),
                spacing="3",
                height="100vh",
            )
        ),
        rx.mobile_and_tablet(
            rx.flex(
                navbar_user(),
                rx.flex(
                    rx.cond(
                        chat_messages.length() | curr_message,
                        messages(chat_messages, curr_message, isPending),
                        "",
                    ),
                    action_input(isPending=isPending),
                    direction="column",
                    padding="10px",
                    height="90%",
                ),
                direction="column",
                spacing="2",
                height="100vh",
            ),
            height="100vh",
        ),
        height="100vh",
    )


app = rx.App()
app.add_page(index)
