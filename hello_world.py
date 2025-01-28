from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fasthtml.common import Html, Head, Title, Script, Link, Body, Div, to_xml

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def default():
    content = Html(
        Head(
            Title("Some page"),
            Script(
                src="https://unpkg.com/htmx.org@2.0.1",
                integrity="sha384-QWGpdj554B4ETpJJC9z+ZHJcA/i59TyjxEPXiiUgN2WmTyV5OEZWCD6gQhgkdpB/",
                crossorigin="anonymous",
            ),
            Link(
                rel="stylesheet",
                href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css",
            ),
        ),
        Body(
            Div(
                "Click for a joke",
                cls="myclass",
                hx_get="random_joke",
            )
        ),
    )

    return to_xml(content)


@app.get("/random_joke")
def get_random_joke():
    joke = {
        "setup": "Why did the chicken cross the road?",
        "punchline": "To get to the other side!",
    }

    page = f"{joke['setup']} <br><br> {joke['punchline']} <br><br><hr> Click for more jokes..."

    return page
