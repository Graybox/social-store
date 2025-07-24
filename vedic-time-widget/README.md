# Vedic Time Widget

This React application displays daily Vedic time information fetched from the
FastAPI backend provided in the repository. It supports offline mode and caches
the latest successful response locally.

## Development

1. Install dependencies:

   ```bash
   npm install
   ```

2. Ensure the API is running (see the project root `README.md`). Then start the
   widget in development mode. Set the API base URL via `VITE_ENGINE_BASE_URL`:

   ```bash
   VITE_ENGINE_BASE_URL=http://localhost:8080 npm run dev
   ```

   The widget will be available at `http://localhost:5173` and will proxy
   requests to the API.

## License

MIT
