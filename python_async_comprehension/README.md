# Python Async Comprehension

This project covers async generators and async comprehensions in Python.

## Learning Objectives

- Write async generators
- Use async comprehensions
- Type-annotate generators and async functions
- Understand parallel async execution with `asyncio.gather`

## Tasks

### 0. Async Generator
`0-async_generator.py` — Coroutine `async_generator` that loops 10 times, waits 1 second asynchronously each iteration, then yields a random float between 0 and 10.

### 1. Async Comprehensions
`1-async_comprehension.py` — Coroutine `async_comprehension` that collects 10 random numbers from `async_generator` using an async comprehension and returns them.

### 2. Run time for four parallel comprehensions
`2-measure_runtime.py` — Coroutine `measure_runtime` that runs `async_comprehension` four times in parallel using `asyncio.gather` and returns the total runtime.

> The total runtime is ~10 seconds (not ~40) because all four comprehensions run concurrently. Each one takes ~10 seconds (10 × 1s sleeps), but since they overlap in parallel, the total wall time is still ~10 seconds.

## Requirements

- Python 3.7+
- All files use `#!/usr/bin/env python3`
- Type annotations are used throughout
