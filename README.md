# Agent Hub

Agent is a lightweight full-stack project built with Flask and Vue. It provides a clean frontend interface, a Flask backend, and basic authentication and chat capabilities.

## Project Highlights

- Frontend uses Vue 3 + Vite with a modern AI-style interface
- Backend uses Flask with health check, authentication, and chat endpoints
- Supports basic user registration and login
- Supports simple chat responses with OpenAI-compatible models when an API key is configured

## Project Structure

```text
Agent/
├── front/              # Vue frontend
│   ├── src/            # Pages and components
│   ├── package.json    # Frontend dependencies and scripts
│   └── vite.config.js  # Vite configuration
├── server/             # Flask backend
│   ├── blueprints/     # Route modules
│   ├── database/       # Database initialization and schema
│   ├── services/       # Service logic
│   └── tests/          # Backend tests
└── README.md           # Project documentation
```

## Requirements

- Python 3.9+
- Node.js 20+
- MySQL (required if you want to enable database-backed registration/login)

## Quick Start

### 1. Install backend dependencies

```bash
cd server
pip install -r requirements.txt
```

### 2. Install frontend dependencies

```bash
cd front
npm install
```

### 3. Start the backend

```bash
cd server
python main.py
```

The backend runs by default at:

- http://127.0.0.1:5000

### 4. Start the frontend

```bash
cd front
npm run dev
```

The frontend runs by default at:

- http://127.0.0.1:5173

## Configuration

### Database Configuration

The backend uses local MySQL by default. You can configure it through environment variables:

```bash
export MYSQL_HOST=localhost
export MYSQL_PORT=3306
export MYSQL_USER=root
export MYSQL_PASSWORD=your_password
export MYSQL_DATABASE=agent
```

### OpenAI Configuration

To allow the chat endpoint to call a real model, set the following environment variables:

```bash
export OPENAI_API_KEY=your_openai_api_key
export OPENAI_MODEL=gpt-4.1-mini
```

If these are not configured, the backend returns a mock response for local development.

## Main Endpoints

- GET /health: Check service status
- POST /auth/register: Register a user
- POST /auth/login: Log in a user
- POST /chat: Send a chat message

## Development Notes

If you want to extend the project further, you can explore the following directions:

- Add chat history support
- Integrate additional model providers
- Add frontend routing and a richer page structure
- Add more complete user information and permission control

## License

This project is intended for learning and demonstration purposes.