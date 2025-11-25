# Base image
FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY pyproject.toml ./
RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Copy project files
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Run app with Uvicorn
CMD ["uvicorn", "lead_gen_pro.app:app", "--host", "0.0.0.0", "--port", "8000"]