import streamlit as st
import os


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Document Search using TF-IDF",
    page_icon="🔎",
    layout="wide"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.html("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700&family=Roboto:wght@400;500;600;700&display=swap');


/* ============================================================
   PAGE
============================================================ */

.stApp {
    background-color: #F8F7FC;
}

.block-container {
    max-width: 1150px;
    padding-top: 35px;
    padding-bottom: 50px;
}


/* ============================================================
   HIDE STREAMLIT DEFAULT UI
============================================================ */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}


/* ============================================================
   FONTS
============================================================ */

h1,
h2,
h3 {
    font-family: 'Playfair Display', serif !important;
}

p,
label,
input,
button {
    font-family: 'Roboto', sans-serif !important;
}


/* ============================================================
   SIDEBAR
============================================================ */

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #4C1D95 0%,
        #5B21B6 50%,
        #6D28D9 100%
    );
}

section[data-testid="stSidebar"] * {
    color: white;
}


/* ============================================================
   TEXT INPUT
============================================================ */

div[data-baseweb="input"] {
    border-radius: 14px;
    background-color: white;
    border: 1px solid #DDD6FE;
}

div[data-baseweb="input"]:focus-within {
    border: 2px solid #8B5CF6;
    box-shadow: 0 0 0 2px #EDE9FE;
}


/* ============================================================
   BUTTON
============================================================ */

.stButton > button {
    width: 100%;
    border: none;
    border-radius: 14px;

    background: linear-gradient(
        135deg,
        #6D28D9,
        #8B5CF6
    );

    color: white;
    font-weight: 600;
    padding: 11px 18px;

    transition: 0.2s;
}

.stButton > button:hover {
    background: linear-gradient(
        135deg,
        #5B21B6,
        #7C3AED
    );

    color: white;

    transform: translateY(-2px);

    box-shadow:
        0 8px 18px
        rgba(109, 40, 217, 0.25);
}


/* ============================================================
   ALERTS
============================================================ */

div[data-testid="stAlert"] {
    border-radius: 14px;
}

