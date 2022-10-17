'''Custom Exceptions'''

class WrongFormatException(Exception):
    '''
    Exception that can be raised when the format type
    given as parameter is not supported.
    '''
    
class WrongMetaFileException(Exception):
    '''
    Exception that can be raised when the meta file 
    format is not correct.
    '''