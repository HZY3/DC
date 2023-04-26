# Initialize variables and data structures
NumProcesses = 5
NumResources = 3
available = [3, 3, 2] # array of available resources
maximum = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]] # matrix of maximum required resources
allocation = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]] # matrix of currently allocated resources
need = [[7, 4, 3], [1, 2, 2], [6, 0, 0], [0, 1, 1], [4, 3, 1]] # matrix of needed resources
finish = [False] * NumProcesses # list of processes that have finished
work = available[:] # list of available resources used for deadlock detection
safeSequenceFound = False # flag indicating whether a safe sequence has been found
safeSequence = [] # list to store the safe sequence

# Deadlock prevention
for i in range(NumProcesses):
    for j in range(NumResources):
        if available[j] < need[i][j]:
            print("Deadlock Prevention: Process ", i, " is blocked because there are not enough resources available.")
            break
    else:
        # Allocate the resources and mark the process as finished
        for j in range(NumResources):
            available[j] -= need[i][j]
            allocation[i][j] += need[i][j]
            need[i][j] = 0
        finish[i] = True

# Loop until all processes have finished or a deadlock is detected
while not safeSequenceFound:
    # Deadlock avoidance
    safeSequenceFound = True # assume a safe sequence has been found
    for i in range(NumProcesses):
        if not finish[i]:
            canRun = True
            for j in range(NumResources):
                if need[i][j] > work[j]:
                    canRun = False
                    break
            if canRun:
                # Process i can run, so allocate its resources and mark it as finished
                for j in range(NumResources):
                    work[j] += allocation[i][j]
                finish[i] = True
                safeSequence.append(i) # add process i to the safe sequence
                safeSequenceFound = (finish.count(True) == NumProcesses) # check if all processes have finished
                break
    if not safeSequenceFound:
        # Deadlock detection
        deadlockDetected = True # assume deadlock has occurred
        for i in range(NumProcesses):
            if not finish[i]:
                canRun = True
                for j in range(NumResources):
                    if need[i][j] > available[j]:
                        canRun = False
                        break
                if canRun:
                    deadlockDetected = False # a deadlock has not occurred
                    break
        if deadlockDetected:
            # Deadlock has occurred, attempt to recover
            for i in range(NumProcesses):
                if not finish[i]:
                    canRun = True
                    for j in range(NumResources):
                        if need[i][j] > available[j]:
                            canRun = False
                            break
                    if canRun:
                        # Terminate process i and free its resources
                        for j in range(NumResources):
                            available[j] += allocation[i][j]
                            allocation[i][j] =0
                            need [i][j]=0
                        finish[i]=True
                        break

# Print whether the system is in a safe state and the safe sequence
if safeSequenceFound:
    print ("system is in safe sequcne")
    print ("Safe Sequcne : ", safeSequence)
else:
    print ("deadlock detected")
