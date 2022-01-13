import uvicorn

from app import create_app

app = create_app()

if __name__ == "__main__":
    file_name = __file__.split('/')[-1].replace('.py', '')
    uvicorn.run(
        f"{file_name}:app",
        host="0.0.0.0",
        port=4500,
        log_level="debug",
        reload=True,
    )
