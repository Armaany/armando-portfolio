"""Smoke tests for the public portfolio application."""

from pathlib import Path

from streamlit.testing.v1 import AppTest


ROOT = Path(__file__).resolve().parents[1]


def test_portfolio_app_renders_without_errors():
    app = AppTest.from_file(str(ROOT / "streamlit_app.py")).run(timeout=20)

    assert not app.exception
    assert app.title or app.markdown


def test_portfolio_source_excludes_private_repository_and_client_links():
    source = (ROOT / "streamlit_app.py").read_text(encoding="utf-8").lower()

    # Construct sensitive identifiers so the guard itself cannot disclose them
    # if this repository's visibility is ever changed by mistake.
    product_prefix = "gov" + "risk"
    blocked = (
        "github.com/armaany/" + product_prefix,
        product_prefix + "-captool",
        product_prefix + "-scraper",
        "streamlit" + ".app",
        "docs" + ".google.com",
        "drive" + ".google.com",
    )
    assert all(value not in source for value in blocked)


def test_downloadable_portfolio_exists_and_is_a_pdf():
    pdf = ROOT / "portfolio" / "PORTFOLIO_ONE_PAGER.pdf"

    assert pdf.exists()
    assert pdf.read_bytes().startswith(b"%PDF")
