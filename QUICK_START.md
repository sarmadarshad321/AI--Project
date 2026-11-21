# ⚡ Quick Start Guide

## 🚀 Run Project in 5 Minutes

### Step 1: Start Backend (Terminal 1)

```bash
# Navigate to backend
cd backend

# Install dependencies (first time only)
pip install -r requirements.txt

# Start server
python app.py
```

✅ Backend running at: http://localhost:5000

### Step 2: Start Frontend (Terminal 2)

```bash
# Navigate to frontend
cd frontend/vite-project

# Install dependencies (first time only)
npm install

# Start development server
npm run dev
```

✅ Frontend running at: http://localhost:5173

### Step 3: Open Browser

Open: **http://localhost:5173**

That's it! 🎉

---

## 📝 Quick Troubleshooting

**Backend error?**
- Check Python version: `python --version` (need 3.8+)
- Install missing packages: `pip install -r backend/requirements.txt`

**Frontend error?**
- Check Node version: `node --version` (need 16+)
- Delete `node_modules` and run `npm install` again

**Can't connect?**
- Make sure BOTH servers are running
- Check backend is on port 5000
- Check frontend API URL in `frontend/vite-project/src/services/api.js`

---

## 🎯 Test the Application

1. **Homepage**: Should show model statistics
2. **Predict**: Fill form → Click Predict → See result
3. **Chatbot**: Click chat icon → Type "Hello" → Chat works
4. **Analytics**: Click Analytics → See charts and metrics

---

**Ready for viva! Good luck! 🎓**


