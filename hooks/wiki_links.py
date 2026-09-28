"""MkDocs hook: convert Obsidian-style [[wiki-links]] to standard markdown links.

This runs at build time so the original markdown source files remain
untouched.  It builds a lookup from wiki-link text to the MkDocs
``use_directory_urls`` style relative URL (path/to/page/) and also
covers section-level aliases such as [[Empatisoi]] that do not match
an actual page heading but should navigate to the first page of that
section.
"""

import re

# Static mapping for wiki-link text -> relative URL (without leading slash).
# URLs follow the ``use_directory_urls: true`` convention, i.e. the .md
# extension is dropped and a trailing slash is added.
WIKI_MAP = {
    # --- 00_Perusteet ---
    "Design thinking perusteet": "00_Perusteet/Design_thinking_perusteet/",
    "Periaatteet ja ajattelutapa": "00_Perusteet/Periaatteet_ja_ajattelutapa/",
    "Prosessimallit": "00_Perusteet/Prosessimallit/",

    # --- 01_Empatisoi ---
    "Empatian merkitys": "01_Empatisoi/Empatian_merkitys/",
    "Empatisoinnin menetelmät": "01_Empatisoi/Empatisoinnin_menetelmat/",
    "Empatisoinnin työkalut": "01_Empatisoi/Empatisoinnin_tyokalut/",

    # --- 02_Maarittele ---
    "Tiedon synteesi ja analyysi": "02_Maarittele/Tiedon_synteesi_ja_analyysi/",
    "Ongelmalause": "02_Maarittele/Ongelmalause/",
    "Käyttäjätarpeet ja oivallukset": "02_Maarittele/Kayttajatarpeet_ja_oivallukset/",

    # --- 03_Ideoi ---
    "Divergentti ja konvergentti ajattelu": "03_Ideoi/Divergentti_ja_konvergentti_ajattelu/",
    "Ideoinnin menetelmät": "03_Ideoi/Ideoinnin_menetelmat/",
    "Ideoiden valinta ja priorisointi": "03_Ideoi/Ideoiden_valinta_ja_priorisointi/",

    # --- 04_Prototypoi ---
    "Prototypoinnin periaatteet": "04_Prototypoi/Prototypoinnin_periaatteet/",
    "Prototyyppien tyypit ja tarkkuustasot": "04_Prototypoi/Prototyyppien_tyypit_ja_tarkkuustasot/",
    "Prototypoinnin menetelmät": "04_Prototypoi/Prototypoinnin_menetelmat/",

    # --- 05_Testaa ---
    "Käyttäjätestauksen periaatteet": "05_Testaa/Kayttajatestauksen_periaatteet/",
    "Palautteen kerääminen ja analysointi": "05_Testaa/Palautteen_keraaminen_ja_analysointi/",
    "Iterointi": "05_Testaa/Iterointi/",

    # --- 06_Yhteenveto ---
    "Menetelmät ja työkalut -taulukko": "06_Yhteenveto/Menetelmat_ja_tyokalut_taulukko/",
    "Käsitteet ja sanasto": "06_Yhteenveto/Kasitteet_ja_sanasto/",
    "Prosessin tiivistelmä (yksi sivu)": "06_Yhteenveto/Prosessin_tiivistelma/",

    # --- Section-level aliases (wiki-link text is the section name, not a page heading ---
    # These point to the first page in each section.
    "Empatisoi": "01_Empatisoi/Empatian_merkitys/",
    "Määrittele": "02_Maarittele/Tiedon_synteesi_ja_analyysi/",
    "Ideoi": "03_Ideoi/Divergentti_ja_konvergentti_ajattelu/",
    "Prototypoi": "04_Prototypoi/Prototypoinnin_periaatteet/",
    "Testaa": "05_Testaa/Kayttajatestauksen_periaatteet/",
}


def on_page_markdown(markdown, *, page, config, files):
    """Replace [[wiki-link]] syntax with standard markdown links.

    Parameters
    ----------
    markdown : str
        The raw markdown source of the page being rendered.
    page : mkdocs.structure.pages.Page
        The page object for which the markdown is being rendered.
    config : mkdocs.config.defaults.MkDocsConfig
        The global configuration.
    files : mkdocs.structure.files.Files
        The global file collection.

    Returns
    -------
    str
        Markdown with all ``[[...]]`` expressions converted.
    """
    def _replace(match):
        title = match.group(1)
        url = WIKI_MAP.get(title)
        if url is None:
            # Unresolved wiki-link: leave it unchanged so it is visible.
            return match.group(0)
        return f"[{title}]({url})"

    return re.sub(r"\[\[([^\[\]]+)\]\]", _replace, markdown)
