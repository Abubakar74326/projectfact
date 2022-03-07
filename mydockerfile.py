# Inherit from the Python Docker image
FROM python:3.7-slim
# Install the Flask package via pip
RUN pip install flask==1.0.2

ENTRYPOINT ["python"]
# Set the command as the script name
CMD ["api.py"]
