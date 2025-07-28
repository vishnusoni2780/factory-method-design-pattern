# Factory Method Design Pattern
This script is a simple implementation of the `Factory Method Design Pattern`, aimed at demonstrating its core principles through a transport system example.

The project is structured to separate different transport modes `Air`, `Road` & `Sea` under the modes module, each implementing a specific transport behavior.

The `factory.py` handles the creation logic, while `client.py` serves as the entry point to interact with the system.

This design promotes flexibility and scalability by decoupling object creation from usage, making it easier to extend or modify transport modes without altering client code.

# Command Line

The command line requires Python to be installed.

To run the script:
```shell
$ py client.py
```

# Repository Structure
```
.
├── README.md
|── client.py
|── factory.py
├── modes
    ├── air.py
    ├── road.py
    |── sea.py
    └── transport.py
```
