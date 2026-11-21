# ✅ Viva Preparation Checklist

Use this checklist to ensure everything is ready for your presentation!

## 📦 Pre-Presentation Setup

### Backend Setup:
- [ ] Python 3.8+ installed (`python --version`)
- [ ] Virtual environment created (optional but recommended)
- [ ] Backend dependencies installed (`pip install -r backend/requirements.txt`)
- [ ] All model files exist in `models/` directory:
  - [ ] `best_model.pkl`
  - [ ] `label_encoders.pkl`
  - [ ] `feature_info.pkl`
  - [ ] `model_info.pkl`
  - [ ] `poly_transformer.pkl`
  - [ ] `kmeans_model.pkl`
  - [ ] `cluster_scaler.pkl`
- [ ] `.env` file created in `backend/` (optional, for chatbot)
- [ ] Backend runs successfully (`python backend/app.py`)
- [ ] Health check works: http://localhost:5000/api/health

### Frontend Setup:
- [ ] Node.js 16+ installed (`node --version`)
- [ ] Frontend dependencies installed (`cd frontend/vite-project && npm install`)
- [ ] Frontend runs successfully (`npm run dev`)
- [ ] Frontend opens in browser: http://localhost:5173

### Testing:
- [ ] Homepage loads correctly
- [ ] Model info displays
- [ ] Price prediction form works
- [ ] Prediction gives results
- [ ] Chatbot opens (even if API key not set)
- [ ] Analytics page loads
- [ ] Visualizations display

## 🎯 Demo Preparation

### What to Show:
1. [ ] **Homepage**: Show model statistics and overview
2. [ ] **Price Prediction**: 
   - Fill form with sample data
   - Show prediction result
   - Explain price range and segment
3. [ ] **Chatbot**: 
   - Start conversation
   - Ask for price prediction
   - Show natural language interaction
4. [ ] **Analytics**: 
   - Show model performance
   - Display visualizations
   - Explain metrics

### Sample Test Data:
- **Car 1**: Honda Civic, 2018, Petrol, 1800cc, Automatic, Karachi, 50,000 km
- **Car 2**: Toyota Corolla, 2020, Petrol, 1300cc, Manual, Lahore, 30,000 km
- **Car 3**: Suzuki Cultus, 2019, Petrol, 1000cc, Manual, Islamabad, 40,000 km

## 📝 Key Points to Remember

### Technical Points:
- Model: Random Forest with Polynomial Features
- Accuracy: ~94% (R² Score)
- Dataset: 5,497 cars from PakWheels
- Features: K-Means clustering for better predictions
- AI: Google Gemini for conversational interface

### Questions to Prepare For:
1. **Why Random Forest?**
   - Handles non-linear relationships
   - Robust to outliers
   - Provides feature importance

2. **Why K-Means Clustering?**
   - Groups similar cars
   - Improves prediction accuracy
   - Considers market segments

3. **Data Preprocessing?**
   - Label encoding for categorical variables
   - Feature scaling
   - Polynomial feature transformation
   - Missing value handling

4. **Model Evaluation?**
   - Train/Test split
   - R² Score, MAE, RMSE metrics
   - Cross-validation

## 🚨 Common Issues & Fixes

### Issue: Backend won't start
**Fix**: 
- Check Python version
- Install dependencies: `pip install -r backend/requirements.txt`
- Check model files exist

### Issue: Frontend won't start
**Fix**: 
- Check Node.js version
- Delete `node_modules` and run `npm install` again
- Clear npm cache: `npm cache clean --force`

### Issue: Can't connect frontend to backend
**Fix**: 
- Ensure backend is running on port 5000
- Check `src/services/api.js` has correct URL
- Check CORS settings in backend

### Issue: Models not loading
**Fix**: 
- Verify `models/` directory exists
- Check all .pkl files are present
- Run from correct directory

### Issue: Chatbot not working
**Fix**: 
- Chatbot works without API key (limited functionality)
- If want full features, add Gemini API key to `.env` file
- Check `.env` file is in `backend/` directory

## 💡 Presentation Tips

1. **Start with Demo**: Show the working application first
2. **Explain Architecture**: Frontend → Backend → ML Model
3. **Show Code**: If asked, show key files (app.py, chatbot.py)
4. **Highlight Features**: AI chatbot, ML predictions, analytics
5. **Explain Model**: How it works, why chosen, performance
6. **Be Confident**: You built this! Explain your choices

## 🎤 Quick Demo Script

1. **Introduction** (30 seconds):
   "This is an AI-powered car price prediction system for Pakistan. It uses Machine Learning to predict used car prices based on various features."

2. **Show Homepage** (30 seconds):
   "The homepage shows model statistics. Our Random Forest model has 94% accuracy, trained on 5,497 cars from PakWheels."

3. **Demo Prediction** (1 minute):
   "Let me predict a price. I'll enter a Honda Civic from 2018..."
   [Fill form and show result]
   "The model predicts this car is worth around X lacs, in the Premium segment."

4. **Show Chatbot** (1 minute):
   "We also have an AI chatbot powered by Google Gemini..."
   [Open chatbot and show conversation]
   "It can predict prices naturally through conversation."

5. **Show Analytics** (30 seconds):
   "The analytics page shows model performance, visualizations, and insights."

6. **Wrap Up** (30 seconds):
   "The system uses Random Forest with polynomial features and K-Means clustering for improved accuracy. Thank you!"

## ✅ Final Check (10 minutes before viva)

- [ ] Both servers are running (backend + frontend)
- [ ] Browser is open and application loads
- [ ] Have sample data ready for prediction
- [ ] Have backup plan if internet fails (local demo)
- [ ] Laptop is charged / plugged in
- [ ] Project folder is accessible

---

**Good luck! You've got this! 🚀🎓**


