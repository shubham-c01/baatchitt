set -e

pip install -r requirements.txt
uvicorn main:app --reload --port 3001
npm install && npm run build
npm start dev
