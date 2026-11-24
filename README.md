# Operating System Scheduling Algorithms

A console program in Python that simulates four CPU scheduling algorithms: FCFS, SJF, SRJF and Round Robin. I wrote it as an exercise for my operating systems course.

## What it does

You enter a list of processes, each with an arrival time and a burst time, and choose an algorithm. The program then prints, second by second, which process is running or whether the CPU is idle. It waits one real second for every time unit, so the output runs like a live clock.

| Algorithm | How it picks the next process |
| --- | --- |
| FCFS (first come, first served) | In arrival order |
| SJF (shortest job first) | Among arrived processes, the one with the shortest burst; it runs to completion |
| SRJF (shortest remaining job first) | Preemptive version of SJF, checked every second |
| Round Robin | Each process runs for a fixed time slice (quantum), then goes to the back of the queue |

## Run it

```
python "OS kodu.py"
```

The program asks for each process as two numbers separated by a space: arrival time, then burst time. Type 0 as the burst time to finish entering processes. Then choose 1 to 4 for the algorithm; Round Robin also asks for the quantum.

Example input: `0 5`, `2 3`, `4 0`, then `1` for FCFS.

## Notes

- Variable names and prompts are in Turkish.
- The file imports numpy, but nothing in the logic uses it, so it has to be installed or that import removed.
- It only prints the schedule. Waiting and turnaround times are not calculated.
