from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Header, Footer, Static, Button

QUESTION = "Do you want to learn about Textual CSS?"


class ExampleApp(App):
    CSS_PATH = "dom4.css"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Container(
            Static(QUESTION, classes="question"),
            Horizontal(
                Button("Yes", variant="success"),
                Button("No", variant="error"),
                classes="buttons",
            ),
            id="dialog",
        )


if __name__ == "__main__":
    app = ExampleApp()
    app.run()
