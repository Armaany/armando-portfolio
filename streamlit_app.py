"""Public, anonymized portfolio for Armando Elizalde."""

from pathlib import Path

import streamlit as st


ROOT = Path(__file__).resolve().parent
PORTFOLIO_PDF = ROOT / "portfolio" / "PORTFOLIO_ONE_PAGER.pdf"


st.set_page_config(
    page_title="Armando Elizalde | AI-Assisted MVP Delivery",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="collapsed",
)


st.markdown(
    """
    <style>
      :root {
        --ink: #162338;
        --muted: #5f6f82;
        --blue: #185adb;
        --blue-soft: #eef4ff;
        --teal: #0f766e;
        --line: #dce4ee;
        --paper: #ffffff;
      }

      .stApp {
        background:
          radial-gradient(circle at 82% 2%, rgba(24, 90, 219, 0.10), transparent 28rem),
          linear-gradient(180deg, #f8fbff 0%, #ffffff 36rem);
      }

      .block-container {
        max-width: 1120px;
        padding-top: 2.2rem;
        padding-bottom: 4rem;
      }

      .eyebrow {
        color: var(--blue);
        font-size: 0.78rem;
        font-weight: 750;
        letter-spacing: 0.12em;
        margin-bottom: 0.8rem;
        text-transform: uppercase;
      }

      .hero-title {
        color: var(--ink);
        font-size: clamp(2.35rem, 6vw, 4.6rem);
        font-weight: 780;
        letter-spacing: -0.045em;
        line-height: 0.98;
        margin: 0;
        max-width: 900px;
      }

      .hero-subtitle {
        color: var(--muted);
        font-size: 1.18rem;
        line-height: 1.7;
        margin: 1.4rem 0 0;
        max-width: 820px;
      }

      .availability {
        align-items: center;
        color: var(--teal);
        display: flex;
        font-size: 0.95rem;
        font-weight: 650;
        gap: 0.55rem;
        margin-top: 1.3rem;
      }

      .availability-dot {
        background: #20a88b;
        border-radius: 99px;
        box-shadow: 0 0 0 5px rgba(32, 168, 139, 0.12);
        display: inline-block;
        height: 0.58rem;
        width: 0.58rem;
      }

      .section-kicker {
        color: var(--blue);
        font-size: 0.76rem;
        font-weight: 750;
        letter-spacing: 0.11em;
        margin: 3.6rem 0 0.45rem;
        text-transform: uppercase;
      }

      .section-title {
        color: var(--ink);
        font-size: 2rem;
        font-weight: 740;
        letter-spacing: -0.025em;
        line-height: 1.15;
        margin: 0 0 1.25rem;
      }

      .card {
        background: rgba(255, 255, 255, 0.88);
        border: 1px solid var(--line);
        border-radius: 18px;
        box-shadow: 0 14px 40px rgba(34, 56, 88, 0.055);
        height: 100%;
        padding: 1.35rem 1.4rem;
      }

      .card-label {
        color: var(--blue);
        font-size: 0.74rem;
        font-weight: 750;
        letter-spacing: 0.09em;
        margin-bottom: 0.55rem;
        text-transform: uppercase;
      }

      .card h3 {
        color: var(--ink);
        font-size: 1.16rem;
        margin: 0 0 0.55rem;
      }

      .card p {
        color: var(--muted);
        line-height: 1.58;
        margin: 0;
      }

      .flow {
        align-items: stretch;
        display: grid;
        gap: 0.7rem;
        grid-template-columns: repeat(5, 1fr);
        margin: 1.2rem 0 0;
      }

      .flow-step {
        background: var(--paper);
        border: 1px solid var(--line);
        border-radius: 14px;
        color: var(--ink);
        font-size: 0.91rem;
        font-weight: 650;
        line-height: 1.35;
        min-height: 7rem;
        padding: 1rem;
      }

      .flow-number {
        color: var(--blue);
        display: block;
        font-size: 0.76rem;
        margin-bottom: 0.7rem;
      }

      .principle {
        border-left: 3px solid var(--blue);
        color: var(--ink);
        font-size: 1.08rem;
        line-height: 1.65;
        margin: 0.5rem 0 1.1rem;
        padding: 0.3rem 0 0.3rem 1rem;
      }

      .boundary {
        background: var(--blue-soft);
        border: 1px solid #d6e4ff;
        border-radius: 16px;
        color: #294463;
        line-height: 1.62;
        margin-top: 2rem;
        padding: 1.1rem 1.25rem;
      }

      .contact {
        background: #14233a;
        border-radius: 22px;
        color: #ffffff;
        margin-top: 3.8rem;
        padding: 2rem;
      }

      .contact h2 {
        color: #ffffff;
        letter-spacing: -0.025em;
        margin: 0 0 0.6rem;
      }

      .contact p {
        color: #cbd6e6;
        line-height: 1.6;
        margin: 0;
      }

      .contact a {
        color: #9fc2ff !important;
        font-weight: 650;
        text-decoration: none;
      }

      div.stDownloadButton > button {
        background: var(--blue);
        border: 0;
        border-radius: 10px;
        color: white;
        font-weight: 700;
        padding: 0.7rem 1rem;
      }

      @media (max-width: 800px) {
        .flow { grid-template-columns: 1fr; }
        .flow-step { min-height: auto; }
        .block-container { padding-top: 1.35rem; }
      }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="eyebrow">AI-assisted product delivery</div>', unsafe_allow_html=True)
st.markdown(
    '<h1 class="hero-title">Armando Elizalde</h1>',
    unsafe_allow_html=True,
)
st.markdown(
    """
    <p class="hero-subtitle">
      I turn ambiguous product ideas into reviewable, tested MVPs. My work combines
      architecture, AI-assisted implementation, delivery control and communication
      with technical and non-technical stakeholders in English and Spanish.
    </p>
    <div class="availability">
      <span class="availability-dot"></span>
      Project-based collaboration · Scope and engagement model open to discussion
    </div>
    """,
    unsafe_allow_html=True,
)

action_left, action_right, action_space = st.columns([1.2, 1.1, 3.7], gap="small")
with action_left:
    if PORTFOLIO_PDF.exists():
        st.download_button(
            "Download case study (PDF)",
            data=PORTFOLIO_PDF.read_bytes(),
            file_name="Armando_Elizalde_Portfolio_Case_Study.pdf",
            mime="application/pdf",
            use_container_width=True,
        )
with action_right:
    st.link_button(
        "View LinkedIn",
        "https://www.linkedin.com/in/elizaltech/",
        use_container_width=True,
    )


st.markdown('<div class="section-kicker">Selected case study</div>', unsafe_allow_html=True)
st.markdown(
    '<h2 class="section-title">Opportunity intelligence and evidence-assisted proposal preparation</h2>',
    unsafe_allow_html=True,
)
st.write(
    "A confidential engagement connected fragmented opportunity discovery with a "
    "human-reviewed document-preparation workflow. The case study is anonymized: "
    "client identity, private source code, operational systems and client documents are withheld."
)

left, middle, right = st.columns(3, gap="medium")
with left:
    st.markdown(
        """
        <div class="card">
          <div class="card-label">The problem</div>
          <h3>Two disconnected workflows</h3>
          <p>Teams had to find relevant opportunities, interpret requirements and locate credible prior evidence without losing meaning between handoffs.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with middle:
    st.markdown(
        """
        <div class="card">
          <div class="card-label">The product</div>
          <h3>A connected, reviewable flow</h3>
          <p>Multi-source discovery feeds an opportunity browser, structured ToR review, evidence retrieval and editable document generation.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with right:
    st.markdown(
        """
        <div class="card">
          <div class="card-label">My role</div>
          <h3>Architecture through release control</h3>
          <p>I led product scoping, architecture, AI-assisted delivery, code review, adversarial testing, integration and release decisions.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


st.markdown('<div class="section-kicker">End-to-end workflow</div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">From discovery to an editable draft</h2>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="flow">
      <div class="flow-step"><span class="flow-number">01</span>Collect and normalize public opportunities</div>
      <div class="flow-step"><span class="flow-number">02</span>Search, filter and understand why each result matched</div>
      <div class="flow-step"><span class="flow-number">03</span>Upload and review the Terms of Reference</div>
      <div class="flow-step"><span class="flow-number">04</span>Retrieve relevant capability evidence</div>
      <div class="flow-step"><span class="flow-number">05</span>Review, edit and export the draft</div>
    </div>
    """,
    unsafe_allow_html=True,
)


st.markdown('<div class="section-kicker">Engineering judgment</div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Reliability choices that protect user trust</h2>', unsafe_allow_html=True)

judgment_left, judgment_right = st.columns(2, gap="large")
with judgment_left:
    st.markdown(
        """
        <div class="principle"><strong>Validate by field name.</strong><br>Reordered data columns cannot silently move values into the wrong fields.</div>
        <div class="principle"><strong>Separate failure from an empty result.</strong><br>An unavailable source cannot quietly masquerade as “nothing found.”</div>
        <div class="principle"><strong>Explain discovery.</strong><br>Matched keywords and discovery timestamps make inclusion and freshness more understandable.</div>
        """,
        unsafe_allow_html=True,
    )
with judgment_right:
    st.markdown(
        """
        <div class="principle"><strong>Preserve last-known-good evidence.</strong><br>A failed document update should not automatically destroy useful searchable material.</div>
        <div class="principle"><strong>Show honest operational states.</strong><br>Empty, unavailable, partial and stale require different user actions.</div>
        <div class="principle"><strong>Keep human review explicit.</strong><br>Fluent generated text and source references are not substitutes for factual verification.</div>
        """,
        unsafe_allow_html=True,
    )


st.markdown('<div class="section-kicker">Delivery approach</div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">How I use AI without outsourcing judgment</h2>', unsafe_allow_html=True)

delivery_a, delivery_b, delivery_c, delivery_d = st.columns(4, gap="small")
delivery_cards = [
    (delivery_a, "01", "Define the contract", "Turn product intent into bounded behavior, ownership and acceptance criteria."),
    (delivery_b, "02", "Accelerate implementation", "Use AI coding tools for focused execution with explicit scope boundaries."),
    (delivery_c, "03", "Challenge assumptions", "Review architecture and test adversarial cases—not only successful demonstrations."),
    (delivery_d, "04", "Control integration", "Verify clean states, preserve traceability and communicate remaining limitations."),
]
for column, number, title, description in delivery_cards:
    with column:
        st.markdown(
            f"""
            <div class="card">
              <div class="card-label">{number}</div>
              <h3>{title}</h3>
              <p>{description}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )


st.markdown(
    """
    <div class="boundary">
      <strong>Responsible portfolio boundary.</strong> This case study describes inspected design and delivery decisions without publishing client identity, private repositories, credentials, operational URLs or confidential source documents. It does not claim unverified time savings, commercial outcomes, guaranteed AI accuracy or completed citation verification.
    </div>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
    <div class="contact">
      <h2>Let’s discuss a scoped MVP</h2>
      <p>
        Available for project-based product development with scope and engagement model open to discussion.<br>
        <a href="mailto:armando21elizalde@gmail.com">armando21elizalde@gmail.com</a>
        &nbsp;·&nbsp;
        <a href="https://www.linkedin.com/in/elizaltech/">LinkedIn</a>
        &nbsp;·&nbsp; English &amp; Spanish
      </p>
    </div>
    """,
    unsafe_allow_html=True,
)
