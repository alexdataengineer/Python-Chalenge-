# Marvel API Python Challenge


This project was built as part of a technical test.
It connects to the Marvel Comics API and retrieves character data using hardcoded API keys, as explicitly requested for the review.

Features

Authentication using ts + public key + private key + md5 hash.

Fetch characters with pagination (limit + offset).

Option to filter by name prefix (nameStartsWith).

Fetch related comics for a given character.

Simple script that prints sample characters to the console.

How to Run
python marvel_client.py


By default, it will fetch 3 characters and print their names.

Notes

API keys are hardcoded for review purposes only, as required in the test instructions.

Keys will be rotated after the evaluation.

For production use, environment variables should be used instead of hardcoding.
