FROM python:3.10-slim

WORKDIR /app

# Create a non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app

# Copy files
COPY --chown=appuser:appuser . .

# Switch to non-root user
USER appuser

# Install dependencies
RUN pip install --no-cache-dir --user -r requirements.txt

# Add user's local bin to PATH
ENV PATH="/home/appuser/.local/bin:${PATH}"

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]