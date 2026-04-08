# Threading means multiple execution paths inside the same process. It is a fundamental OS-level mechanism for concurrent executions.
# Threading  allows a single process to have multiple "threads of execution" running concurrently - think of it as multiple workers within the same workspace, sharing the same memory and resources but each doing different tasks.

"""
Concurrency in computer science refers to the ability of a system to handle multiple tasks by making progress on them during overlapping time periods, though not necessarily executing them simultaneously. It's about dealing with many things at once by organizing and coordinating tasks so they run efficiently without interfering with each other, even on a single CPU through time-sharing or context switching

Python's threading module is just a wrapper around OS-level threads (POSIX threads on Unix/Linux, Windows threads on Windows). However, Python has a notorious limitation: the Global Interpreter Lock (GIL).
The GIL means that even with multiple threads, only one thread can execute Python bytecode at a time. This makes Python threading useful for I/O-bound tasks (network requests, file operations, database queries) where threads spend time waiting, but nearly useless for CPU-bound tasks (mathematical computations, data processing) where you need true parallel computation.

A process owns:
- Memory (heap)
- Code
- Open files

A thread is lightweight worker inside that process:
- Shares the same memory
- Has its own instruction pointers and stack
- Runs in parallel (or interleaved)

"""