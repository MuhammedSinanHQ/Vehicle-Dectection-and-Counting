# Vehicle Detection and Counting

A computer-vision project that detects and counts vehicles in video frames.
The core analysis pipeline lives in the Jupyter notebook (`Vehicle_Detect_&_Count.ipynb`),
and a minimal Flask web app is provided for deployment.

## Project Structure

```
.
├── app.py                        # Flask web app entrypoint
├── app/
│   └── templates/
│       └── index.html            # Landing page template
├── render.yaml                   # Render deployment blueprint
├── requirements.txt              # Python dependencies
├── README.md                     # This file
└── Vehicle_Detect_&_Count.ipynb  # Core detection notebook
```

## Local Development

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app**

   ```bash
   python app.py
   ```

   The server starts on <http://localhost:8000>.

3. **Available endpoints**

   | Route | Description |
   |-------|-------------|
   | `GET /` | Landing page |
   | `GET /health` | Returns `{"status": "healthy"}` |

## Deploy to Render (Free Plan)

This repository includes a `render.yaml` [Blueprint](https://render.com/docs/blueprint-spec)
so you can deploy in a few clicks with no billing configuration needed.

### Steps

1. Fork or push this repository to your own GitHub account.
2. Go to <https://dashboard.render.com> and click **New → Blueprint**.
3. Connect your GitHub account and select this repository.
4. Render will detect `render.yaml` and configure the service automatically.
5. Click **Apply** — the app will be built and deployed on the free plan.

Once deployed, your service URL will be shown in the Render dashboard.

## Notebook

Open `Vehicle_Detect_&_Count.ipynb` in Jupyter to explore the vehicle detection
and counting pipeline step by step:

```bash
pip install jupyter
jupyter notebook
```
