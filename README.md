# Credit Score Prediction API

A Flask-based REST API service that provides credit score predictions using a machine learning model. This service is containerized with Docker and designed to work within a microservices architecture.

## 🚀 Features

- **Credit Score Prediction**: Predict credit scores based on personal and financial data
- **RESTful API**: Simple HTTP endpoints for easy integration
- **Dockerized**: Fully containerized for easy deployment
- **CORS Enabled**: Cross-origin resource sharing for web applications
- **Health Check**: Built-in health check endpoint

## 📋 Prerequisites

- Python 3.10+
- Docker and Docker Compose
- Pre-trained ML model (`model.pkl`)

## 🛠️ Installation

### Local Development

1. Clone the repository:

```bash
git clone <repository-url>
cd pt2-ai
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python app.py
```

The service will be available at `http://localhost:5000`

### Docker Deployment

1. Build and run with Docker Compose:

```bash
docker-compose up --build
```

The service will be available at `http://localhost:5001`

## 📡 API Endpoints

### Health Check

```http
GET /
```

Returns: `"Healthy"`

### Predict Credit Score

```http
POST /predict
Content-Type: application/json
```

#### Request Body

```json
{
  "FLAG_OWN_CAR": 1,
  "FLAG_OWN_REALTY": 0,
  "CNT_CHILDREN": 2,
  "AMT_INCOME_TOTAL": 50000,
  "NAME_INCOME_TYPE": "Working",
  "NAME_EDUCATION_TYPE": "Higher education",
  "NAME_FAMILY_STATUS": "Married",
  "NAME_HOUSING_TYPE": "House / apartment",
  "DAYS_BIRTH": -12000,
  "DAYS_EMPLOYED": -3000,
  "OCCUPATION_TYPE": "Accountants",
  "CNT_FAM_MEMBERS": 4,
  "CNT_ADULTS": 2,
  "AMT_INCOME_PER_CHILDREN": 25000,
  "AMT_INCOME_PER_FAM_MEMBER": 12500
}
```

#### Response

```json
{
  "score": 85
}
```

## 📊 Input Parameters

| Parameter                   | Type    | Description                       |
| --------------------------- | ------- | --------------------------------- |
| `FLAG_OWN_CAR`              | Integer | Car ownership flag (0/1)          |
| `FLAG_OWN_REALTY`           | Integer | Real estate ownership flag (0/1)  |
| `CNT_CHILDREN`              | Integer | Number of children                |
| `AMT_INCOME_TOTAL`          | Float   | Total income amount               |
| `NAME_INCOME_TYPE`          | String  | Type of income source             |
| `NAME_EDUCATION_TYPE`       | String  | Education level                   |
| `NAME_FAMILY_STATUS`        | String  | Family status                     |
| `NAME_HOUSING_TYPE`         | String  | Housing type                      |
| `DAYS_BIRTH`                | Integer | Days since birth (negative value) |
| `DAYS_EMPLOYED`             | Integer | Days employed (negative value)    |
| `OCCUPATION_TYPE`           | String  | Occupation type                   |
| `CNT_FAM_MEMBERS`           | Integer | Number of family members          |
| `CNT_ADULTS`                | Integer | Number of adults in family        |
| `AMT_INCOME_PER_CHILDREN`   | Float   | Income per child                  |
| `AMT_INCOME_PER_FAM_MEMBER` | Float   | Income per family member          |

## 🏗️ Project Structure

```
pt2-ai/
├── app.py                 # Main application entry point
├── config.py             # Configuration and model loading
├── controller.py         # Business logic for predictions
├── routes.py             # API route definitions
├── model.pkl             # Pre-trained ML model
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker container configuration
├── docker-compose.yaml  # Docker Compose configuration
└── README.md           # Project documentation
```

## 🐳 Docker Configuration

The application is configured to run in a Docker container with the following specifications:

- **Base Image**: Python 3.10
- **Port Mapping**: 5001 (host) → 5000 (container)
- **Environment**: Flask debug mode enabled
- **Network**: Connected to `pt2-backend_network` (external)

## 🔧 Configuration

### Environment Variables

- `FLASK_APP`: Set to `app.py`
- `FLASK_RUN_HOST`: Set to `0.0.0.0` for container access
- `FLASK_ENV`: Set to `debug` for development

### CORS Configuration

The API is configured to accept requests from any origin with GET and POST methods enabled.

## 🧪 Testing

### Example cURL Request

```bash
curl -X POST http://localhost:5001/predict \
  -H "Content-Type: application/json" \
  -d '{
    "FLAG_OWN_CAR": 1,
    "FLAG_OWN_REALTY": 0,
    "CNT_CHILDREN": 2,
    "AMT_INCOME_TOTAL": 50000,
    "NAME_INCOME_TYPE": "Working",
    "NAME_EDUCATION_TYPE": "Higher education",
    "NAME_FAMILY_STATUS": "Married",
    "NAME_HOUSING_TYPE": "House / apartment",
    "DAYS_BIRTH": -12000,
    "DAYS_EMPLOYED": -3000,
    "OCCUPATION_TYPE": "Accountants",
    "CNT_FAM_MEMBERS": 4,
    "CNT_ADULTS": 2,
    "AMT_INCOME_PER_CHILDREN": 25000,
    "AMT_INCOME_PER_FAM_MEMBER": 12500
  }'
```

## 📦 Dependencies

### Core Dependencies

- **Flask 3.1.1**: Web framework
- **scikit-learn 1.4.2**: Machine learning library
- **pandas 2.3.1**: Data manipulation
- **joblib 1.5.1**: Model serialization
- **flask-cors 6.0.1**: Cross-origin resource sharing
- **numpy 2.2.6**: Numerical computing

### Full dependency list available in `requirements.txt`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions, please open an issue in the repository or contact the development team.

---

**Note**: Make sure you have the `model.pkl` file in the root directory before running the application. This file contains the pre-trained machine learning model required for predictions.
