import csv
import streamlit as st
from io import StringIO

# ---#1-----
st.set_page_config(page_title="CSV Profiler", layout="wide")

st.title("CSV Profiler")
st.caption("Upload CSV → profile → export JSON + Markdown")

st.sidebar.header("Inputs")

rows = None
report = st.session_state.get("report")

# ----2-----
uploaded = st.file_uploader("Upload a CSV", type=["csv"])
show_preview = st.sidebar.checkbox("Show preview", value=True)

if uploaded is not None:
    text = uploaded.getvalue().decode("utf-8-sig")
    rows = list(csv.DictReader(StringIO(text)))

    if show_preview:
        st.subheader("Preview")
        st.write(rows[:5])
else:
    st.info("Upload a CSV to begin.")

#---3----
from profile import profile_rows

if rows is not None:
    if len(rows) > 0:
        if st.button("Generate report"):
            st.session_state["report"] = profile_rows(rows)



# ---4----
from render import write_markdown

if report is not None:
    st.subheader("Columns")
    st.write(report["columns"])

    with st.expander("Markdown preview", expanded=False):
        st.markdown(write_markdown(report))

# ---5----

import json
from pathlib import Path
from render import write_markdown

if report is not None:
    report_name = st.sidebar.text_input("Report name", value="report")

    json_file = report_name + ".json"
    json_text = json.dumps(report, indent=2, ensure_ascii=False)

    md_file = report_name + ".md"
    md_text = write_markdown(report)

    c1, c2 = st.columns(2)
    c1.download_button("Download JSON", data=json_text, file_name=json_file)
    c2.download_button("Download Markdown", data=md_text, file_name=md_file)

    if st.button("Save to outputs/"):
        out_dir = Path("outputs")
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / json_file).write_text(json_text, encoding="utf-8")
        (out_dir / md_file).write_text(md_text, encoding="utf-8")
        st.success("Saved outputs/" + json_file + " and outputs/" + md_file)


#--6----

if uploaded is not None:
    text = uploaded.getvalue().decode("utf-8-sig")
    rows = list(csv.DictReader(StringIO(text)))

    if len(rows) == 0:
        st.error("CSV has no data. Upload a CSV with at least 1 row.")
        st.stop()

    if len(rows[0]) == 0:
        st.warning("CSV has no headers (no columns detected).")
