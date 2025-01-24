#!/bin/bash

while ! nc -z server 8000; do
  echo "Aguardando o servidor estar pronto..."
  sleep 1
done

python3 client.py