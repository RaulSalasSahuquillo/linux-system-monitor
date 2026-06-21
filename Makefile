# Makefile to compile and execute the System Resource Monitor application

# Compiler settings and flags
CC = gcc
CFLAGS = -O2 -Wall
TARGET = src/cpu_motor
SRC = src/cpu.c

.PHONY: all clean run

# Default rule to compile the C engine
all: $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) $< -o $@

# Rule to compile and run the application
run: all
	python3 src/main.py

# Rule to clean up generated files
clean:
	rm -f $(TARGET)
	rm -rf src/__pycache__
