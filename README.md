# logIO 
## Logging IO repository

A simple logging wrapper with more intuitive approach for logging information in the backend
This will support a great number of IO stream methods with nice and friendly looking
verbosity level.

Usage:

This is not yet ready but this will be the desirable use cases that I'm intending
    
    # Import the logger and setup for your module 
    from logIO import get_logger    
    logger = get_logger(__name__)
    
    # All the below methods will support following arguments
    #       msg                 `str`       Message to display
    #       use_colors          `bool`      Show the colors in output as 
                                            Info=Green, Warning=Orange, Error=Red, Critical=Red, Debug=White
    #       custom_color        `str`       You can give the name of the color that you want
    
    logger.info("This will show as INFO log in console")
    logger.warning("This will show as WARNING log in console", use_color=True)  
    logger.critical("This will show as WARNING log in console", use_color=True, custom_color="Yellow")
    logger.error("This will show as WARNING log in console", use_color=False)                               # No color
    logger.debug("This will show as WARNING log in console", use_color=True, custom_color="Cyan")
    
    
    
    
    