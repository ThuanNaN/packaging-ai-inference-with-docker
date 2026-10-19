# packaging-ai-inference-with-docker

OCR app packaged with Docker: upload an image, get the detected text lines and bounding boxes.

- **backend/**: FastAPI + [RapidOCR](https://github.com/RapidAI/RapidOCR) (ONNX Runtime, CPU only). Endpoints: `GET /health`, `POST /ocr/predict`.
- **frontend/**: Gradio UI that calls the backend and draws the boxes on the image.

## Run

Requires Docker with Compose.

```bash
cp frontend/.env.example frontend/.env
docker compose up --build -d
```

- UI: http://localhost:3000
- API docs: http://localhost:8000/docs
- Try the API: `curl -F "file_upload=@sample.png" http://localhost:8000/ocr/predict`

Uploaded images are saved to `backend/app/logs/images/` (bind-mounted into the backend container).

```bash
docker compose logs -f   # follow logs
docker compose down      # stop and remove containers
```
