# Real-Time Delivery Tracking System 🚚

A Django-based delivery tracking system that integrates Google Maps with Apache Kafka for real-time location updates.

## 🌟 Features

- **Real-Time Tracking**: Live delivery agent location tracking on Google Maps
- **Kafka Integration**: Efficient location data streaming
- **Django Backend**: Robust backend for handling real-time updates
- **Interactive UI**: User-friendly interface for tracking deliveries

## 🛠️ Tech Stack

- Django 5.1.5
- Apache Kafka
- Google Maps API
- Python 3.11
- HTML/CSS/JavaScript

## 🚀 Quick Start

### Prerequisites

```bash
# Install Python 3.11+
# Install Apache Kafka
# Install Zookeeper
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/SagarNikam09/Delivery-Tracking-RealTime-kafka.git
cd Zomato-clone-Django
```

2. **Set up virtual environment**
```bash
python -m venv djenv
djenv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure Kafka**
```bash
# Start Zookeeper
.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties

# Start Kafka Server (in new terminal)
.\bin\windows\kafka-server-start.bat .\config\server.properties
```

5. **Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Start the development server**
```bash
python manage.py runserver
```

## 📝 Configuration

1. **Create .env file in project root**
```env
DEBUG=True
SECRET_KEY=your_secret_key
GOOGLE_MAPS_API_KEY=your_google_maps_api_key
```

2. **Configure Kafka settings**
```python
KAFKA_BOOTSTRAP_SERVERS = ['localhost:9092']
KAFKA_TOPIC = 'location_updates'
```

## 🔧 Usage

1. Start the Kafka consumer:
```bash
python manage.py kafka_consumer
```

2. Access the application:
- Open `http://localhost:8000` in your browser
- Track delivery locations in real-time
- View delivery updates on the interactive map

## 📚 API Endpoints

- `GET /`: Home page
- `GET /data/`: Get latest location updates
- `POST /update-location/`: Update delivery agent location

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

Distributed under the Apache License. See `LICENSE` for more information.