</style>
""")


# ============================================================
# LOAD DOCUMENTS
# ============================================================

def load_documents():

    folder = "documents"

    documents = []
    names = []

    if not os.path.exists(folder):
        return documents, names

    for filename in sorted(os.listdir(folder)):

        if filename.lower().endswith(".txt"):

            path = os.path.join(folder, filename)

            try:

                with open(
                    path,
                    "r",
                    encoding="utf-8"
                ) as file:

                    content = file.read()

                if content.strip():

                    documents.append(content)
                    names.append(filename)

            except Exception:
                pass

    return documents, names


# ============================================================
# TF-IDF SEARCH
# ============================================================

def search_documents(query, documents, names):

    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    all_text = documents + [query]

    matrix = vectorizer.fit_transform(all_text)

    document_vectors = matrix[:-1]

    query_vector = matrix[-1]

    scores = cosine_similarity(
        query_vector,
        document_vectors
    )[0]

    results = list(
        zip(names, documents, scores)
    )

    results.sort(
        key=lambda x: x[2],
        reverse=True
    )

    return results


# ============================================================
# LOAD DOCUMENT DATA
# ============================================================

documents, document_names = load_documents()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.html("""
    <div style="
        text-align:center;
        padding:20px 5px 30px 5px;
    ">

        <div style="
            font-size:45px;
            margin-bottom:8px;
        ">
            🔎
        </div>

        <div style="
            font-family:'Playfair Display',serif;
            font-size:28px;
            font-weight:700;
            color:white;
        ">
            DocFind
        </div>

        <div style="
            font-family:Roboto,sans-serif;
            font-size:11px;
            letter-spacing:2px;
            color:#C4B5FD;
            margin-top:5px;
        ">
            DOCUMENT SEARCH
        </div>

    </div>
    """)


    # --------------------------------------------------------
    # PROJECT
    # --------------------------------------------------------

    st.html("""
    <div style="
        font-size:11px;
        letter-spacing:1.5px;
        font-weight:700;
        color:#C4B5FD;
        margin-bottom:10px;
    ">
        PROJECT
    </div>
    """)


    # --------------------------------------------------------
    # INFORMATION RETRIEVAL
    # --------------------------------------------------------

    st.html("""
    <div style="
        background:rgba(255,255,255,0.11);
        border:1px solid rgba(255,255,255,0.08);
        border-radius:14px;
        padding:15px;
        margin-bottom:12px;
    ">

        <div style="
            font-weight:600;
            font-size:14px;
        ">
            📚 Information Retrieval
        </div>

        <div style="
            font-size:12px;
            color:#EDE9FE;
            margin-top:6px;
            line-height:1.5;
        ">
            Search and retrieve relevant
            documents using NLP.
        </div>

    </div>
    """)


    # --------------------------------------------------------
    # TF-IDF
    # --------------------------------------------------------

    st.html("""
    <div style="
        background:rgba(255,255,255,0.11);
        border:1px solid rgba(255,255,255,0.08);
        border-radius:14px;
        padding:15px;
        margin-bottom:12px;
    ">

        <div style="
            font-weight:600;
            font-size:14px;
        ">
            📊 TF-IDF
        </div>

        <div style="
            font-size:12px;
            color:#EDE9FE;
            margin-top:6px;
            line-height:1.5;
        ">
            Converts text into numerical
            feature vectors.
        </div>

    </div>
    """)


    # --------------------------------------------------------
    # COSINE SIMILARITY
    # --------------------------------------------------------

    st.html("""
    <div style="
        background:rgba(255,255,255,0.11);
        border:1px solid rgba(255,255,255,0.08);
        border-radius:14px;
        padding:15px;
        margin-bottom:12px;
    ">

        <div style="
            font-weight:600;
            font-size:14px;
        ">
            📐 Cosine Similarity
        </div>

        <div style="
            font-size:12px;
            color:#EDE9FE;
            margin-top:6px;
            line-height:1.5;
        ">
            Measures similarity between
            query and documents.
        </div>

    </div>
    """)


    # --------------------------------------------------------
    # DOCUMENT COUNT
    # --------------------------------------------------------

    st.html(f"""
    <div style="
        margin-top:25px;
        background:rgba(255,255,255,0.11);
        border:1px solid rgba(255,255,255,0.08);
        border-radius:14px;
        padding:15px;
    ">

        <div style="
            font-weight:600;
            font-size:14px;
        ">
            📄 Documents Loaded
        </div>

        <div style="
            font-size:12px;
            color:#EDE9FE;
            margin-top:6px;
        ">
            {len(documents)} text documents
        </div>

    </div>
    """)


# ============================================================
# HERO SECTION
# ============================================================

st.html("""
<div style="
    background:linear-gradient(
        135deg,
        #4C1D95 0%,
        #6D28D9 55%,
        #8B5CF6 100%
    );

    border-radius:28px;

    padding:42px;

    margin-bottom:25px;

    box-shadow:
        0 12px 30px
        rgba(109,40,217,0.20);

">

    <div style="
        font-size:45px;
        margin-bottom:8px;
    ">
        🔎
    </div>

    <div style="
        font-family:'Playfair Display',serif;
        font-size:42px;
        font-weight:700;
        color:white;
        line-height:1.1;
    ">
        Document Search
    </div>

    <div style="
        font-family:Roboto,sans-serif;
        font-size:16px;
        color:#EDE9FE;
        margin-top:10px;
        line-height:1.6;
        max-width:700px;
    ">
        Search and retrieve the most relevant
        document using TF-IDF and Cosine Similarity.
    </div>


    <!-- TAGS -->

    <div style="margin-top:20px;">

        <span style="
            display:inline-block;
            background:#A78BFA;
            color:white;
            padding:7px 13px;
            border-radius:20px;
            font-size:11px;
            font-weight:700;
            margin-right:6px;
        ">
            TF-IDF
        </span>

        <span style="
            display:inline-block;
            background:rgba(255,255,255,0.15);
            color:white;
            padding:7px 13px;
            border-radius:20px;
            font-size:11px;
            font-weight:700;
            margin-right:6px;
        ">
            COSINE SIMILARITY
        </span>

        <span style="
            display:inline-block;
            background:rgba(255,255,255,0.15);
            color:white;
            padding:7px 13px;
            border-radius:20px;
            font-size:11px;
            font-weight:700;
            margin-right:6px;
        ">
            NLP
        </span>

        <span style="
            display:inline-block;
            background:rgba(255,255,255,0.15);
            color:white;
            padding:7px 13px;
            border-radius:20px;
            font-size:11px;
            font-weight:700;
        ">
            INFORMATION RETRIEVAL
        </span>

    </div>

