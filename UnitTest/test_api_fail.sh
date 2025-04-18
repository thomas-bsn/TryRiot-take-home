#!/bin/bash

echo "Test /decrypt avec des données mal encodées"
curl -s -X POST http://localhost:8000/decrypt \
  -H "Content-Type: application/json" \
  -d '{"name":"cestfaux", "age":"cestfaux", "contact":"{bad json"}'

echo -e "\n\nTest /verify avec une mauvaise signature"
curl -s -X POST http://localhost:8000/verify \
  -H "Content-Type: application/json" \
  -d '{
    "signature": "cestfaux",
    "data": {
      "message": "Hello World",
      "timestamp": 1616161616
    }
  }'

echo -e "\n\nTest /verify sans signature"
curl -s -X POST http://localhost:8000/verify \
  -H "Content-Type: application/json" \
  -d '{
    "data": {
      "message": "Hello World",
      "timestamp": 1616161616
    }
  }'

echo -e "\n\nTest /verify sans data"
curl -s -X POST http://localhost:8000/verify \
  -H "Content-Type: application/json" \
  -d '{
    "signature": "abcd1234"
  }'
