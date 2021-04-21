
queue_1 = []  # first queue
queue_2 = []  # second queue


# Function to push an element into stack using two queues.
def push(x):

    # global declaration
    global queue_1
    global queue_2

    queue_1.append(x)
    # code here


# Function to pop an element from stack using two queues.
def pop():

    # global declaration
    global queue_1
    global queue_2
    # if(len(queue_1)==0):
    #     return -1
    while(len(queue_1) > 0):
        queue_2.append(queue_1.pop(0))
    if(len(queue_2) == 0):
        return -1
    return queue_2.pop(-1)
    # code here