</div>
""")


# ============================================================
# STATISTICS CARDS
# ============================================================

col1, col2, col3 = st.columns(3)


# ============================================================
# CARD 1
# ============================================================

with col1:

    st.html(f"""
    <div style="
        background:white;
        border:1px solid #DDD6FE;
        border-radius:18px;
        padding:20px;

        box-shadow:
            0 4px 12px
            rgba(76,29,149,0.06);
    ">

        <div style="font-size:27px;">
            📄
        </div>

        <div style="
            font-size:28px;
            font-weight:700;
            color:#4C1D95;
            margin-top:5px;
        ">
            {len(documents)}
        </div>

        <div style="
            color:#6B6478;
            font-size:13px;
        ">
            Documents Available
        </div>

    </div>
    """)


# ============================================================
# CARD 2
# ============================================================

with col2:

    st.html("""
    <div style="
        background:white;
        border:1px solid #DDD6FE;
        border-radius:18px;
        padding:20px;

        box-shadow:
            0 4px 12px
            rgba(76,29,149,0.06);
    ">

        <div style="font-size:27px;">
            📊
        </div>

        <div style="
            font-size:24px;
            font-weight:700;
            color:#4C1D95;
            margin-top:8px;
        ">
            TF-IDF
        </div>

        <div style="
            color:#6B6478;
            font-size:13px;
        ">
            Text Representation
        </div>

    </div>
    """)


# ============================================================
# CARD 3
# ============================================================

with col3:

    st.html("""
    <div style="
        background:white;
        border:1px solid #DDD6FE;
        border-radius:18px;
        padding:20px;

        box-shadow:
            0 4px 12px
            rgba(76,29,149,0.06);
    ">

        <div style="font-size:27px;">
            📐
        </div>

        <div style="
            font-size:24px;
            font-weight:700;
            color:#4C1D95;
            margin-top:8px;
        ">
            Cosine
        </div>

        <div style="
            color:#6B6478;
            font-size:13px;
        ">
            Similarity Method
        </div>

    </div>
    """)


# ============================================================
# SEARCH SECTION HEADER
# ============================================================

st.html("""
<div style="
    background:white;

    border:1px solid #DDD6FE;

    border-radius:20px;

    padding:22px 25px 12px 25px;

    margin-top:25px;

    box-shadow:
        0 4px 12px
        rgba(76,29,149,0.04);
">

    <div style="
        font-family:'Playfair Display',serif;
        color:#4C1D95;
        font-size:25px;
        font-weight:600;
    ">
        🔍 Search Your Documents
    </div>

    <div style="
        color:#6B6478;
        font-size:13px;
        margin-top:5px;
    ">
        Enter a keyword or sentence to find
        the most relevant document.
    </div>

