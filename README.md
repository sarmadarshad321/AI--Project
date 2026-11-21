# 🚗 AI Car Price Prediction System

A complete AI-powered web application for predicting used car prices in Pakistan using Machine Learning and Natural Language Processing.

## 📋 Project Overview

This project features:
- **ML Model**: Random Forest with Polynomial Features & K-Means Clustering
- **Frontend**: React.js with Vite
- **Backend**: Flask REST API
- **AI Chatbot**: Google Gemini AI for conversational car price predictions
- **Analytics Dashboard**: Data visualization and model performance metrics

## 🛠️ Tech Stack

### Backend
- Python 3.8+
- Flask 3.0.0
- scikit-learn
- pandas, numpy
- Google Generative AI (Gemini)

### Frontend
- React 19
- Vite
- Tailwind CSS
- Recharts (for visualizations)
- Axios (API calls)

## 📁 Project Structure

```
AI-Project-main/
├── backend/
│   ├── app.py              # Flask API server
│   ├── chatbot.py          # Gemini AI chatbot
│   ├── requirements.txt    # Python dependencies
│   └── env.txt            # Environment variables template
├── frontend/
│   └── vite-project/       # React frontend
│       ├── src/
│       │   ├── components/ # React components
│       │   ├── pages/      # Page components
│       │   └── services/   # API services
│       └── package.json
├── models/                 # Trained ML models (.pkl files)
├── data/                   # Dataset files (.csv)
└── visualizations/         # Generated charts and graphs
```

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.8 or higher
- Node.js 16+ and npm
- Gemini API Key (optional, for chatbot)

### Step 1: Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create virtual environment (recommended):**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup Gemini API Key (Optional for chatbot):**
   - Copy `env.txt` to `.env`:
     ```bash
     copy env.txt .env   # Windows
     cp env.txt .env     # Linux/Mac
     ```
   - Edit `.env` and add your Gemini API key:
     ```
     GEMINI_API_KEY=your_actual_api_key_here
     ```
   - Get API key from: https://aistudio.google.com/app/apikey

5. **Start Backend Server:**
   ```bash
   python app.py
   ```
   
   Backend will run on: `http://localhost:5000`

### Step 2: Frontend Setup

1. **Open a new terminal and navigate to frontend:**
   ```bash
   cd frontend/vite-project
   ```

2. **Install Node dependencies:**
   ```bash
   npm install
   ```

3. **Start Frontend Development Server:**
   ```bash
   npm run dev
   ```
   
   Frontend will run on: `http://localhost:5173` (or another port if 5173 is busy)

### Step 3: Access the Application

- **Frontend**: Open `http://localhost:5173` in your browser
- **Backend API**: `http://localhost:5000`
- **Health Check**: `http://localhost:5000/api/health`

## 🎯 Features

### 1. **Car Price Prediction**
- Input car details (brand, model, city, fuel type, engine, transmission, year, mileage)
- Get instant price prediction with confidence range
- Price segmentation (Economy, Mid-Range, Premium, Luxury)

### 2. **AI Chatbot**
- Conversational interface using Google Gemini AI
- Natural language car price predictions
- Can chat about any topic (not just cars)
- Supports Urdu/English mix

### 3. **Analytics Dashboard**
- Model performance metrics (R², MAE, RMSE)
- Data visualizations:
  - Actual vs Predicted prices
  - Feature importance
  - Model comparison
  - Cluster distributions

### 4. **Model Information**
- Model accuracy and performance statistics
- Feature options and valid inputs
- Dataset information

## 📊 Model Performance

- **Algorithm**: Random Forest Regressor
- **Accuracy (R² Score)**: ~94%
- **Features**: Polynomial transformation + K-Means clustering
- **Dataset**: 5,497 cars from PakWheels

## 🔌 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API information |
| `/api/health` | GET | Health check |
| `/api/model-info` | GET | Model performance metrics |
| `/api/feature-options` | GET | Valid input options |
| `/api/predict` | POST | Predict car price |
| `/api/analytics/stats` | GET | Analytics statistics |
| `/api/visualizations/<name>` | GET | Get visualization images |
| `/api/chatbot` | POST | Chatbot conversation |

### Example Prediction Request:
```json
POST /api/predict
{
  "car_brand": "honda",
  "car_model": "civic",
  "city": "karachi",
  "fuel_type": "petrol",
  "engine": 1800,
  "transmission": "automatic",
  "registered_in": 2018,
  "mileage": 50000
}
```

## 🐛 Troubleshooting

### Backend Issues:

1. **Models not loading:**
   - Check if `models/` directory exists with all .pkl files
   - Ensure you're running from project root or backend directory

2. **Port 5000 already in use:**
   - Change port in `app.py` line 3461: `app.run(debug=True, host="0.0.0.0", port=5001)`
   - Update frontend API URL in `frontend/vite-project/src/services/api.js`

3. **Gemini API errors:**
   - Check if `.env` file exists in `backend/` directory
   - Verify API key is correct
   - Chatbot will work without API key but with limited functionality

### Frontend Issues:

1. **npm install fails:**
   - Delete `node_modules` and `package-lock.json`
   - Run `npm install` again
   - Try `npm cache clean --force`

2. **Can't connect to backend:**
   - Ensure backend is running on port 5000
   - Check CORS settings in backend `app.py`
   - Verify API URL in `src/services/api.js`

3. **Port 5173 already in use:**
   - Vite will automatically use next available port
   - Check terminal output for actual port number

## 📝 For Viva Presentation

### Key Points to Highlight:

1. **Technology Stack**: Modern tech (React, Flask, ML)
2. **AI Integration**: Google Gemini for conversational AI
3. **ML Model**: Random Forest with 94% accuracy
4. **Features**: 
   - Price prediction
   - AI chatbot
   - Analytics dashboard
   - Real-time predictions

### Demo Flow:

1. Show homepage with model statistics
2. Demonstrate price prediction form
3. Show AI chatbot conversation
4. Display analytics dashboard
5. Explain model performance metrics

### Questions You Might Get:

- **Q: Why Random Forest?**
  - A: Handles non-linear relationships well, robust to outliers, provides feature importance

- **Q: Why K-Means clustering?**
  - A: Groups similar cars, improves prediction accuracy by considering car segments

- **Q: How did you collect data?**
  - A: Used PakWheels dataset with 5,497 car listings

- **Q: What's the accuracy?**
  - A: R² score of 0.94, meaning 94% of variance is explained by the model

## 📞 Support

If you face any issues:
1. Check all dependencies are installed
2. Ensure both backend and frontend are running
3. Check console/terminal for error messages
4. Verify API keys are set correctly (if using chatbot)

## 📄 License

This project is for academic/educational purposes.

## ✨ Credits

- Dataset: PakWheels
- ML Framework: scikit-learn
- AI Model: Google Gemini
- Frontend: React + Vite
- Backend: Flask

---

**Good luck with your viva! 🎓**


