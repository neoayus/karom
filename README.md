# YomiBashi (Backend)

## YomiBashi: Japanese (Kanji --> Romajai) Subtitle Converter API

YomiBashi is a FastAPI-based backend service that processes `.srt` subtitle files and converts Japanese text into a more readable format using **romaji/furigana-style transformations** powered by `pykakasi`.

It is designed to support language learners who want readable Japanese subtitles for study and comprehension.

---

## Live API

The backend is deployed and accessible at:

[YOMIBASHI@RENDER](https://yomibashi.onrender.com/)

---

## Purpose

YomiBashi backend is used to:

* Accept `.srt` subtitle files
* Process Japanese text
* Convert kanji/kana into readable romaji format
* Return a converted subtitle file
* Support frontend integration (React frontend hosted separately @ [YOMIBASHI@NETLIFY](https://yomibashi.netlify.app/))

This service powers the YomiBashi web application.

---

##  Tech Stack

* **Python 3**
* **FastAPI**
* **Uvicorn**
* **pykakasi**
* **srt**
* **python-multipart**

---

## Installation (Local Development)

### Step 01: Clone the repository

```bash
git clone https://github.com/neoayus/yomibashi-backend.git
cd yomibashi-backend
```

### Step 02: Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

### Step 03: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 04: Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Server will run at:
```
http://127.0.0.1:8000
```

## Deployment

This backend is deployed using:

* **Render (Web Service)**
* Python 3 runtime
* Uvicorn as ASGI server

Production URL:

```
https://yokibashi.onrender.com
```

## Future Improvements  

* Clean code
* Add authentication
* Add rate limiting
* Add file size limits
* Add caching
* Improve error handling