# AI Finance Controller

> **Razorpay Buildathon 2026 | Track 04 — "Run the books and the cash position"**

The AI Finance Controller is a full-stack system designed to automate financial reconciliation. It seamlessly matches bank transaction feeds with internal ledgers, using a state-of-the-art multi-tier pipeline that goes beyond traditional rule-based matching.

## Key Features

- **High-Throughput Processing**: Utilizes DeepBlocker-inspired SIF embeddings to perform rapid pre-filtering of transaction candidates.
- **Advanced Normalization**: Normalizes dates, names, and amounts accurately to improve matching rates using Ditto-inspired architectures.
- **4-Tier Reconciliation Pipeline**:
  - **Tier 1 (Exact Match)**: Immediate match on amount, date, and reference.
  - **Tier 2 (Probabilistic Matching)**: Uses Jaro-Winkler string comparison and Fellegi-Sunter weights to handle fees, delays, and structural grouping.
  - **Tier 3 (LLM Fallback)**: Intelligent discrepancy resolution powered by Google Gemini, employing advanced prompt structuring and span tagging for high F1 precision.
  - **Tier 4 (Exception Handling)**: Categorizes unresolvable matches with clear, actionable reason codes (e.g., Missing, Duplicates).
- **Beautiful & Real-Time Dashboard**: Built with React + Vite. Features live Server-Sent Events (SSE) streaming of processing logs, statistical visualizers, and an integrated Q&A settlement chatbot.

## Architecture

Our application is structured into a modern decoupled stack:
- **Frontend**: React + Vite (Hosted on Vercel)
- **Backend**: Python + FastAPI (Hosted on Railway)
- **AI Integration**: Gemini API for advanced match confidence scoring and exception analysis.

## Getting Started

### Backend Setup

1. Navigate to the `backend/` directory:
   ```bash
   cd backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your environment variables (e.g., in `.env`):
   ```
   GEMINI_API_KEY=your_api_key_here
   ```
4. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend Setup

1. Navigate to the `frontend/` directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the development server:
   ```bash
   npm run dev
   ```

## Demo & Testing

Run our built-in data generator to spin up synthetic test cases representing 9 distinct transaction mismatch scenarios, and upload `bank.csv` and `ledger.csv` through the dashboard to test the pipeline live!
