"""The main Dashboard App."""

from rxconfig import config

import reflex as rx

from reflex_dashboard.styles import BACKGROUND_COLOR, FONT_FAMILY, THEME, STYLESHEETS

from reflex_dashboard.pages.tools import tools
from reflex_dashboard.pages.team import team
from reflex_dashboard.pages.index import index

# Create app instance and add index page.
app = rx.App(
    theme=THEME,
    stylesheets=STYLESHEETS,
)

app.add_page(index, route="/")
app.add_page(tools, route="/tools")
app.add_page(team, route="/team")
