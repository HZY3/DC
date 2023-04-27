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

    ########################################################################################################################
    Various approaches to detect the deadlock in the distributed system are as follows:

1. Centralized Approach

Only one resource is responsible for detecting deadlock in the centralized method, and it is simple and easy to use. Still, the disadvantages include excessive workload on a single node and single-point failure (i.e., the entire system is dependent on one node, and if that node fails, the entire system crashes), making the system less reliable.

2. Hierarchical Approach

In a distributed system, it is the integration of both centralized and distributed approaches to deadlock detection. In this strategy, a single node handles a set of selected nodes or clusters of nodes that are in charge of deadlock detection.

3. Distributed Approach

In the distributed technique, various nodes work to detect deadlocks. There is no single point of failure as the workload is equally spread among all nodes. It also helps to increase the speed of deadlock detection.
   
    1. Deadlock Prevention: As the name implies, this strategy ensures that deadlock can never happen because system designing is carried out in such a way. If any one of the deadlock-causing conditions is not met then deadlock can be prevented. Following are the three methods used for preventing deadlocks by making one of the deadlock conditions to be unsatisfied:

Collective Requests: In this strategy, all the processes will declare the required resources for their execution beforehand and will be allowed to execute only if there is the availability of all the required resources. When the process ends up with processing then only resources will be released. Hence, the hold and wait condition of deadlock will be prevented.
But the issue is initial resource requirements of a process before it starts are based on an assumption and not because they will be required. So, resources will be unnecessarily occupied by a process and prior allocation of resources also affects potential concurrency.
Ordered Requests: In this strategy, ordering is imposed on the resources and thus, process requests for resources in increasing order. Hence, the circular wait condition of deadlock can be prevented. 
An ordering strictly indicates that a process never asks for a low resource while holding a high one.
There are two more ways of dealing with global timing and transactions in distributed systems, both of which are based on the principle of assigning a global timestamp to each transaction as soon as it begins.
    2. Deadlock Avoidance: In this strategy, deadlock can be avoided by examining the state of the system at every step. The distributed system reviews the allocation of resources and wherever it finds an unsafe state, the system backtracks one step and again comes to the safe state. For this, resource allocation takes time whenever requested by a process. Firstly, the system analysis occurs whether the granting of resources will make the system in a safe state or unsafe state then only allocation will be made.

A safe state refers to the state when the system is not in deadlocked state and order is there for the process regarding the granting of requests.
An unsafe state refers to the state when no safe sequence exists for the system. Safe sequence implies the ordering of a process in such a way that all the processes run to completion in a safe state.
3. Deadlock Detection and Recovery: In this strategy, deadlock is detected and an attempt is made to resolve the deadlock state of the system. These approaches rely on a Wait-For-Graph (WFG), which is generated and evaluated for cycles in some methods. The following two requirements must be met by a deadlock detection algorithm: 

Progress: In a given period, the algorithm must find all existing deadlocks. There should be no deadlock existing in the system which is undetected under this condition. To put it another way, after all, wait-for dependencies for a deadlock have arisen, the algorithm should not wait for any additional events to detect the deadlock. 
 No False Deadlocks: Deadlocks that do not exist should not be reported by the algorithm which is called phantom or false deadlocks.
