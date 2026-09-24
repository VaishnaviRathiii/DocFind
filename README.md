# 🔎 Document Search using TF-IDF

<p align="center">
  <strong>NLP-based document retrieval using TF-IDF and Cosine Similarity.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/NLP-6D28D9?style=for-the-badge" />
  <img src="https://img.shields.io/badge/TF--IDF-8B5CF6?style=for-the-badge" />
</p>

---

## 🌐 Live Demo

🔗 **[Open Document Search App](YOUR_STREAMLIT_URL)**

---

## 📌 About

**Document Search using TF-IDF** is an NLP-based application that searches through a collection of text documents and retrieves the most relevant documents for a given query.

It uses **TF-IDF (Term Frequency-Inverse Document Frequency)** to represent text and **Cosine Similarity** to measure the relevance between the user's query and available documents.

---

## ✨ Features

- 🔎 Search documents using keywords or queries
- 📊 TF-IDF-based text representation
- 📐 Cosine Similarity-based relevance calculation
- 🏆 Automatic document ranking
- 📈 Similarity scores
- 📄 Most relevant document identification
- 📖 Document preview
- 🎨 Interactive Streamlit UI
- 📁 `.txt` document support

---

## 🧠 Technologies

| Technology | Purpose |
|---|---|
| Python | Core development |
| Streamlit | Web interface |
| Scikit-learn | TF-IDF and Cosine Similarity |
| NLP | Information Retrieval |
| HTML/CSS | UI styling |

---

## 🔄 How It Works

```text
User Query
    ↓
TF-IDF Vectorization
    ↓
Cosine Similarity
    ↓
Similarity Scores
    ↓
Document Ranking
    ↓
Relevant Documents

### Step-by-Step

1. **User enters a query**
   - The user provides keywords or a natural-language search query.

2. **TF-IDF Vectorization**
   - The query and documents are converted into numerical TF-IDF vectors.

3. **Cosine Similarity**
   - The similarity between the query vector and each document vector is calculated.

4. **Document Ranking**
   - Documents are ranked according to their similarity scores.

5. **Results Display**
   - The most relevant documents and their similarity scores are displayed in the Streamlit interface.

---

## ⚠️ Limitations

- Works mainly with `.txt` files
- Limited semantic understanding
- Does not automatically understand synonyms
- Uses traditional keyword-based retrieval
- May not perform well when the query uses words that are different from the document vocabulary

---

## 🔮 Future Scope

- 📄 PDF and DOCX support
- 🧠 Semantic search using embeddings
- 📤 User document upload
- 🔀 Hybrid search combining keyword and semantic retrieval
- 🔎 Search-term highlighting
- 📊 Search analytics
- 🌐 Support for larger document collections

---

## 👩‍💻 Author

### Vaishnavi Rathi

**Artificial Intelligence & Machine Learning Student**
