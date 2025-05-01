#!/bin/bash

echo "Starting Ollama server..."
ollama run
ollama pull gemma3:1b &
ollama serve 



echo "Waiting for Ollama server to be active..."
while [ "$(ollama list | grep 'NAME')" = "" ]; do
  sleep 1
done