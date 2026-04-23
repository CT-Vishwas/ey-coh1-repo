# Streamlit CSV Processor

A boilerplate Streamlit application that accepts a CSV upload, previews data, calculates numeric summaries, and generates a downloadable report in CSV or JSON format.

## Folder structure

- `app.py` - Streamlit app entry point
- `src/` - business logic modules
  - `data_processing.py` - CSV loading, cleaning, and summary helpers
  - `reporting.py` - report generation and exporting logic
  - `utils/file_io.py` - reusable file system utilities
- `reports/` - generated reports output directory
- `requirements.txt` - Python dependencies

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Run the app

```bash
streamlit run app.py
```

## Usage

1. Upload a CSV file using the sidebar.
2. Preview the first rows and numeric summary.
3. Click `Generate report` to save a report under `reports/`.
4. Download the generated report directly from the Streamlit UI.