</div>
""")


# ============================================================
# SEARCH INPUT + BUTTON
# ============================================================

search_col, button_col = st.columns(
    [5, 1],
    vertical_alignment="bottom"
)


with search_col:

    query = st.text_input(
        "Search",
        placeholder="Example: machine learning algorithms",
        label_visibility="collapsed"
    )


with button_col:

    search_clicked = st.button(
        "🔍 Search",
        type="primary"
    )


# ============================================================
# SEARCH PROCESS
# ============================================================

if search_clicked:

    if not query.strip():

        st.warning(
            "Please enter a search query."
        )

    elif not documents:

        st.error(
            "No documents found. Add .txt files "
            "inside the documents folder."
        )

    else:

        results = search_documents(
            query,
            documents,
            document_names
        )

        st.session_state.results = results
        st.session_state.query = query


# ============================================================
# DISPLAY RESULTS
# ============================================================

if "results" in st.session_state:

    results = st.session_state.results

    query = st.session_state.query


    # ========================================================
    # RESULTS HEADER
    # ========================================================

    st.html(f"""
    <div style="
        margin-top:30px;
        margin-bottom:15px;

        display:flex;
        justify-content:space-between;
        align-items:center;
    ">

        <div style="
            font-family:'Playfair Display',serif;
            color:#4C1D95;
            font-size:27px;
            font-weight:600;
        ">
            Search Results
        </div>

        <div style="
            background:#EDE9FE;
            color:#6D28D9;
            padding:7px 13px;
            border-radius:20px;
            font-size:11px;
            font-weight:700;
        ">
            {len(results)} DOCUMENTS
        </div>

    </div>


    <!-- QUERY DISPLAY -->

    <div style="
        background:#F3F0FF;

        border-left:4px solid #8B5CF6;

        border-radius:10px;

        padding:12px 16px;

        color:#5B21B6;

        font-size:13px;

        margin-bottom:18px;
    ">
        🔎 <strong>Query:</strong> {query}
    </div>
    """)


    # ========================================================
    # RESULT CARDS
    # ========================================================

    for rank, (name, text, score) in enumerate(
        results,
        start=1
    ):

        percentage = score * 100

        # Keep progress bar inside valid range
        bar_width = max(
            0,
            min(
                100,
                percentage
            )
        )

        st.html(f"""
        <div style="
            background:white;

            border:1px solid #DDD6FE;

            border-radius:18px;

            padding:20px;

            margin-bottom:13px;

            box-shadow:
                0 4px 12px
                rgba(76,29,149,0.05);
        ">


            <!-- RESULT NUMBER -->

            <div style="
                display:inline-block;

                background:#EDE9FE;

                color:#6D28D9;

                padding:5px 10px;

                border-radius:8px;

                font-size:10px;

                font-weight:700;
            ">
                RESULT #{rank}
            </div>


            <!-- FILE NAME -->

            <div style="
                font-size:17px;

                font-weight:700;

                color:#29213D;

                margin-top:10px;
            ">
                📄 {name}
            </div>


            <!-- SCORE -->

            <div style="
                color:#6B6478;

                font-size:13px;

                margin-top:5px;
            ">
                Cosine Similarity:

                <strong style="
                    color:#6D28D9;
                ">
                    {percentage:.2f}%
                </strong>
            </div>


            <!-- PROGRESS BAR -->

            <div style="
                width:100%;

                height:8px;

                background:#EDE9FE;

                border-radius:20px;

                margin-top:13px;

                overflow:hidden;
            ">

                <div style="
                    width:{bar_width}%;

                    height:100%;

                    background:linear-gradient(
                        90deg,
                        #6D28D9,
                        #A78BFA
                    );

                    border-radius:20px;
                ">
                </div>

            </div>

        </div>
        """)


    # ========================================================
    # BEST RESULT
    # ========================================================

    best_name, best_text, best_score = results[0]

    best_percentage = best_score * 100


    st.html(f"""
    <div style="
        background:linear-gradient(
            135deg,
            #F3F0FF,
            #EDE9FE
        );

        border:2px solid #8B5CF6;

        border-radius:20px;

        padding:25px;

        margin-top:25px;
    ">

        <div style="
            color:#6D28D9;

            font-size:11px;

            font-weight:700;

            letter-spacing:1.5px;
        ">
            🏆 MOST RELEVANT DOCUMENT
        </div>


        <div style="
            font-family:'Playfair Display',serif;

            color:#4C1D95;

            font-size:27px;

            font-weight:600;

            margin-top:8px;
        ">
            📄 {best_name}
        </div>


        <div style="
            color:#6D28D9;

            font-size:15px;

            font-weight:600;

            margin-top:7px;
        ">
            Similarity Score: {best_percentage:.2f}%
        </div>

    </div>
    """)


    # ========================================================
    # DOCUMENT PREVIEW
    # ========================================================

    st.html(f"""
    <div style="
        background:linear-gradient(
            135deg,
            #4C1D95,
            #6D28D9
        );

        border-radius:20px;

        padding:25px;

        margin-top:18px;
    ">

        <div style="
            color:#C4B5FD;

            font-size:11px;

            font-weight:700;

            letter-spacing:1.5px;

            margin-bottom:12px;
        ">
            📖 DOCUMENT PREVIEW
        </div>


        <div style="
            color:#F8F7FC;

            font-size:14px;

            line-height:1.8;
        ">
            {best_text}
        </div>

    </div>
    """)


# ============================================================
# HOW IT WORKS
# ============================================================

st.html("""
<div style="
    background:white;

    border:1px solid #DDD6FE;

    border-radius:20px;

    padding:25px;

    margin-top:30px;

    box-shadow:
        0 4px 12px
        rgba(76,29,149,0.04);
