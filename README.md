# 🌤️ Weather Dashboard

![Python 3.12](https://img.shields.io/badge/Python-3.12-blue)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)

## Overview

This is a Streamlit web application that provides an interactive weather dashboard. It fetches real-time weather data from the Open-Meteo API and displays current conditions along with temperature trends in a user-friendly interface.

## Prerequisites

The only prerequisite is having Docker Desktop installed on your machine.

## Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/agrimal-tely/sandbox-python.git
   cd sandbox-python
   ```

2. Run the application:
   ```bash
   docker-compose up
   ```

   The dashboard will be available at `http://localhost:8501`.

## Architecture

The application uses a Dockerfile to create an isolated container environment running Python 3.12 and Streamlit. It employs Docker Compose for multi-container orchestration, ensuring easy deployment and scalability.