# **BotNetSim - High Volume Web Request Simulator**

## **Overview**
BotNetSim is a high-volume web request simulator designed to send a large number of requests to specified URLs using multiple threads. This project simulates a botnet by creating a customizable number of bots that repeatedly send HTTP requests to target websites. The requests use various user-agent strings to mimic different browsers and devices. It also handles connection retries, timeouts, and status code errors to ensure robust and persistent requests.

## **Features**
- **Multi-threaded Execution**: Capable of running up to 2000 threads simultaneously to simulate high traffic.
- **Randomized User Agents**: Uses a diverse list of user-agent strings to make requests appear as if they are coming from different browsers and platforms.
- **Session Management with Retries**: Implements session handling with automatic retries for failed requests.
- **Error Handling**: Manages connection errors, timeouts, and server-side errors (e.g., 403 Forbidden) gracefully.
- **Queue-Based Task Management**: Uses a queue to distribute tasks to worker threads efficiently.

## **Prerequisites**
Make sure you have the following installed before running the project:
- Python 3.x
- `requests` library (install using `pip install requests`)
- `urllib3` for handling retries and suppressing warnings.


