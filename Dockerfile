
# 1. Builder stage (prod deps)
    FROM python:3.12-slim AS builder

    WORKDIR /app
    
    ENV PYTHONDONTWRITEBYTECODE=1
    ENV PYTHONUNBUFFERED=1
    
    RUN apt-get update && apt-get install -y \
        build-essential \
        && rm -rf /var/lib/apt/lists/*
    
    RUN pip install --upgrade pip
    
    COPY requirements.txt .
    
    # Install production dependencies
    RUN pip install --no-cache-dir --prefix=/install -r requirements.txt
    
    
 # 2. Test stage (dev + tests)
    FROM python:3.12-slim AS test
    
    WORKDIR /app
    
    ENV PYTHONDONTWRITEBYTECODE=1
    ENV PYTHONUNBUFFERED=1
    
    RUN pip install --upgrade pip
    
    # Copy dependencies from builder
    COPY --from=builder /install /usr/local
    
    # Copy dev requirements
    COPY requirements-dev.txt .
    
    # Install dev dependencies
    RUN pip install --no-cache-dir -r requirements-dev.txt
    
    # Copy full project (including tests)
    COPY . .
    
    # Run tests
    RUN python -m pytest --disable-warnings -v
    
    
# 3. Final stage (runtime)
    FROM python:3.12-slim AS final
    
    WORKDIR /app
    
    ENV PYTHONDONTWRITEBYTECODE=1
    ENV PYTHONUNBUFFERED=1
    
    # Create non-root user
    RUN addgroup --system app && adduser --system --group app
    
    # Copy only prod dependencies
    COPY --from=builder /install /usr/local
    
    # Copy application code only (no tests ideally)
    COPY app ./app
    COPY requirements.txt .
    
    # Set ownership
    RUN chown -R app:app /app
    
    # Switch to non-root user
    USER app
    
    EXPOSE 8000
    
    CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]