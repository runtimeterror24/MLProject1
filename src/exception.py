import sys
from src.logger import logging

def error_message_detail(error,error_details:sys):
    #error_details is annotated with type sys, indicating that it should be an instance of sys module. 
    _,_,exc_tb= error_details.exc_info() #where(file,line) exception has occured

    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] and line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_details=error_detail)

    def __str__(self):
        return self.error_message
