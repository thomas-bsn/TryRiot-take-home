#!/bin/bash

echo "Test /encrypt"
curl -s -X POST http://localhost:8000/encrypt \
  -H "Content-Type: application/json" \
  -d '{"name":"John Doe","age":30,"contact":{"email":"john@example.com","phone":"123-456-7890"}}' | tee tmp_encrypt.json

echo -e "\n\nTest /decrypt"
curl -s -X POST http://localhost:8000/decrypt \
  -H "Content-Type: application/json" \
  -d @tmp_encrypt.json

echo -e "\n\nTest /sign"
curl -s -X POST http://localhost:8000/sign \
  -H "Content-Type: application/json" \
  -d '{"message":"Hello World","timestamp":1616161616}' | tee tmp_signature.json

echo -e "\n\nTest /verify"
SIGNATURE=$(jq -r .signature tmp_signature.json)
curl -s -X POST http://localhost:8000/verify \
  -H "Content-Type: application/json" \
  -d "{\"signature\": \"$SIGNATURE\", \"data\": {\"message\": \"Hello World\", \"timestamp\": 1616161616}}"

echo -e "\n\nCleanup"
rm -f tmp_*.json
