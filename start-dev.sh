#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

CYAN='\033[0;36m'
VIOLET='\033[0;35m'
GREEN='\033[0;32m'
DIM='\033[2m'
RESET='\033[0m'

cleanup() {
  echo ""
  echo -e "${VIOLET}Stopping RAYS DeckForge services...${RESET}"
  kill $FASTAPI_PID $NEXTJS_PID 2>/dev/null || true
  pkill -f "uvicorn server:app" 2>/dev/null || true
  pkill -f "next dev" 2>/dev/null || true
  echo -e "${GREEN}✓ All services stopped.${RESET}"
  exit 0
}

trap cleanup SIGINT SIGTERM

echo -e "${CYAN}"
cat "$SCRIPT_DIR/scripts/deckforge-ascii.txt" 2>/dev/null || echo "RAYS DeckForge"
echo -e "${RESET}"
echo -e "${DIM}Local-first AI presentation engine${RESET}"
echo ""

command -v uv >/dev/null 2>&1 || {
  echo "uv is required."
  exit 1
}
command -v node >/dev/null 2>&1 || {
  echo "Node.js is required."
  exit 1
}
command -v npm >/dev/null 2>&1 || {
  echo "npm is required."
  exit 1
}

if [ -f "$SCRIPT_DIR/.env" ]; then
  set -a
  source "$SCRIPT_DIR/.env"
  set +a
fi

FASTAPI_PORT=${FASTAPI_PORT:-8000}
NEXTJS_PORT=${NEXTJS_PORT:-3000}

echo -e "${CYAN}▸${RESET} FastAPI backend  → http://localhost:${FASTAPI_PORT}"
echo -e "${CYAN}▸${RESET} Next.js frontend → http://localhost:${NEXTJS_PORT}"
echo ""

# FastAPI
echo -e "${VIOLET}Starting FastAPI backend...${RESET}"
cd "$SCRIPT_DIR/servers/fastapi"
export APP_DATA_DIRECTORY="${APP_DATA_DIRECTORY:-$SCRIPT_DIR/app_data}"
export TEMP_DIRECTORY="${TEMP_DIRECTORY:-$SCRIPT_DIR/app_data/temp}"
export USER_CONFIG_PATH="${USER_CONFIG_PATH:-$SCRIPT_DIR/app_data/userConfig.json}"
mkdir -p "$APP_DATA_DIRECTORY" "$TEMP_DIRECTORY"

uv run uvicorn server:app --host 0.0.0.0 --port "$FASTAPI_PORT" --reload &
FASTAPI_PID=$!

sleep 2

# Next.js
echo -e "${VIOLET}Starting Next.js frontend...${RESET}"
cd "$SCRIPT_DIR/servers/nextjs"
export NEXT_PUBLIC_FAST_API="http://localhost:${FASTAPI_PORT}"
export FAST_API_INTERNAL_URL="http://localhost:${FASTAPI_PORT}"
export DISABLE_AUTH="${DISABLE_AUTH:-true}"

PORT=$NEXTJS_PORT npm run dev &
NEXTJS_PID=$!

echo ""
echo -e "${GREEN}✓ RAYS DeckForge is running${RESET}"
echo -e "${DIM}Backend:  http://localhost:${FASTAPI_PORT}/docs${RESET}"
echo -e "${DIM}Frontend: http://localhost:${NEXTJS_PORT}${RESET}"
echo ""
echo -e "${DIM}Press Ctrl+C to stop all servers${RESET}"

wait
