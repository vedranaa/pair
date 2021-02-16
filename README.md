# pair

Extension of the socket.socket class with functionality usefull for sending data between two computers on the same (wireless) network.
    
It requires coordinantion between the sender and receiver, as receiving side (using the current implementation) will (once receiving has been called) block execution of whatever is running, and keep on waiting for the data. So you need to be sure that something is in the socket, or on the way.

The intended usage is when two operators are sitting close by, and can (verbaly) agree when something is to be send/received.


| Inviting side   | Joining side  |
|---|---|
|  <code> import pair <br>import numpy as np</code>  | import  |
|---|---|
|  Invite | -  |
|  - | Join  |
|---|---|
