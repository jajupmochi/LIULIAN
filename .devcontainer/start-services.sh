#!/bin/bash

# Start backend in background
echo "Starting FastAPI backend on port 8000..."
cd /workspaces/LIULIAN
uv run uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload > /tmp/backend.log 2>&1 &

# Wait a moment for backend to start
sleep 3

# Start frontend in background
echo "Starting Streamlit frontend on port 8501..."
uv run streamlit run frontend/app.py --server.port 8501 --server.address 0.0.0.0 > /tmp/frontend.log 2>&1 &

echo ""
echo "✅ Services started!"
echo "   - Backend API: http://localhost:8000/docs"
echo "   - Frontend UI: http://localhost:8501"
echo ""
echo "Check logs:"
echo "   - Backend: tail -f /tmp/backend.log"
echo "   - Frontend: tail -f /tmp/frontend.log"
