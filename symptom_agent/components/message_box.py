import reflex as rx


def message(data: dict) -> rx.Component:
    return rx.fragment(
        rx.card(
            rx.markdown(data["question"]),
            align_self="end",
            max_width="80%",
            class_name="py-0 px-3",
        ),
        rx.card(
            rx.markdown(data["answer"]),
            align_self="start",
            max_width="80%",
            class_name="py-0 px-3",
        ),
    )


def display_curr(data: dict, isPending: bool) -> rx.Component:
    return rx.fragment(
        rx.card(
            rx.markdown(data["question"]),
            align_self="end",
            max_width="80%",
            class_name="py-0 px-3",
        ),
        rx.cond(
            isPending,
            rx.skeleton(rx.text("Agent Thinking ...."), loading=False),
            rx.card(
                rx.markdown(data["answer"]),
                align_self="start",
                max_width="80%",
                class_name="py-0 px-3",
            ),
        ),
    )


def messages(
    chat_messages: list[dict], curr_message: dict, isPending: bool
) -> rx.Component:

    return rx.auto_scroll(
        rx.flex(
            rx.foreach(chat_messages, message),
            rx.cond(curr_message, display_curr(curr_message, isPending), ""),
            direction="column",
            spacing="3",
        ),
        padding="10px",
        type="scroll",
    )