">

    <div style="
        font-family:'Playfair Display',serif;

        color:#4C1D95;

        font-size:25px;

        font-weight:600;
    ">
        ⚙️ How It Works
    </div>


    <div style="
        color:#6B6478;

        font-size:13px;

        margin-top:5px;

        margin-bottom:18px;
    ">
        The system follows three main steps.
    </div>


    <!-- STEP 1 -->

    <div style="
        background:#F8F7FC;

        border:1px solid #EDE9FE;

        border-radius:14px;

        padding:16px;

        margin-bottom:10px;
    ">

        <strong style="
            color:#4C1D95;
        ">
            01 &nbsp; TF-IDF Vectorization
        </strong>


        <div style="
            color:#6B6478;

            font-size:12px;

            margin-top:7px;
        ">
            Converts documents and the query
            into numerical vectors.
        </div>

    </div>


    <!-- STEP 2 -->

    <div style="
        background:#F8F7FC;

        border:1px solid #EDE9FE;

        border-radius:14px;

        padding:16px;

        margin-bottom:10px;
    ">

        <strong style="
            color:#4C1D95;
        ">
            02 &nbsp; Cosine Similarity
        </strong>


        <div style="
            color:#6B6478;

            font-size:12px;

            margin-top:7px;
        ">
            Calculates how similar the query is
            to every document.
        </div>

    </div>


    <!-- STEP 3 -->

    <div style="
        background:#F8F7FC;

        border:1px solid #EDE9FE;

        border-radius:14px;

        padding:16px;
    ">

        <strong style="
            color:#4C1D95;
        ">
            03 &nbsp; Ranking
        </strong>


        <div style="
            color:#6B6478;

            font-size:12px;

            margin-top:7px;
        ">
            Documents are ranked according to
            their similarity scores.
        </div>

    </div>

</div>
""")


# ============================================================
# FOOTER
# ============================================================

st.html("""
<div style="
    margin-top:50px;
    padding:25px 20px 15px 20px;
    border-top:1px solid #DDD6FE;
    text-align:center;
">

    <div style="
        font-family:'Playfair Display',serif;
        font-size:20px;
        font-weight:600;
        color:#4C1D95;
        margin-bottom:6px;
    ">
        Document Search using TF-IDF
    </div>

    <div style="
        font-size:13px;
        text-decoration:none !important;
        color:#6B6478;
        margin-bottom:12px;
    ">
        Created by
        <strong style="color:#6D28D9;">
            <a href="mailto:rathivaishnavi949@gmail.com" target="_blank">Vaishnavi Rathi</a>
        </strong>
        <br>
        &nbsp;•&nbsp;
        For Educational Purposes Only.
    </div>

    <div style="
        display:flex;
        justify-content:center;
        gap:10px;
        flex-wrap:wrap;
    ">

        <a
            href="https://www.linkedin.com/in/vaishnavi-rathi-/"
            target="_blank"
            style="
                text-decoration:none;
                background:#F3F0FF;
                color:#6D28D9;
                border:1px solid #DDD6FE;
                padding:7px 14px;
                border-radius:20px;
                font-size:12px;
                font-weight:600;
            "
        >
            LinkedIn
        </a>

        <a
            href="https://github.com/VaishnaviRathiii"
            target="_blank"
            style="
                text-decoration:none;
                background:#F3F0FF;
                color:#6D28D9;
                border:1px solid #DDD6FE;
                padding:7px 14px;
                border-radius:20px;
                font-size:12px;
                font-weight:600;
            "
        >
            GitHub
        </a>

    </div>

    <div style="
        font-size:10px;
        color:#A39AAD;
        margin-top:15px;
    ">
        © 2026 Vaishnavi Rathi
    </div>

</div>
""")