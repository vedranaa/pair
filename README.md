# `pair`: pair your sock(et)s!

Extension of the [`socket.socket`](https://docs.python.org/3/library/socket.html) class with functionality usefull for sending data between two computers on the same (wireless) network.
    
It requires coordinantion between the sender and receiver, as receiving side (using the current implementation) will (once receiving has been called) block execution of whatever is running, and keep on waiting for the data. So you need to be sure that something is in the socket, or on the way.

The intended usage is when two operators are sitting close by, and can (verbaly) agree when something is to be send/received.

## Use
### Establishing connection
When establishing connection we differentiate between the innviting side and the joining side. The inviting side chooses a port number (PORT), which needs to be larger than 1024, I normaly use a number between 8000 and 9000. The joining side joins using the PORT number and the E number, which is the last part of the inviters IP HOST address on the network -- this will be printed out when inviting side invites, and should be commuincated to the joinin side. If you test the `pair` on your local machine by communincating between two python sessions running in parallel, chools E=0 to indicate joining on local host. (Extra info: after joining, the communication will be on another, not the initial, port.) 

| | Inviting side   | Joining side  |
---|---|---
| imports |  <code> import pair </code> | <code> import pair </code> |
| inviting| <code> PORT = 8035 # or other nr </code> <br/> <code> socket = pair.pair.invite(PORT) </code> <br/> <code> Out: Inviting to 8, 8035 </code>|  |
| joining|  | <code> socket = pair.pair.join(8, 8035) # use (0, 835) for localhost! </code> |
| confirmation| <code> Out: Paired! </code> | <code> Out: Paired </code>|

### Transfering data -- TODO: FIX TRUNCATED PICKLE!
After the connection has been established, there is no difference betweeen the funcionality for the inviting and the joining side. One side sends, and another side receives. Do not call for receive, unless something has been, or will be send. The funcionality for text works only for text. The functionality for bytes works for whatever (also text), but most importantly for numpy arrays.

| | Sending side   | Receiving side  |
---|---|---
| text |  <code> socket.sendtext('Hello world! ') </code> | <code> txt = socket.recvtext() </code>   |
| bytes | <code> import numpy as np </code> <br/> <code> A = np.arange(1000000).reshape((2500,400)) </code> <br/> <code> socket.sendb(A) </code> | <code> A = socket.recvb() <code> |

### Closing
Remember to close your socket and free the port.

| | Both sides   |
---|---
| closing |  <code> socket.close() </code> | 

