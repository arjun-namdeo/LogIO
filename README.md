# logIO 
## Logging IO repository

A simple logging wrapper with more intuitive approach for logging information in the backend
This will support a great number of IO stream methods with nice and friendly looking
verbosity level.

Usage:


```python
from logIO import get_logger    
logger = get_logger(__name__)

# logger will use colors by default
# Info=Green, Warning=Orange, Error=Red, Critical=Red, Debug=White

logger.info("This will show as INFO log in console")
logger.warning("This will show as WARNING log in console", use_color=False)  
logger.critical("This will show as CRITICAL log in console")
logger.error("This will show as ERROR log in console")
logger.debug("This will show as DEBUG log in console")

```
    
    
    
