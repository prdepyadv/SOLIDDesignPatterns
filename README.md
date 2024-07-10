# Python: SOLID Principles and Top Design Patterns

## Design Patterns in Python

This repository contains implementations of various design patterns in Python, including the Factory Method and Singleton patterns. Additionally, it includes an example of a thread-safe Singleton logger in a Flask application.

## Factory Method Pattern

The Factory Method pattern defines an interface for creating an object, but allows subclasses to alter the type of objects that will be created. This is useful for situations where a class cannot anticipate the class of objects it must create.

## Singleton Pattern

The Singleton pattern ensures that a class has only one instance and provides a global point of access to it. This is useful for shared resources like configuration settings or logging.

### Thread-Safe Singleton Logger in Flask

The app/commands/__init__.py file demonstrate how to implement a thread-safe Singleton logger in a Flask application.

## Usage

Install dependencies:
pip install -r requirements.txt

Run the Flask application:
flask --app app run
