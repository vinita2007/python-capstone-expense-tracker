# Python Capstone Project - Personal Expense Tracker

## Overview
A portfolio-ready Python application built for **Module 06: Python Capstone Project**[span_4](start_span)[span_4](end_span). It features clean file structuring, exception safety, automated logging, and SQLite database storage.

## System Architecture & File Structure
- `expense_tracker.py` - Core application logic with error handling and logging.
- `expenses.db` - Persistent SQLite relational database.
- `expense_tracker.log` - Application runtime activity and error log.

## Database Schema (`expenses`)
- `id` (INTEGER, Primary Key, Auto-increment)
- `title` (TEXT, Not Null)
- `amount` (REAL, Not Null)
- `category` (TEXT, Not Null)
- `date` (TEXT, Not Null)

## Setup & Execution Instructions
1. Clone the repository.
2. Run the application script:
   ```bash
   python expense_tracker.py
   
