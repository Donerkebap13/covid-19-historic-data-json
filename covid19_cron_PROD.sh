#!/bin/bash

python3 covid19_data_retriever_PROD.py

git add .

git status

git commit -m "Automatic Update"

git push