# Scalable REST API Test Automation Framework

A lightweight automation testing framework built using Python and PyTest to validate REST APIs.

## Features
- Automated REST API testing
- Status code validation
- Response schema validation
- Response time performance testing
- Structured logging for debugging
- HTML test report generation

## Tech Stack
- Python
- PyTest
- Requests
- PyTest-HTML

## Project Structure

api-testing-framework
│
├── tests
├── utils
├── config
├── logs
├── requirements.txt

## Run Tests

pip install -r requirements.txt

pytest

## Generate HTML Test Report

pytest --html=report.html
