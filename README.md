# pair

Extension of the socket.socket class with functionality usefull for sending data between two computers on the same (wireless) network.
    
It requires coordinantion between the sender and receiver, as receiving side (using the current implementation) will (once receiving has been called) block execution of whatever is running, and keep on waiting for the data. So you need to be sure that something is in the socket, or on the way.

The intended usage is when two operators are sitting close by, and can (verbaly) agree when something is to be send/received.

## Use
### Establishing connection
When establishing connection we differentiate between the innviting side and the joining side. The inviting side chooses a port number (PORT), which needs to be larger than 1024, I normaly use a number between 8000 and 9000. The joining side joins using the PORT number and the E number, which is the last part of the inviters IP HOST address on the network -- this will be printed out when inviting side invites, and should be commuincated to the joinin side. If you test the ´pair´ on your local machine by communincating between two python sessions running in parallel, chools E=0 to indicate joining on local host.  

| | Inviting side   | Joining side  |
---|---|---
| imports |  <code> import pair </code> <br/> <code> import numpy as np </code> | <code> import pair </code> <br/> <code> import numpy as np </code>   |
| inviting| <code> socket = pair.pair.invite(PORT) </code> |  |
| joining|  | <code> socket = pair.pair.join(E, PORT) </code> |

### Transfering data

| | Sending side   | Receiving side  |
---|---|---
| text |  <code> socket.sendtext('Hello world! ') </code> | <code> txt = socket.recvtext() </code>   |
| numpy arrays | <code> A = np.arange(1000000).reshape((2500,400)) </code> <br/> <code> socket.sendb(A) </code> | <code> A = socket.recvb() <code> |

### Closing

| | Both sides   |
---|---
| closing |  <code> socket.close() </code> | 

