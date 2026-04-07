# Step 1: Choose a base image
FROM python:3.11-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy dependencies file first
COPY requirements.txt .

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of your app code
COPY . .

# Step 6: Tell Docker which port the app uses
EXPOSE 5000

# Step 7: Command to run the app
CMD ["python", "app.py"]
