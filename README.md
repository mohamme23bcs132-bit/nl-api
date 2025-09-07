# ML API - Iris Classification

A FastAPI-based machine learning API for Iris flower classification using a trained Random Forest model.

## Features

- FastAPI web framework
- Iris classification using scikit-learn
- Docker containerized
- Ready for cloud deployment

## Local Development

### Using Docker
```bash
docker build -t ml-api .
docker run -p 8000:8000 ml-api
```

### API Endpoints

- `GET /` - Welcome message
- `POST /predict` - Make predictions
- `GET /docs` - API documentation

### Example Usage

```bash
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

## Deployment

This project is configured for deployment on Railway, Render, or other container platforms.
