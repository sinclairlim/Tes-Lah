# Sentry Watcher

**Sentry Watcher** is a Python-based monitoring and alerting system designed to watch over a directory, analyze incoming files using AI models, upload results to cloud storage, and trigger alerts based on specific conditions. It's modular, extensible, and integrates cloud capabilities with intelligent automation.

## Features

- 🔍 **Directory Monitoring**: Watches for file changes using `watchdog`.
- 🧠 **File Analysis**: Uses a placeholder AI model for content analysis (can be extended).
- ☁️ **Cloud Upload**: Uploads files to AWS S3 with `boto3`.
- 🚨 **Alert System**: Sends alerts when suspicious content is detected.
- ✅ **Test Suite**: Simple tests to validate the AI logic.

## Project Structure

```
.
├── alert.py           # Alert system implementation
├── analyzer.py        # File content analyzer using AI logic
├── sentry_watcher.py  # Main service that watches and processes files
├── uploader.py        # Handles uploading files to AWS S3
├── test_ai.py         # Tests for the analyzer module
├── requirements.txt   # Python dependencies
```

## Installation

1. **Clone the repo:**

   ```bash
   git clone https://github.com/yourusername/sentry-watcher.git
   cd sentry-watcher
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment:**

   Create a `.env` file in the root directory with your AWS credentials:

   ```
   AWS_ACCESS_KEY_ID=your_access_key
   AWS_SECRET_ACCESS_KEY=your_secret_key
   AWS_REGION=your_region
   S3_BUCKET=your_bucket_name
   ```

## Usage

Start the Sentry Watcher:

```bash
python sentry_watcher.py /path/to/watch
```

## Testing

Run the included test suite:

```bash
python test_ai.py
```

## Extending

- Replace the placeholder AI model in `analyzer.py` with your own.
- Customize alerts in `alert.py` (e.g., Slack, Email, etc.).
- Add more file processing steps in `sentry_watcher.py`.

## Dependencies

See [`requirements.txt`](requirements.txt):
- `watchdog`
- `boto3`
- `python-dotenv`

## License

MIT License.
