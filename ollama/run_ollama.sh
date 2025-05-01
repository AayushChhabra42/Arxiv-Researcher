#!/bin/bash

echo "Starting Ollama server..."
ollama pull gemma3b:1b &
ollama serve



echo "Waiting for Ollama server to be active..."
while [ "$(ollama list | grep 'NAME')" = "" ]; do
  sleep 1
done