from fastapi import FastAPI
from app.db import get_db_connection
from app.routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/data", tags=["Data"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Olympics API!"}

@app.get("/test-db")
def test_db_connection():
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM olympic_hosts LIMIT 1")
            result = cursor.fetchone()
            conn.close()
            if result:
                return {"message": "Connexion réussie à la base de données", "sample_data": result}
            else:
                return {"message": "Connexion réussie à la base de données, mais aucune donnée n'a été trouvée"}
        except Exception as e:
            return {"message": f"Erreur lors de l'exécution de la requête: {str(e)}"}
    else:
        return {"message": "Échec de la connexion à la base de données"}

@app.get("/predictions")
def get_predictions():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Predictions")
        result = cursor.fetchall()
        conn.close()
        return {"predictions": result}
    else:
        return {"error": "Failed to connect to the database"}
