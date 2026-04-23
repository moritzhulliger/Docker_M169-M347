FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-eng \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install flask pytesseract Pillow

WORKDIR /app

COPY ocr_server.py .

EXPOSE 5000

CMD ["python3", "ocr_server.py"]